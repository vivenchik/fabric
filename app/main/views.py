from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Poll, Question
from .serializer import PollSerializer, QuestionSerializer


def success_response(id):
    return {
        'result': 'success',
        'id': id,
    }


def error_response():
    return {
        'result': 'error',
        'error_code': 'wrong_data'
    }


class PollViewAll(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def post(self, request):
        poll = request.data.get('poll')
        serializer = PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll_in_base = serializer.save()
            return Response(success_response(poll_in_base.id))
        return Response(error_response())


class PollView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        poll = get_object_or_404(Poll, id=id)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def delete(self, request, id):
        poll = get_object_or_404(Poll, id=id)
        poll.delete()
        return Response(success_response(id), status=204)

    def put(self, request, id):
        poll_in_base = get_object_or_404(Poll, id=id)
        data = request.data.get('poll')
        serializer = PollSerializer(poll_in_base, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            poll_in_base = serializer.save()
            return Response(success_response(poll_in_base.id))
        return Response(error_response())


class QuestionViewAll(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request):
        question = request.data.get('question')
        serializer = QuestionSerializer(data=question)
        if serializer.is_valid(raise_exception=True):
            question_in_base = serializer.save()
            return Response(success_response(question_in_base.id))
        return Response(error_response())


class QuestionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        question = get_object_or_404(Question, id=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def delete(self, request, id):
        question = get_object_or_404(Question, id=id)
        question.delete()
        return Response(success_response(id), status=204)

    def put(self, request, id):
        question_in_base = get_object_or_404(Question, id=id)
        data = request.data.get('question')
        serializer = QuestionSerializer(question_in_base, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            question_in_base = serializer.save()
            return Response(success_response(question_in_base.id))
        return Response(error_response())
