from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.user_login, name='login'),
   path('index', views.index, name='index'),
   path('view_term<int:term_number>', views.view_term, name='view_term'),
   path('create_quiz<int:term_number>', views.create_quiz, name='create_quiz')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)