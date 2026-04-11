from django.contrib import admin
from .models import BibleQuiz, BibleQuizLoad

class BibleQuizAdmin(admin.ModelAdmin):
    list_display = ('level', 'question', 'correct_answer')
    list_filter = ('level', 'question', 'correct_answer')
    search_fields = ('level', 'question', 'correct_answer')
    ordering = ('level', 'question', 'correct_answer')


class BibleQuizLoadAdmin(admin.ModelAdmin):
    list_display = ('level', 'question', 'correct_answer')
    list_filter = ('level', 'question', 'correct_answer')
    search_fields = ('level', 'question', 'correct_answer')
    ordering = ('level', 'question', 'correct_answer')


admin.site.register(BibleQuiz, BibleQuizAdmin)
admin.site.register(BibleQuizLoad, BibleQuizLoadAdmin)

