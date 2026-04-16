from django.db import models


class BibleQuiz(models.Model):
    category = models.CharField(max_length = 100)
    difficulty = models.CharField(max_length = 100)
    question_text = models.CharField(max_length = 200)
    option_a = models.CharField(max_length=400)
    option_b = models.CharField(max_length=400)
    option_c = models.CharField(max_length=400)
    option_d = models.CharField(max_length=400)
    correct_answer = models.CharField(max_length=200)
    reference = models.CharField(max_length = 200)

    def __str__(self):
        return self.question_text


class VerseOfDay(models.Model):
    theme = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    verse = models.CharField(max_length = 1000)

    def __str__(self):
        return self.theme

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    note = models.CharField(max_length = 500)

    def __str__(self):
        return self.name


class SubmitQuestion(models.Model):
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    question_text = models.CharField(max_length=200)
    option_a = models.CharField(max_length=400)
    option_b = models.CharField(max_length=400)
    option_c = models.CharField(max_length=400)
    option_d = models.CharField(max_length=400)
    correct_answer = models.CharField(max_length=200)
    reference = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text