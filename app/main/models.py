from django.db import models
from django.contrib.postgres.fields import ArrayField


class Poll(models.Model):
    name = models.CharField(max_length=100)
    begin_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPE_CHOICES = [
        (0, 'text'),
        (1, 'single_choice'),
        (2, 'multiple_choice'),
    ]

    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES)
    choices = ArrayField(models.CharField(max_length=30), null=True)

    def __str__(self):
        return f'{self.poll.name} {self.text}'


class Answer(models.Model):
    user = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer = ArrayField(models.TextField())

    class Meta:
        unique_together = (('user', 'question'),)
