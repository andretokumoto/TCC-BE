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
    
    if request.method == 'POST' or request.method == 'GET':
        dados = request.data
        
        pdf_gerado = to_pdf(dados)

        if os.path.exists(pdf_gerado):

            arquivo = FileResponse(open(pdf_gerado, 'rb'), content_type='application/x-tex')
            arquivo['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_gerado)}"'

        return arquivo
        
    else:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
     
@api_view(['POST'])
def getLatex(request):
    
    if request.method == 'POST':
        
        dados = request.data
        tex_gerado = to_tex(dados)
        
        if os.path.exists(tex_gerado):

            arquivo = FileResponse(open(tex_gerado, 'rb'), content_type='application/x-tex')
            arquivo['Content-Disposition'] = f'attachment; filename="{os.path.basename(tex_gerado)}"'

            return arquivo
        
        else:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
