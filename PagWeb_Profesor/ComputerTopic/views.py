from django.shortcuts import render

def computer_topic(request):
    return render(request, 'ComputerTopic/Computer.html')
