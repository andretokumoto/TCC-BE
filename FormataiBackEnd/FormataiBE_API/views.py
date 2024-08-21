from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import api_view, throttle_classes ,permission_classes
from .templates.request_to_document import to_pdf, to_tex
from django.http import FileResponse
import os


@api_view(['GET','POST'])
def getpdf(request):
    
    if request.method == 'GET':
     ...
     
@api_view(['POST'])
def getLatex(request):
    
    if request.method == 'POST':
        
        dados = request.data
        tex_gerado = to_tex(dados)
        
        arquivo = FileResponse(open(tex_gerado, 'rb'), content_type='application/x-tex')
        arquivo['Content-Disposition'] = f'attachment; filename="{os.path.basename(tex_gerado)}"'
        return arquivo
