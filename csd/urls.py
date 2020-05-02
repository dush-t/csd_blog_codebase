"""csd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/<str:name>/<int:age>', views.say_hello),
    path('posts', views.get_post),
    path('sign_up/', views.sign_up),
    path('sign_in/', views.sign_in),
    path('sign_out/', views.sign_out),
    path('me/', views.profile),

    path('create_post/', views.create_post),
    path('view_post/<int:pk>', views.view_post, name='view_post'),
    path('author_profile/<str:username>', views.author_profile),
]
