from django.db import models
from .utils import gerar_link_whatsapp

class Empresa(models.Model):
    nome_fantasia = models.CharField("Nome Fantasia", max_length=200)
    cnpj = models.CharField("CNPJ", max_length=18, unique=True)
    email_contato = models.EmailField("E-mail de Contato")
    whatsapp = models.CharField("WhatsApp/Telefone", max_length=20)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome_fantasia

class LicencaAmbiental(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    tipo_licenca = models.CharField("Tipo de Licença", max_length=100)
    data_emissao = models.DateField("Data de Emissão")
    data_vencimento = models.DateField("Data de Vencimento")
    
    # Campos de controle de notificação
    notificado_30 = models.BooleanField("Aviso 30 Dias", default=False)
    notificado_20 = models.BooleanField("Aviso 20 Dias", default=False)
    notificado_10 = models.BooleanField("Aviso 10 Dias", default=False)
    notificado_5  = models.BooleanField("Aviso 5 Dias", default=False)
    notificado_3  = models.BooleanField("Aviso 3 Dias", default=False)
    notificado_0  = models.BooleanField("Aviso Vencimento", default=False)

    class Meta:
        verbose_name = "Licença Ambiental"
        verbose_name_plural = "Licenças Ambientais"

    def __str__(self):
        return f"{self.tipo_licenca} - {self.empresa.nome_fantasia}"

    def get_whatsapp_link(self):
        return gerar_link_whatsapp(self)

class DocumentoLicenca(models.Model):
    licenca = models.ForeignKey(LicencaAmbiental, related_name='documentos', on_delete=models.CASCADE)
    arquivo = models.FileField("Arquivo PDF", upload_to='licencas_pdfs/')
    data_upload = models.DateTimeField("Data do Upload", auto_now_add=True)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"