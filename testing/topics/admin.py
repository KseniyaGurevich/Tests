from django.contrib import admin
from .models import Group, Test, Question, Answer, QuestionAnswer


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'group')
    list_editable = ('name', 'group')
    search_fields = ('name',)
    list_filter = ('group__title',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    list_editable = ('title', 'description', 'slug')
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk',  'test', 'name')
    list_editable = ('test', 'name',)
    list_filter = ('test__name',)
    search_fields = ('name',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'name', 'check')
    list_editable = ('name', 'question', 'check')
    list_filter = ('question__name',)
    search_fields = ('name',)


# @admin.register(TestQuestion)
# class TestQuestionAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'test', 'question')
#     list_editable = ('test', 'question')
#     search_fields = ('name',)


# @admin.register(QuestionAnswer)
# class QuestionAnswerAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'test', 'question', 'answer', 'check')
#     list_editable = ('test', 'question', 'answer', 'check')
#     search_fields = ('test__name',)