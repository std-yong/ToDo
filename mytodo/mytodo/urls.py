"""mytodo URL Configuration

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
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name="todo_list"),
    path('post', views.todo_post, name="post"),
    path('<int:pk>', views.todo_detail, name="detail"),
    path('<int:pk>/edit', views.todo_edit, name="edit"),
    path('done/', views.done_list, name='done_list'),
    path('done/<int:pk>', views.todo_done, name='todo_done'),
]
