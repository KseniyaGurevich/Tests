from . import views
from django.urls import path

app_name = 'topics'
urlpatterns = [
    path('', views.index, name='group_list'),
    path('group/<slug:slug>/', views.tests_in_group, name='tests_in_group'),
    path('tests/<int:test_id>/', views.test_detail, name='test_detail')
]