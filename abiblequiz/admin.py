from django.contrib import admin
from .models import BibleQuiz, VerseOfDay, Contact, SubmitQuestion


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


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    ordering = ('name', 'email')


class SubmitQuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    list_filter = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    search_fields = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')
    ordering = ('category', 'difficulty', 'question_text', 'correct_answer', 'reference')


admin.site.register(BibleQuiz, BibleQuizAdmin)
admin.site.register(VerseOfDay, VerseOfDayAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SubmitQuestion, SubmitQuestionAdmin)

