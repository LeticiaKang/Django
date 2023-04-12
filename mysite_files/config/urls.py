
from django.contrib import admin
from django.urls import path, include
from pybo import views

# from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('pybo/', include('pybo.urls')),
    # http://localhost:8000/pybo/으로 시작하는 URL은 'pybo.urls'를 참조해서 이동하게 된다.

    path('common/', include('common.urls')),
    # http://localhost:8000/common/ 시작하는 모든 URL은 common/urls.py파일을 참조할 것이다.

    path('', views.index, name='index'),  # '/' 에 해당되는 path

]
