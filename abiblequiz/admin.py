from django.contrib import admin
from .models import BibleQuiz, VerseOfDay

class BibleQuizAdmin(admin.ModelAdmin):
    list_display = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    list_filter = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    search_fields = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    ordering = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')

class VerseOfDayAdmin(admin.ModelAdmin):
    list_display = ('theme', 'address', 'verse')
    list_filter = ('theme', 'address', 'verse')
    search_fields = ('theme', 'address', 'verse')
    ordering = ('theme', 'address', 'verse')

admin.site.register(BibleQuiz, BibleQuizAdmin)

