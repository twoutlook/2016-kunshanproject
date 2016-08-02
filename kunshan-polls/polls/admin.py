from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):

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
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
