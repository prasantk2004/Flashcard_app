from django.db import models

# Create your models here.

class Question(models.Model):
	QUESTION_TYPES = (
		('mcq', 'Multiple Choice'),
		('text', 'Text Answer'),
	)
	text = models.CharField(max_length=255)
	type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='text')
	# For text questions
	answer_text = models.CharField(max_length=255, blank=True)
	# For MCQ questions
	option_a = models.CharField(max_length=255, blank=True)
	option_b = models.CharField(max_length=255, blank=True)
	option_c = models.CharField(max_length=255, blank=True)
	option_d = models.CharField(max_length=255, blank=True)
	correct_option = models.CharField(max_length=1, blank=True)  # 'a','b','c','d'

	# Optional media for question prompt
	question_image = models.ImageField(upload_to='quiz/question_images/', blank=True, null=True)
	question_audio = models.FileField(upload_to='quiz/question_audio/', blank=True, null=True)
	question_video = models.FileField(upload_to='quiz/question_videos/', blank=True, null=True)

	# Optional media for answer (for text questions, or to show after answering)
	answer_image = models.ImageField(upload_to='quiz/answer_images/', blank=True, null=True)
	answer_audio = models.FileField(upload_to='quiz/answer_audio/', blank=True, null=True)
	answer_video = models.FileField(upload_to='quiz/answer_videos/', blank=True, null=True)

	def __str__(self):
		return self.text[:50]
