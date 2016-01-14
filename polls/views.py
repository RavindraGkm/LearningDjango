from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # out_list = []
    # for q in latest_question_list:
    #     out_list.append(q.question_text)
    # return HttpResponse(', '.join(out_list))
    context = {'latest_questions': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You are looking at result of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question no %s" % question_id)