from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_register(request):
    if request.method=='POST':
        # data=JSONParser.parse(request.POST)
        # data_recieved=JSONParser.parse(request)
        data_recieved=JSONParser().parse(request)
        serialized_data=UserSerializer(data=data_recieved)
        if serialized_data.is_valid():
            serialized_data.save()
            # return HttpResponse("done")
            return HttpResponse("<html><body>done</body></html>")
        else:
            return HttpResponse("<html><body>error</body></html>")
    else:
        return HttpResponse("welcome user")   


from .serializers import ques_add_serializer

@csrf_exempt
def ques_add(request):
    if request.method=='POST':
        data_received=JSONParser().parse(request)
        serialized_data=ques_add_serializer(data=data_received)
        if serialized_data.is_valid():
            serialized_data.save(author=request.user)
            # return HttpResponse("<html><body>done</body></html>")
            return HttpResponse("<h1>Done</h1>")
        else:
            # return HttpResponse("<html><body>error</body></html>")
            # return HttpResponse("eone")
            # return HttpResponse(serialized_data._errors)
            return HttpResponse(serialized_data.error_messages)
            
    else:
        # return HttpResponse("<html><body>helo</body></html>")
        return HttpResponse("<h1>Helo</h1>")