from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Question
from django.template import loader
from django.http import Http404


# Create your views here.
# 首页


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


# 详情
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 结果
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# 投票
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
