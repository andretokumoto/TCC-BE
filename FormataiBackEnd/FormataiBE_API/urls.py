from django.urls import path
from . import views


#rotas
urlpatterns = [
    path('get-pdf/',views.getpdf),
    path('get-latex/',views.getLatex),
]