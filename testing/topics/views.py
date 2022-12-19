from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required

from .models import Test, Group, Question, QuestionAnswer, TestQuestion, Answer, UserTest
from .forms import AnswerForm
NUMBER_OF_POSTS: int = 10


def index(request):
    template = 'topics/index.html'
    group_list = Group.objects.all()
    paginator = Paginator(group_list, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def test_detail(request, test_id):
    template = 'topics/test.html'
    test = get_object_or_404(Test, id=test_id)
    question = Question.objects.filter(test_id=test.id).first()
    context = {
        'test': test,
        'question': question,
    }
    return render(request, template, context)


@login_required
def question_detail(request, test_id, question_id):
    template = 'topics/questions2.html'
    test = get_object_or_404(Test, id=test_id)
    question_ids = Question.objects.filter(test_id=test.id).values_list('id', flat=True)
    if question_id in question_ids:
        question = get_object_or_404(Question, id=question_id)
        context = {
            'test': test,
            'question': question,
            'question_ids': question_ids,
        }
        #answers = Answer.objects.filter(question_id=question_id).values_list('name', 'check')
        answers = question.answers.values_list('name', 'check')
        right_list = []
        for answer in answers:
            if answer[1] is True:
                right_list.append(answer[0])
        print(right_list)
        right_answers = 0
        wrong_answers = 0
        if request.method == "POST":
            check_list = request.POST.getlist('check')
            result = UserTest.objects.create(user=request.user, test_id=test_id)
            if check_list:
                if check_list == right_list:
                    print("Да!")
                    result.right_answers += 1
                else:
                    print("Нет!")
                    result.wrong_answers += 1
                    result.save()
                return render(request, template, context)
            else:
                context['error_message'] = 'Выберите один или несколько вариантов ответа'
                return render(request, template, context)
        return render(request, template, context)
    return render(request, 'topics/result.html')


@login_required
def tests_in_group(request, slug):
    template = 'topics/tests_in_group.html'
    group = get_object_or_404(Group, slug=slug)
    tests_list = group.groups.all()
    paginator = Paginator(tests_list, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, template, context)


def results(request, test_id):
    result = UserTest.objects.filter(user=request.user, test_id=test_id)
    return render(request, 'topics/result.html', {'result': result})
