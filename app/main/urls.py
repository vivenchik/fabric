from django.urls import path

from .views import PollViewAll, PollView, QuestionViewAll, QuestionView


urlpatterns = [
    path('poll/', PollViewAll.as_view(), name='poll_all'),
    path('poll/<int:id>/', PollView.as_view(), name='poll_single'),
    path('question/', QuestionViewAll.as_view(), name='question_all'),
    path('question/<int:id>/', QuestionView.as_view(), name='question_single'),
]
