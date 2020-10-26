from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from djongo import models
from django.core.validators import URLValidator
from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from djangotoolbox.fields import ListField
#from .forms import BlogContentForm

def script_injection(value):
    if value.find('<script>') != -1:
        raise ValidationError(_('Script injection in %(value)s'),
                              params={'value': value})
# Create your models here.

class newModel(models.Model):
    myatr = models.CharField(blank=True, null=True, max_length=250)
    list_answers =  ListField()

class Term(models.Model):
    term_number = models.IntegerField(unique=True)
    def __int__(self):
        return self.term_number

class Quiz(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True, related_name='quizzes')
    title = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

class Question(models.Model):
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    option1 = models.CharField(blank=True, null=True, max_length=250)
    option2 = models.CharField(blank=True, null=True, max_length=250)
    option3 = models.CharField(blank=True, null=True, max_length=250)
    option4 = models.CharField(blank=True, null=True, max_length=250)
    correct_answer = models.CharField(blank=True, null=True, max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')

    def __str__(self):
        return self.text
    
class QuizQuestions(models.Model):
    category = models.CharField(blank=True, null=True, max_length=250)
    type = models.CharField(blank=True, null=True, max_length=250)
    difficulty = models.CharField(blank=True, null=True, max_length=250)
    question = models.CharField(blank=True, null=True, max_length=250)
    correct_answer = models.CharField(blank=True, null=True, max_length=250)
    incorrect_answers =  ArrayField(models.CharField(max_length=10, blank=True),size=8)
    objects = models.DjongoManager()



    
    
    
# class BlogContent(models.Model):
#     comment = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     class Meta:
#         abstract = True


