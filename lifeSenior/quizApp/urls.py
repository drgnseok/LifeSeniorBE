from django.urls import path
from .views import home, solveQuiz

app_name = 'quizApp'

urlpatterns = [
    path('home', home, name="home"),
    path('solveQuiz/<int:quiz_id>/<str:choice_text>', solveQuiz, name="solveQuiz")

]
    