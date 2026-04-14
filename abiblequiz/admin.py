from django.contrib import admin
from .models import BibleQuiz

class BibleQuizAdmin(admin.ModelAdmin):
    list_display = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    list_filter = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    search_fields = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    ordering = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')


admin.site.register(BibleQuiz, BibleQuizAdmin)

