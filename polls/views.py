from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 首页
from polls.models import Question


def index(request):
    latest_question_list =Question.objects.order_by
    return HttpResponse("hello world.You are at the polls index.")


# 详情
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# 结果
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# 投票
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
