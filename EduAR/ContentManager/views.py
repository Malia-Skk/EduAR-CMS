from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Term, Quiz, Question
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TermSerializer
from rest_framework import generics

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username'] = username
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def view_term(request, term_number):
    term = Term.objects.get(term_number=term_number)
    quizzes = Quiz.objects.filter(term=term)

    context = {
        'term':term,
        'quizzes':quizzes
    }
    return render(request, 'view_term.html', context)

def create_quiz(request, term_number):
    if request.method == 'POST':
        #create quiz
        #View the quiz you have created, view_quiz(request, quiz.id)
        pass
    term = Term.objects.get(term_number=term_number)
    context = {'term':term}
    return render(request, 'create_quiz.html', context)

def view_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    term = quiz.term
    questions = Question.objects.filter(quiz=quiz)

    context = {
        'quiz':quiz,
        'term':term,
        'questions':questions
    }

    return render(request, 'view_quiz.html', context)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list'
    }
    return  Response(api_urls)

@api_view(['GET'])
def term_list(request):
    terms = Term.objects.all()
    serializer = TermSerializer(terms, many=True)
    return Response(serializer.data)
