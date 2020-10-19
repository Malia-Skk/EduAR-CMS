from django.db import models

# Create your models here.

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
    


    


