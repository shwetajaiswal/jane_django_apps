from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice, Task
from django.http import Http404
from django.template import loader, RequestContext

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer


# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'latest_questions':latest_questions},)
    #output = ', ' .join([p.question_text for p in latest_questions])
    #return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("Question Detail View: %s" %question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    else:
        return HttpResponse("Question Detail View: %s" %question_id)

def results(request, question_id):
    return HttpResponse("Results Detail View: %s" %question_id)

def vote(request, question_id):
    return HttpResponse("Vote Detail View: %s" %question_id)


#@api_view(['GET', 'POST'])
#def task_list(request):
class TaskList(APIView):

    """
    List all tasks, or create a new task.
    """
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
