from django.contrib.admin import AdminSite
from .models import LicencaAmbiental
from django.utils import timezone
from datetime import timedelta

class KMProjetosAdminSite(AdminSite):
    site_header = "KM Projetos - Gestão Ambiental"
    site_title = "Painel Eng. Márcio"
    index_title = "Indicadores de Licenciamento"

    def index(self, request, extra_context=None):
        hoje = timezone.now().date()
        # Dados para o Dashboard dentro do Admin
        extra_context = extra_context or {}
        extra_context['total'] = LicencaAmbiental.objects.count()
        extra_context['alerta'] = LicencaAmbiental.objects.filter(
            data_vencimento__lte=hoje + timedelta(days=30), 
            data_vencimento__gte=hoje
        ).count()
        extra_context['vencidas'] = LicencaAmbiental.objects.filter(data_vencimento__lt=hoje).count()
        
        return super().index(request, extra_context)

admin_site = KMProjetosAdminSite(name='myadmin')