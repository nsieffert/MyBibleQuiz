from django.db import models


class BibleQuiz(models.Model):
    level = models.IntegerField()
    question = models.CharField(max_length=200)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class BibleQuizLoad(models.Model):
    level = models.IntegerField()
    question = models.CharField(max_length=200)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question
