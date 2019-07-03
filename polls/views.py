from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic


# Create your views here.
# 首页


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
#
# # 详情
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# # 结果
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # 复写该方法
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 投票
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice', None])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reversed('polls:results', args=(question.id,)))


'''
有些新的东西，我们要解释一下：

request.POST是一个类似字典的对象，允许你通过键名访问提交的数据。本例中，request.POST[’choice’]返回被选择选项的ID，并且值的类型永远是string字符串，那怕它看起来像数字！同样的，你也可以用类似的手段获取GET请求发送过来的数据，一个道理。
request.POST[’choice’]有可能触发一个KeyError异常，如果你的POST数据里没有提供choice键值，在这种情况下，上面的代码会返回表单页面并给出错误提示。PS：通常我们会给个默认值，防止这种异常的产生，例如request.POST[’choice’,None]，一个None解决所有问题。
在选择计数器加一后，返回的是一个HttpResponseRedirect而不是先前我们常用的HttpResponse。HttpResponseRedirect需要一个参数：重定向的URL。这里有一个建议，当你成功处理POST数据后，应当保持一个良好的习惯，始终返回一个HttpResponseRedirect。这不仅仅是对Django而言，它是一个良好的WEB开发习惯。
我们在上面HttpResponseRedirect的构造器中使用了一个reverse()函数。它能帮助我们避免在视图函数中硬编码URL。它首先需要一个我们在URLconf中指定的name，然后是传递的数据。例如'/polls/3/results/'，其中的3是某个question.id的值。重定向后将进入polls:results对应的视图，并将question.id传递给它。白话来讲，就是把活扔给另外一个路由对应的视图去干。
'''
