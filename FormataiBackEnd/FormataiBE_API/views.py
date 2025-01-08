from django.http import FileResponse, HttpResponse
from rest_framework.response import Response
import os
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .templates.request_to_document import to_pdf, to_tex

@csrf_exempt
@api_view(['POST'])
def getpdf(request):
    """
    Gera um arquivo PDF com base nos dados fornecidos na requisição e retorna o arquivo para download.
    """
    try:
       
        dados = request.data

        # Gera o arquivo PDF
        pdf_gerado = to_pdf(dados)

        if os.path.exists(pdf_gerado):
            # Retorna o arquivo PDF como resposta para download
            
            response = FileResponse(open(pdf_gerado, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_gerado)}"'
            os.remove(pdf_gerado)

            return response

        return Response({"error": "O arquivo PDF não foi encontrado."}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": f"Erro ao gerar o PDF: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
def getLatex(request):
    """
    Gera um arquivo LaTeX (.tex) com base nos dados fornecidos na requisição e retorna o arquivo para download.
    """
    try:
        
        dados = request.data

        # Gera o arquivo LaTeX
        tex_gerado = to_tex(dados)

        if os.path.exists(tex_gerado):
            # Retorna o arquivo LaTeX como resposta para download
            response = FileResponse(open(tex_gerado, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(tex_gerado)}"'

            #remove arquivo temporario
            os.remove(tex_gerado)

            return response

        return Response({"error": "O arquivo LaTeX não foi encontrado."}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": f"Erro ao gerar o LaTeX: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
