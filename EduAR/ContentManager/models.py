from django.db import models

# Create your models here.

class Term(models.Model):
    term_number = models.IntegerField(unique=True)

class Quiz(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    option1 = models.CharField(blank=True, null=True, max_length=250)
    option2 = models.CharField(blank=True, null=True, max_length=250)
    option3 = models.CharField(blank=True, null=True, max_length=250)
    option4 = models.CharField(blank=True, null=True, max_length=250)
    correct_answer = models.CharField(blank=True, null=True, max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    


    


