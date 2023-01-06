from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    # path함수 알아보기! route(첫번재 인자)는 클라이언트가 요청할 path을 의미한다.
    # urls.py에서 path parameter로 정의하면 view 메소드에서 해당 인자를 넘겨받을 수 있다.
    # int 정수형 숫자, str 모든 문자열, slug 하이픈(-)이나 언저바(_)를 포함한 숫자 영, 문자열

    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    
    # 해석 : "answer/create/<int:question_id>/" 이 형식으로 불러지면
    #        view에서 answer_create함수를 불러와라, 근데 그 별칭은 answer_create로 하겠다.
    # 별칭을 짓는 이유는? url에 이름을 지으면 템프릿을 포함한 장고 어디에서나 명확하게 참조가 가능하다.

    # http://127.0.0.1:8000/pybo/2/에서 url을 매핑하기 위해 넣어준 것임
    # question_detail.html에서 <form action="{% url 'pybo:answer_create' question_id%}" method="post">에서
    # url 'pybo:answer_create'이 answer_create 별칭에 해당하는 URL 매핑 규칙을 등록한 것임
    # 이제 http://locahost:8000/pybo/answer/create/2/ 와 같은 페이지를 요청하면 URL 매핑 규칙에 의해 views.answer_create 함수가 호출될 것이다.
]