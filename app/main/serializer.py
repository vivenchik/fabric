from rest_framework import serializers

from .models import Poll, Question, Answer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'name', 'begin_date', 'end_date', 'description']

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, poll, validated_data):
        poll.name = validated_data.get('name', poll.name)
        poll.end_date = validated_data.get('end_date', poll.end_date)
        poll.description = validated_data.get('description', poll.description)
        poll.save()
        return poll


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'text', 'type', 'choices']

    def get_poll(self, obj):
        return obj.poll.id

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, question, validated_data):
        question.text = validated_data.get('text', question.text)
        question.type = validated_data.get('type', question.type)
        question.save()
        return question


class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', 'type', 'choices']


class UserPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'begin_date', 'end_date', 'description', 'questions']

    questions = UserQuestionSerializer(many=True, read_only=True)


class UserSimplePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'description']


class UserExtendedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'text', 'type', 'choices']

    poll = UserSimplePollSerializer(many=False, read_only=True)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer']

    question = UserExtendedQuestionSerializer(many=False, read_only=True)


class AnswerCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['question'].type in (0, 1) and len(data['answer']) != 1:
            raise serializers.ValidationError('You cant choose multiple.')
        return data

    class Meta:
        model = Answer
        fields = ['user', 'question', 'answer']

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)
