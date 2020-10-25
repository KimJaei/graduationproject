"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# import 내용은 습관처럼 암기!
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
import portfolio.views
import accounts.views
import c_type.views

# path('~의 url이 입력되면', ~에있는 함수를 띄워라.)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name="index"),
    path('blog/', include('blogapp.urls')) ,  # blog/하면 blogapp.urls에서 url불러옴
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
    path('c_type/', include('c_type.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 로 해도 된다.