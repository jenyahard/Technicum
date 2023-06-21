from django.shortcuts import render

from scripts.gpt_test import get_gpt_answer


def question_wiew(request):
    template = 'questions.html'
    context = {'answer': ''}
    if request.method == 'POST':
        question = request.POST.get('field1')
        answer = get_gpt_answer(question)
        context = {'answer': answer}
    return render(request, template, context)
