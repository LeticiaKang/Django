from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('subject', 'writer')


admin.site.register(Question, QuestionAdmin)