from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.\

from django.http import HttpResponse


def index(request):
    question_list = Question.objects.order_by('-create_date')
    # 질문 목록을 작성일시 역순으로 정력하라는 의미(order_by: 역순, orderby : 최신순)
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    # render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    # question_list데이터를 pybo/question_list.html(템플릿)에 적용하여 HTML 생성
    # question_list.html을 작성해서 읽을 수 있도록 해야한다.

    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)