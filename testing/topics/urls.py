from . import views
from django.urls import path, re_path


app_name = 'topics'
urlpatterns = [
    path('', views.index, name='group_list'),
    path('group/<slug:slug>/', views.tests_in_group, name='tests_in_group'),
    path('tests/<int:test_id>/', views.test_detail, name='test_detail'),
    path('tests/<int:test_id>/<int:question_id>/', views.question_detail, name='question_detail'),
    path('result/', views.results, name='results')
]