# -*- coding: utf-8 -*-
import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sic.settings")

from unicodedata import normalize
from django.contrib.auth.models import User
from modelos.pessoa import Pessoa
from modelos.funcionario import Funcionario


def cria_funcionario(usuario, pessoa):
    funcionario = Funcionario()
    funcionario.pessoa = pessoa
    funcionario.usuario = usuario

    funcionario.save()


def cria_usuario(pessoa):
    nome = gera_nome_de_usuario(pessoa.nome)

    user = User.objects.create_user(nome, password='12345678')
    user.save()

    cria_funcionario(user, pessoa)


def gera_nome_de_usuario(nome, codif='utf-8'):
    nome_split = nome.split(' ')
    nome = nome_split[0] + '.' + nome_split[-1]
    nome = normalize('NFKD', nome.decode(codif)).encode('ASCII', 'ignore')

    nome = nome.lower()
    return nome


def cria_pessoa(nome):
    pessoa = Pessoa()
    pessoa.nome = nome

    pessoa.save()
    cria_usuario(pessoa)


def main_pessoas():
    with open('csvs/pessoas.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            nome = ', '.join(row)

            print 'Pessoa: ' + nome
            cria_pessoa(nome)

if __name__ == '__main__':
    print 'Cadastro de Pessoa, Usuario e Funcionario'
    # main_pessoas()
    print gera_nome_de_usuario("Nome com Ãcento")
