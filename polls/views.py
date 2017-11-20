from django.shortcuts import render
from django.http import HttpResponse
from polls.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'polls/index.html')

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request,'polls/users.html',{'form':form})



