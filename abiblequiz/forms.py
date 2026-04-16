from django import forms


class BibleQuizForm(forms.Form):
    category = forms.CharField(max_length=100)
    difficulty = forms.CharField(max_length=100)
    question_text = forms.CharField(max_length=200)
    option_a = forms.CharField(max_length=400)
    option_b = forms.CharField(max_length=400)
    option_c = forms.CharField(max_length=400)
    option_d = forms.CharField(max_length=400)
    correct_answer = forms.CharField(max_length=200)
    reference = forms.CharField(max_length=400)


class VerseOfDayForm(forms.Form):
    theme = forms.CharField(max_length = 100)
    address = forms.CharField(max_length = 100)
    verse = forms.CharField(max_length = 1000)


class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 100)
    note = forms.CharField(max_length=500)


class SubmitQuestionForm(forms.Form):
    category = forms.CharField(max_length=100)
    difficulty = forms.CharField(max_length=100)
    question_text = forms.CharField(max_length=200)
    option_a = forms.CharField(max_length=400)
    option_b = forms.CharField(max_length=400)
    option_c = forms.CharField(max_length=400)
    option_d = forms.CharField(max_length=400)
    correct_answer = forms.CharField(max_length=200)
    reference = forms.CharField(max_length=200)