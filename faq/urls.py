from django.urls import path

from faq import views

urlpatterns = [
    path('', views.list_questions, name = 'list_questions'),
    path('<int:id>/', views.list_choice, name = 'list_choice'),
]

# The ID (integer) will be the URL to indicate the choices of a question.
