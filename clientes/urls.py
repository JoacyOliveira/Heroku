from django.urls import path
from .views import lista_produtos, criar_produto, update, delete


urlpatterns = [
    path('list/', lista_produtos, name="list"),
    path('salvar/', criar_produto, name='salvar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
