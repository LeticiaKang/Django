"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('pybo/', views.index),
    path('pybo/', include('pybo.urls')),
    # 이제 pybo/question/create, pybo/answer/create 등의 pybo/로 시작하는 URL을 추가해야 할 때 config/urls.py 파일을 수정할 필요없이 pybo/urls.py 파일만 수정하면 된다.
]
