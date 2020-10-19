from django.contrib import admin
from .models import Term, Quiz, Question
# Register your models here.

admin.site.register(Term)
admin.site.register(Quiz)
admin.site.register(Question)

admin.site.site_header = "EduAR CMS"
admin.site.index_title = "Content Management"