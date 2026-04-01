from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Question
from .forms import QuestionForm


def question_list(request):
	questions = Question.objects.all().order_by('-id')
	return render(request, 'quiz/question_list.html', {'questions': questions})


def question_add(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Question added!')
			return redirect('question_list')
	else:
		form = QuestionForm()
	return render(request, 'quiz/question_form.html', {'form': form})


def practice(request, pk):
	question = get_object_or_404(Question, pk=pk)
	streak = int(request.session.get('streak', 0) or 0)
	best_streak = int(request.session.get('best_streak', 0) or 0)
	return render(request, 'quiz/practice.html', {'q': question, 'streak': streak, 'best_streak': best_streak})


def check_answer(request, pk):
	question = get_object_or_404(Question, pk=pk)
	if request.method != 'POST':
		return redirect('practice', pk=pk)

	user_answer = request.POST.get('answer', '').strip()
	is_correct = False
	correct = ''

	if question.type == 'text':
		correct = (question.answer_text or '').strip()
		is_correct = user_answer.lower() == correct.lower()
	else:
		correct = question.correct_option
		is_correct = user_answer.lower() == (question.correct_option or '').lower()

	# Update streak in session
	streak = int(request.session.get('streak', 0) or 0)
	best_streak = int(request.session.get('best_streak', 0) or 0)
	if is_correct:
		streak += 1
		if streak > best_streak:
			best_streak = streak
			new_best = True
		else:
			new_best = False
	else:
		streak = 0
		new_best = False
	request.session['streak'] = streak
	request.session['best_streak'] = best_streak

	context = {
		'q': question,
		'user_answer': user_answer,
		'correct': correct,
		'is_correct': is_correct,
		'streak': streak,
		'best_streak': best_streak,
		'new_best': new_best,
	}
	return render(request, 'quiz/result.html', context)

