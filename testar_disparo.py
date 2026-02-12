import os
import django
from datetime import date, timedelta

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from ambiental.models import Empresa, LicencaAmbiental
from ambiental.services import enviar_notificacoes_completas

def executar_teste():
    print("Iniciando teste de disparo...")
    
    # 1. Cria empresa de teste (se não existir)
    empresa, created = Empresa.objects.get_or_create(
        cnpj="00.000.000/0001-00",
        defaults={
            "nome_fantasia": "Empresa Teste Márcio",
            "email_contato": "seu-email@gmail.com", # <--- COLOQUE SEU EMAIL AQUI
            "whatsapp": "5594900000000"             # <--- COLOQUE SEU WHATSAPP AQUI
        }
    )

    # 2. Cria licença vencendo em exatos 30 dias
    data_vencimento_teste = date.today() + timedelta(days=30)
    
    LicencaAmbiental.objects.create(
        empresa=empresa,
        tipo_licenca="TESTE-PROJETO",
        data_emissao=date.today(),
        data_vencimento=data_vencimento_teste
    )

    print(f"✅ Licença de teste criada para: {data_vencimento_teste}")
    print("📧 Disparando notificações...")
    
    # 3. Chama a função de envio que criamos
    resultado = enviar_notificacoes_completas()
    print(f"🏁 Resultado: {resultado}")

if __name__ == "__main__":
    executar_teste()