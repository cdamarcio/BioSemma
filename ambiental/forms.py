from django import forms
from .models import LicencaAmbiental

class LicencaForm(forms.ModelForm):
    # Definimos o campo de arquivo
    arquivos = forms.FileField(required=False, label="Anexar PDFs da Licença")

    class Meta:
        model = LicencaAmbiental
        fields = ['empresa', 'tipo_licenca', 'data_emissao', 'data_vencimento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionamos o atributo 'multiple' manualmente para burlar a validação rígida
        self.fields['arquivos'].widget.attrs.update({'multiple': True})