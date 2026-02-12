from django.contrib import admin
from django.urls import path
from ambiental import views

urlpatterns = [
    path('admin/logoff/', views.encerrar_sessao, name='logoff_custom'), # Rota nova
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('admin/')),
]