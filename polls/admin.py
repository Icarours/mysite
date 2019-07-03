from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 不能同时指定fields和fieldssets
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 将Question的相关属性全部显示出来
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 筛选,按时间日期筛选
    list_filter = ['pub_date']
    # 搜索框,搜素
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
