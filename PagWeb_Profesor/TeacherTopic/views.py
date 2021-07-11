from django.shortcuts import render

def teacher(request):
    return render(request, 'TeacherTopic/Teacher.html')