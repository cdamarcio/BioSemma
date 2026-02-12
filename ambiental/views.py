from django.contrib.auth import logout
from django.shortcuts import redirect

def encerrar_sessao(request):
    logout(request)
    return redirect('/admin/login/')