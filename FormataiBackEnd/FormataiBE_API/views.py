from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import api_view, throttle_classes ,permission_classes


@api_view(['GET','POST'])
def getpdf(request):
    
    if request.method == 'GET':
     ...

