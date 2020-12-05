from django.db import models


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

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES)

    def __str__(self):
        return f'{self.poll.name} {self.text}'
