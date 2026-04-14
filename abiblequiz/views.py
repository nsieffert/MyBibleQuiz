from django.shortcuts import render, redirect
from .models import BibleQuiz
import random


def index(request):
    # redirects user to the setup page to begin a session
    # question_order comes from # 6 in setup()
    if 'question_order' not in request.session:
        return redirect('setup')

   # 1. Get the list of randomized IDs from setup() - random.shuffle, set score
    question_order = request.session['question_order']
    total_questions = len(question_order)
    # total_questions = 5
    current_index = request.session.get('current_question_index', 0)

    # Handling the end of the game - index.html line 32
    if current_index >= total_questions:
        context = {
            'game_over': True,
            'score': request.session.get('score', 0),
            'total': total_questions,
        }
        return render(request, 'index.html', context)

    # 2. Grab the ID for the current turn get the question
    current_question_id = question_order[current_index]
    question = BibleQuiz.objects.get(id=current_question_id)

    # reset the fields to await user's input
    message = None
    is_correct = None
    show_next_button = False
    show_end_button = False

    # if user wants to end the game:
    if 'end_game' in request.POST:
        context = {
            'game_over': True,
            'score': request.session.get('score', 0),
            'total': total_questions,
        }
        return render(request, 'index.html', context)

    # If user submits an answer (not end of game):
    if request.method == 'POST':
        if 'next_question' in request.POST:
            request.session['current_question_index'] += 1
            return redirect('index')

        user_answer = request.POST.get('user_answer', '').strip().upper()

        if user_answer == question.correct_answer.upper():
            message = "Correct!"
            is_correct = True
            request.session['score'] += 1
        else:
            message = (f"Incorrect. The correct answer was {question.correct_answer}.")
            is_correct = False

        show_next_button = True
        show_end_button = True

    context = {
        'question': question,
        'message': message,
        'is_correct': is_correct,
        'score': request.session.get('score', 0),
        'show_next_button': show_next_button,
        'show_end_button': show_end_button,
        'game_over': False,
    }
    return render(request, 'index.html', context)


def setup(request):
    # Pull from models to get unique categories/difficulties
    categories = BibleQuiz.objects.values_list('category', flat=True).distinct()
    difficulties = BibleQuiz.objects.values_list('difficulty', flat=True).distinct()

    if request.method == 'POST':
        selected_cat = request.POST.get('category')
        selected_diff = request.POST.get('difficulty')

     # 1. Pull all the questions from the database
        questions = BibleQuiz.objects.all()

        # 2. If they don't pick All, then narrow down by their selection
        if selected_cat != "All":
            questions = questions.filter(category=selected_cat)

        # 3. If they don't pick All, then narrow down by their selection
        if selected_diff != "All":
            questions = questions.filter(difficulty=selected_diff)

        # 4. Now pull all that they DID Select
        question_ids = list(questions.values_list('id', flat=True))

        # 5. Shuffle the selected IDs
        random.shuffle(question_ids)

        # 6 Save shuffled to session
        request.session['question_order'] = question_ids
        request.session['selected_category'] = selected_cat
        request.session['selected_difficulty'] = selected_diff
        request.session['current_question_index'] = 0
        request.session['score'] = 0

        # 7 Send them to the game page
        return redirect('index')

    context = {
        'categories': categories,
        'difficulties': difficulties,
    }
    return render(request, 'setup.html', context)
