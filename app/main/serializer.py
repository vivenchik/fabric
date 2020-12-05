from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    begin_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, poll, validated_data):
        poll.name = validated_data.get('name', poll.name)
        poll.end_date = validated_data.get('end_date', poll.end_date)
        poll.description = validated_data.get('description', poll.description)
        poll.save()
        return poll


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    poll = serializers.SerializerMethodField()
    text = serializers.CharField()
    type = serializers.IntegerField()

    def get_poll(self, obj):
        return obj.poll.id

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, question, validated_data):
        question.text = validated_data.get('text', question.text)
        question.type = validated_data.get('type', question.type)
        question.save()
        return question
