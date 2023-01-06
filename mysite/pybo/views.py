from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm


# from django.http import HttpResponse

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


# 답변 등록을 의한 메서드(pybo.urls.py)
def answer_create(request, question_id):
    # request() : url를 통해 form에 입력한 사용자의 데이터를 포함하여 여러 요청된 정보를 갖고 오는 객체
    # - 터미널에 print(request.POST)를 통해 확인해보면, request가 form에 입력한 데이터를 갖고 있는 것을 확인할 수 있음

    # redirect() : 해당 함수가 호출되었을 때, 지정해논 경로로 이동시키는 역할
    # 만약 views에서 return redirect('/')이라고 했으면 urls에 가서 urlpatterns에 있는 리스트에 path("/", index)인 것을 찾아온다.
    # 최종적으로 index()가 response되는 것임

    question = get_object_or_404(Question, pk=question_id)
    print(request.POST)
    # # 첫번째 방법
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # # 두번째 방법
    # # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # # answer.save()
    # return redirect('pybo:detail', question_id=question.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)