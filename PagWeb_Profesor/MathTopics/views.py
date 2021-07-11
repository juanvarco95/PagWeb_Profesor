from django.shortcuts import render

def math_topic(request):
    return render(request, 'MathTopics/Math.html')