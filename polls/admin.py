from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date information", {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInLine]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
