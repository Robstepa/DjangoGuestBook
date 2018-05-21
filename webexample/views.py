# Create your views here.
from django.shortcuts import render

from webexample.comment import Comment

comments = []


def index(request):
    if request.method == 'POST' and new_comment(request) != 0:
        comments.append(new_comment(request))
    return render(request, 'index.html', {'comments': comments})


def new_comment(request):
    if request.POST.get('name') == "" or request.POST.get('comment') == "":
        return 0
    return Comment(request.POST.get('name'), request.POST.get('comment'))
