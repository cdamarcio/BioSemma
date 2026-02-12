from django.core.mail import send_mail
from django.conf import settings
from .models import LicencaAmbiental
from datetime import date, timedelta

def enviar_alertas_vencimento():
    # Define o alvo: licenças que vencem daqui a exatos 30 dias
    data_alvo = date.today() + timedelta(days=30)
    licencas = LicencaAmbiental.objects.filter(data_vencimento=data_alvo, notificado_30_dias=False)
    
    sucesso = 0

    for licenca in licencas:
        assunto = f"⚠️ ALERTA: Vencimento de Licença Ambiental - {licenca.empresa.nome_fantasia}"
        
        mensagem = f"""
        Olá, equipe da {licenca.empresa.nome_fantasia},

        Este é um aviso automático do seu Sistema de Gestão Ambiental.
        
        Informamos que a sua licença ({licenca.tipo_licenca}) está próxima do vencimento:
        - Data de Vencimento: {licenca.data_vencimento.strftime('%d/%m/%Y')}
        - Prazo restante: 30 dias.

        Por favor, entre em contato para iniciarmos o processo de renovação e evitar multas ou interrupções nas atividades.

        Atenciosamente,
        Departamento de Engenharia Ambiental
        """
        
        destinatario = [licenca.empresa.email_contato]
        
        try:
            send_mail(
                assunto,
                mensagem,
                settings.EMAIL_HOST_USER,
                destinatario,
                fail_silently=False,
            )
            # Atualiza o banco para não enviar o e-mail novamente amanhã
            licenca.notificado_30_dias = True
            licenca.save()
            sucesso += 1
        except Exception as e:
            print(f"Erro ao enviar para {licenca.empresa.nome_fantasia}: {e}")

    return f"{sucesso} e-mails de alerta enviados com sucesso."