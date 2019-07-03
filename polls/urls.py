from django.urls import path
from . import views

'''
接下来，在项目的主urls.py文件中添加urlpattern条目，指向我们刚才建立的polls这个app独有的urls文件，这里需要导入include模块。
打开mysite/urls.py文件，代码如下：
'''
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # 添加新的单词'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
]
'''
path()方法：
路由系统中最重要的path()方法可以接收4个参数，其中2个是必须的：route和view，以及2个可选的参数：kwargs和name。

route：

route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项，然后执行该条目映射的视图函数或下级路由，其后的条目将不再继续匹配。因此，url路由的编写顺序非常重要！

需要注意的是，route不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 https://www.example.com/myapp/时，它会尝试匹配 myapp/。处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。

view：

view指的是处理当前url请求的视图函数。当Django匹配到某个路由条目时，自动将封装的HttpRequest对象作为第一个参数，被“捕获”的参数以关键字参数的形式，传递给该条目指定的视图view。

kwargs：

任意数量的关键字参数可以作为一个字典传递给目标视图。

name：

对你的URL进行命名，让你能够在Django的任意处，尤其是模板内显式地引用它。这是一个非常强大的功能，相当于给URL取了个全局变量名，不会将url匹配地址写死。

path()方法的四个参数，每个都非常有讲究，这里先做基本的介绍，在后面有详细的论述。
'''
