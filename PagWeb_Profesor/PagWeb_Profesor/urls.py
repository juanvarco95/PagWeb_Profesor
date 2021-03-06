"""PagWeb_Profesor URL Configuration

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



from django.contrib import admin
from django.urls import path, include
from django.urls.converters import IntConverter


urlpatterns = [
    path('', include('gestionUsers.urls')),
    path('admin/', admin.site.urls),
    path('math_topics/', include('MathTopics.urls')),
    path('computer_topic/', include('ComputerTopic.urls')),
    path('teacher_topic/', include('TeacherTopic.urls')),
    path('Math_Spanish_Teacher', include('MathComputerSTeacher.urls'))
]
