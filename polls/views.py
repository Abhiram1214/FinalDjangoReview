from django.shortcuts import render
from django.http import HttpResponse
from polls.forms import NewUserForm
from polls.models import Question, Choice
# Create your views here.

def index(request):
    return render(request,'polls/index.html')

def questions(request):
    questions_list = Question.objects.all()
    return render(request,'polls/questions.html',{'question_list':questions_list})

def choices(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
    return render(request, 'polls/choices.html',{'choices':choices})


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request,'polls/users.html',{'form':form})



