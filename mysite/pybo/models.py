from django.db import models

# 질문 클래스
class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name = "제목")
    # 제목은 '텍스트','최대 200글자' 만약 프라이머리 키로 설정하고 싶으면 'primary_key=True' 넣으면 됨
    content = models.TextField(verbose_name = "내용")
    # 내용은 '텍스트', '글자수 제한없음'
    create_date = models.DateTimeField(verbose_name = "작성일시")
    # 작성일시는 '날짜/시간'
    writer = models.CharField(max_length=10, default="NaN", verbose_name = "작성자")

    def __str__(self):
    # id대신 제목을 표기할 수 있음
        return self.subject

# 답변 클래스
# : 질문에 대한 답변에 해당되므로 Question 모델을 속성으로 가져가야 한다.
class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    # 기본 모델의 속성을 연결하기 위한 "ForeignKey"가 필요하다.
    # on_delete=models.CASCADE 는 ForeignKey의 원키 질문이 삭제되면 답변도 함께 삭제된다는 의미
    content = models.TextField()
    # 내용은 '텍스트', '글자수 제한없음'
    create_date = models.DateTimeField()
    # 작성일시는 '날짜/시간'
    writer = models.CharField(max_length=10, default="NaN", verbose_name="작성자")

