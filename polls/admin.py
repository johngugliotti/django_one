from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

#admin.site.register(Question)

"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
"""


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
