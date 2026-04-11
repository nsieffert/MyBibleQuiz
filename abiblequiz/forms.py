from django import forms


class BibleQuizForm(forms.Form):
    level = forms.IntegerField()
    question = forms.CharField(max_length=200)
    optionA = forms.CharField(max_length=200)
    optionB = forms.CharField(max_length=200)
    optionC = forms.CharField(max_length=200)
    optionD = forms.CharField(max_length=200)
    correct_answer = forms.CharField(max_length=200)


class BibleQuizLoadForm(forms.Form):
    level = forms.IntegerField()
    question = forms.CharField(max_length=200)
    optionA = forms.CharField(max_length=200)
    optionB = forms.CharField(max_length=200)
    optionC = forms.CharField(max_length=200)
    optionD = forms.CharField(max_length=200)
    correct_answer = forms.CharField(max_length=200)