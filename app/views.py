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
