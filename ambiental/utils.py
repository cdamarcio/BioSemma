import urllib.parse

def gerar_link_whatsapp(licenca):
    # O texto deve começar com """ e terminar com """
    texto = f"""*KM Projetos - Alerta Ambiental*

Olá, *{licenca.empresa.nome_fantasia}*!
Informamos que a sua licença *{licenca.tipo_licenca}* vence em *{licenca.data_vencimento.strftime('%d/%m/%Y')}*.

Podemos iniciar a renovação?
Atenciosamente, Eng. Márcio Rodrigues."""
    
    texto_url = urllib.parse.quote(texto)
    link = f"https://api.whatsapp.com/send?phone={licenca.empresa.whatsapp}&text={texto_url}"
    return link