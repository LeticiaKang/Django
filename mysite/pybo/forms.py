from django import forms
from pybo.models import Answer, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        # fields = ['subject',  'author',  'content']  # QuestionForm에서 사용할 Question 모델의 속성
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성

        labels = {
            'subject': '제목',
            # 'author' : '작성자',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        # fields = [ 'author' , 'content']
        fields = [ 'content']
        labels = {
            # 'author' : '작성자',
            'content': '답변내용',
        }
