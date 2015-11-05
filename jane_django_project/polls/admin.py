from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):
	extra = 3
	model = Choice

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}), ('Date Info', {'fields': ['pub_date']})]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date','was_published_in_last_week')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)



