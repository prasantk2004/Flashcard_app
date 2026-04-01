from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'type', 'answer_text', 'correct_option')
	list_filter = ('type',)
	search_fields = ('text', 'answer_text')
