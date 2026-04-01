from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'text', 'type',
			'answer_text',
			'option_a', 'option_b', 'option_c', 'option_d', 'correct_option',
			'question_image', 'question_audio', 'question_video',
			'answer_image', 'answer_audio', 'answer_video',
		]
		widgets = {
			'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter question text'}),
			'answer_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter correct text answer'}),
			'option_a': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option A'}),
			'option_b': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option B'}),
			'option_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option C'}),
			'option_d': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option D'}),
			'correct_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'a/b/c/d'}),
		}

	def clean(self):
		cleaned = super().clean()
		qtype = cleaned.get('type')
		if qtype == 'text' and not cleaned.get('answer_text'):
			raise forms.ValidationError('Provide the correct text answer for text questions.')
		if qtype == 'mcq':
			missing = [f for f in ['option_a','option_b','option_c','option_d','correct_option'] if not cleaned.get(f)]
			if missing:
				raise forms.ValidationError('Provide all options and the correct option for MCQ.')
			if cleaned.get('correct_option') not in ['a','b','c','d']:
				raise forms.ValidationError('Correct option must be one of: a, b, c, d.')
		return cleaned