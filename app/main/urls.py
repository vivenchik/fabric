from django.urls import path

from .views import PollViewAll, PollView, QuestionViewAll, QuestionView, UserPollViewAll, UserAnswerViewAll


urlpatterns = [
    path('admin/poll/', PollViewAll.as_view(), name='admin_poll_all'),
    path('admin/poll/<int:id>/', PollView.as_view(), name='admin_poll_single'),
    path('admin/question/', QuestionViewAll.as_view(), name='admin_question_all'),
    path('admin/question/<int:id>/', QuestionView.as_view(), name='admin_question_single'),
    path('poll/', UserPollViewAll.as_view(), name='user_poll_all'),
    path('answer/<int:user>/', UserAnswerViewAll.as_view(), name='user_answer_all'),
]
