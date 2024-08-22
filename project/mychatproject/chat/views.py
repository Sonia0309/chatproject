from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from chat.models import Message

def index(request):
    messages = Message.objects.all()
    return render(request, 'chat/index.html', {'messages': messages})
