@echo off
echo -----------------------------------------------------
echo   CONFIGURANDO SYSAMBIENTAL
echo   Desenvolvedor: Marcio Rodrigues de Oliveira
echo -----------------------------------------------------

:: 1. Criando ambiente virtual (venv)
echo [1/4] Criando ambiente virtual Python...
python -m venv venv

:: 2. Ativando o ambiente e instalando dependencias
echo [2/4] Instalando bibliotecas (Django, Requests, etc)...
call venv\Scripts\activate
pip install -r requirements.txt

:: 3. Preparando o Banco de Dados
echo [3/4] Criando tabelas no banco de dados...
python manage.py makemigrations
python manage.py migrate

:: 4. Finalizacao
echo [4/4] Tudo pronto! 
echo.
echo Para rodar o sistema, use: 
echo 1. call venv\Scripts\activate
echo 2. python manage.py runserver
echo.
pause