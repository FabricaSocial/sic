Configuração de Ambiente
===========

Django
-----

1. Instalar Python e Pip

  * sudo apt-get install python
  * sudo apt-get install python-pip
      
2. Instalar dependências
      
  * sudo apt-get install python-dev

3. Instalar Django

  * sudo pip install django

4. Instalar dependencias do Projeto

  * sudo pip install -r requeriments.txt


Servidor de Desenvolvimento
-----------

Para iniciar o servidor de desenvolvimento, executar o comando abaixo, dentro da pasta raíz do projeto:

  * python manage.py runserver


Sincronizar Banco de Dados
----------
Para sincronizar o banco de dados, basta executar o comando abaixo, dentro da pasta raíz do projeto:

  * python manage.py syncdb

Desta forma, as tabelas pardões do django serão criadas. Para sincronizar as tabelas das aplicações dentro do projeto, executar:

  * python manage.py migrate nome\_da\_aplicacao
