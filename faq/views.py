from django.shortcuts import render, redirect

from faq.models import Question, Choice

def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'faq/list_quest.html', {'questions' : questions})

def list_choice(request, id):
    choice = Choice.objects.filter(question_id=id)
    return render(request, 'faq/list_choice.html', {'choices' : choice})

# There is one parameter id.
# It is to indicate the choices related to the question ID
