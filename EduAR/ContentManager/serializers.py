from rest_framework import serializers
from .models import Term, Quiz, Question, QuizQuestions



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = "__all__"

class TermSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = Term
        fields = "__all__"

class QuizQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestions
        fields = '__all__'