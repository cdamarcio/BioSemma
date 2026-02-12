@echo off
cd /d "G:\Meu Drive\1-Notebook\PROJETOS DE TI\SysAmbiental"
call venv\Scripts\activate
python manage.py notificar_clientes
pause