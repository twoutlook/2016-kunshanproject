from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # fields = [ 'question_text','pub_date']

    fieldsets = [
        ('問題︰',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
