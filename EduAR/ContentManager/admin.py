from django.contrib import admin
from .models import Term, Quiz, Question, QuizQuestions, newModel
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .forms import *
from django.db import models
# Register your models here.
@admin.register(newModel)
class MyModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass

admin.site.register(Term)
admin.site.register(Quiz)
admin.site.register(Question)
#admin.site.register(QuizQuestions)
#admin.site.register(DynamicArrayMixin)

admin.site.site_header = "EduAR CMS"
admin.site.index_title = "Content Management"

# class MyModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     pass

#admin.site.register(QuizQuestions)

@admin.register(QuizQuestions)
class MyModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


    