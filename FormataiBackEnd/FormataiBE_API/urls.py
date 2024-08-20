from django.urls import path
from . import views


#rotas
urlpatterns = [
    path('get-pdf/',views.getpdf),#rota para gerar pdf
]