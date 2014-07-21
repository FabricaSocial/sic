Sistema Integrado CIAS
===

Sistema interno da Fábrica Social, onde são realizadas as operações administrativas da fábrica.

Linguagens, Ferramentas e Frameworks
---------
* **Python v2.7** + **Django v1.6.5**
* Padrão MVT, implementado pelo **[Django](https://www.djangoproject.com/)**
* Não será utilizada nenhuma IDE específica e o uso de qualquer IDE é permitido.
* [Foundation Framework] (http://foundation.zurb.com/) - Para implementar a interface de usuário
* Banco de Dados [MySQL] (http://dev.mysql.com/downloads/mysql/)
* Deploy: [Apache2 + mod_wsgi] (https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/)

Etapas de Implementação
--------
O sistema será implementado por módulos:

###Lista Telefônica
Primeiro módulo a ser implementado. Consiste em um sistema de pesquisa de ramal por funcionário e/ou departamento.

####Etapas

1. Migrar banco de dados atual do SIC para MySQL.
2. Sincronizar Django com o banco já existente.
3. Definir classes modelo, para utilização do ORM do Django.
4. Implementar sistema de login.
5. Implementar módulo de lista telefônica.

**Tempo estimado:** 4 dias.
