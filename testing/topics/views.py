from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Test, Group, Question, QuestionAnswer, TestQuestion, Answer

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


def test_detail(request, test_id):
    template = 'topics/test.html'
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test_id=test_id)
    context = {
        'test': test,
        'questions': questions,
    }
    return render(request, template, context)


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
