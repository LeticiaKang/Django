from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    # POST인 경우 사용자 생성
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            # 개별적으로 값을 가져옴 (form.cleaned_data.get)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            # 사용자 이름과 비번이 일치 하는지 확인해 줌 (django.contrib.auth.authenticate)
            user = authenticate(username=username, password=raw_password)

            # 사용자 세션을 생성 (django.contrib.auth.login)
            login(request, user)  # 로그인
            return redirect('index')

    else:
        form = UserForm()

    # 아닌 경우 회원가입 화면을 보여줌
    return render(request, 'common/signup.html', {'form': form})