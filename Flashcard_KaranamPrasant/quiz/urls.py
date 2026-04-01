from django.urls import path
from . import views

urlpatterns = [
	path('', views.question_list, name='question_list'),
	path('add/', views.question_add, name='question_add'),
	path('practice/<int:pk>/', views.practice, name='practice'),
	path('check/<int:pk>/', views.check_answer, name='check_answer'),
]