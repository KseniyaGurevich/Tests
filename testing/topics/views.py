from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from .models import Test, Group, Question, QuestionAnswer, TestQuestion, Answer
from .forms import AnswerForm
NUMBER_OF_POSTS: int = 10


class QuestionLDetailView(DetailView):
    model = Question
    template_name = 'topics/questions.html'
    #context_object_name = 'current_question'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.resquest.data)
    #     # context['test.id'] = self.resquest.data
    #     # return context

    # def get_queryset(self):
    #     #test = self.kwargs.get('id')
    #     #print(test)
    #     return Question.objects.all().order_by('id')
    #     #return Question.objects.filter(test=test).order_by('id')

    # def get_queryset(self):
    #     test_id = self.request.get('test_id')
    #     quest = Question.objects.filter
    #     print(quest.values())
    #     qs = super().get_queryset()
    #     print('qs', qs)
    #     test = self.kwargs.get('name')
    #     print(test)
    #     return qs.filter(test__id=test)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = AnswerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('topics:question_detail', pk=self.kwargs.get('pk'))


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


# def test_detail(request, test_id):
#     template = 'topics/test.html'
#     test = get_object_or_404(Test, id=test_id)
#     question = Question.objects.filter(test_id=test.id).first()
#     context = {
#         'test': test,
#         'question': question,
#     }
#     return render(request, template, context)


def test_detail(request, test_id):
    template = 'topics/test.html'
    test = get_object_or_404(Test, id=test_id)
    question = Question.objects.filter(test_id=test.id).order_by('id').first()
    context = {
        'test': test,
        'question': question,
    }
    return render(request, template, context)


def question_detail(request, test_id, question_id):
    template = 'topics/questions2.html'
    test = get_object_or_404(Test, id=test_id)
    question_ids = Question.objects.filter(test_id=test.id).values_list('id', flat=True)
    print(question_ids)
    if question_id in question_ids:
        question = get_object_or_404(Question, id=question_id)
    # for question in questions:
    #     context = {
    #         'test': test,
    #         'question': question,
    #     }
    #     return render(request, template, context)
        context = {
            'test': test,
            'question': question,
            'question_ids': question_ids,
        }
        return render(request, template, context)
    else:
        return render(request, 'topics/result.html')


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

