"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog import views
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', views.home),
    url('about/', views.about,name="about"),
    url('contact/', views.contact,name="contact"),
    url('dashboard/', views.dashboard,name="dashboard"),
    url('signup/', views.user_signup,name="signup"),
    url('logout/', views.user_logout,name="logout"),
    url('login/', views.user_login,name="login"),
    url('addpost/', views.add_post,name="addpost"),
    url('updatepost/<int:id>/', views.update_post,name="updatepost"),
    url('delete/<int:id>/', views.delete_post,name="deletepost"),

    
]

#  from django.conf.urls import url, include
#  from django.contrib import admin
#  urlpatterns = [
#      url(r'^admin/', admin.site.urls),
#      url('', views.home),
#      url('about/', views.about,name="about"),
#      url('', views.home),
#      url('', views.home),
#      url('', views.home),
#      url('', views.home),
#      url('', views.home),
#      url('', views.home),
#      url('', views.home),
#    ]
