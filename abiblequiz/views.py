from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import BibleQuiz, BibleQuizLoad
from .forms import BibleQuizForm, BibleQuizLoadForm


def index(request):
    # 1. Initialize session variables if they don't exist yet
    if 'score' not in request.session:
        request.session['score'] = 0
        request.session['current_question_index'] = 0

    # Grab all questions in order
    all_questions = BibleQuiz.objects.all()

    # Stop if there are no questions in the database
    if not all_questions.exists():
        return render(request, 'abiblequiz/index.html')

    # Get the current question based on the saved index
    current_index = request.session['current_question_index']

    # If the user answered all available questions but didn't reach 5, loop back to the start
    if current_index >= len(all_questions):
        request.session['current_question_index'] = 0
        current_index = 0

    question = all_questions[current_index]

    # 2. HANDLE SUBMISSION
    if request.method == 'POST':
        selected_option_id = request.POST.get('option')

        if selected_option_id:
            selected_option = get_object_or_404(BibleQuiz, pk=selected_option_id)

            # Check answer and add to score
            is_correct = selected_option.correct_answer
            if is_correct:
                request.session['score'] += 1

            # Move on to the next question for the next turn
            request.session['current_question_index'] += 1

            # Check if they reached the winning score of 5!
            if request.session['score'] >= 5:
                # Reset the game for next time
                request.session['score'] = 0
                request.session['current_question_index'] = 0

                return render(request, 'index.html', {'winner': True})

            return render(request, 'index.html', {
                'question': question,
                'is_correct': is_correct,
                'score': request.session['score'],
                'submitted': True
            })

    # 3. HANDLE PAGE LOAD (GET)
    return render(request, 'abiblequiz/index.html', {
        'question': question,
        'score': request.session['score']
    })

def quiz_load(request):
    if request.method == 'POST':
        quiz_loader = BibleQuizLoadForm(request.POST)
        if quiz_loader.is_valid():
            level = quiz_loader.cleaned_data["level"]
            question = quiz_loader.cleaned_data["question"]
            optionA = quiz_loader.cleaned_data["optionA"]
            optionB = quiz_loader.cleaned_data["optionB"]
            optionC = quiz_loader.cleaned_data["optionC"]
            optionD = quiz_loader.cleaned_data["optionD"]
            correct_answer = quiz_loader.cleaned_data["correct_answer"]

            # this section stores the data in the database
            BibleQuizLoad.objects.create(level=level, question=question, optionA=optionA,
                                             optionB=optionB, optionC=optionC, optionD=optionD,
                                             correct_answer=correct_answer)
            messages.success(request, "Question Created Successfully")

    return render(request, 'templates/quiz_load.html')
        # return HttpResponse('Your message here')