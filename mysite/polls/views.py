from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question,Choice
def index(request):
    # print(request)
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list=Question.objects.order_by('pub_date')[0:5]
    output=", ".join([q.question_text for q in latest_question_list])
    context={'latest_question_list':latest_question_list}

    return render(request,'polls/index.html',context)
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    else:
        print("hello")
        return render(request, 'polls/details.html', {'question': question})
def result(request,question_id):
    return HttpResponse("you're looking at result of question %s." %Question.objects.get(pk=question_id).question_text)
def vote(request,question_id):
    return HttpResponse("you're voting on question %s."%Choice.objects.filter(pk=question_id))
