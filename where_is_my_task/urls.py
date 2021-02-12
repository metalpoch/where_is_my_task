"""where_is_my_task URL Configuration

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
from django.contrib import admin
from django.urls import path, include
# *********
from django.conf import settings
from django.conf.urls.static import static
# *********
from app.views import (home,
                       sign_up,
                       contact,
                       my_tasks,
                       task_delete,
                       task_management,
                       task_completed
                       )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # Sign-up Sign-in
    path('', include('django.contrib.auth.urls')),
    path('signup/', sign_up, name='sign_up'),

    # Task Management:
    path('task_management/', task_management, name='task_management'),
    path('task_delete/<id>/', task_delete, name='task_delete'),
    path('task_completed/<id>/', task_completed, name='task_completed'),

    path('mytasks/', my_tasks, name='my_tasks'),  # Show task from employee
    path('contact/', contact, name='contact')  # Contact page
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
