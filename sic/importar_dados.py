# -*- coding: utf-8 -*-
import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sic.settings")

from unicodedata import normalize
from django.contrib.auth.models import User
from modelos.pessoa import Pessoa
from modelos.funcionario import Funcionario
from modelos.administrativo import CoordenadoriaAdjunta, \
    Coordenadoria, Departamento, Ramal


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


def importar_pessoas():
    with open('csvs/pessoas.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            nome = ', '.join(row)

            print 'Cadastrando Pessoa: ' + nome
            cria_pessoa(nome)


def importar_coordenadoria_adjunta():
    coordenadoria = Coordenadoria()
    coordenadoria.descricao = 'Coordenadoria de Integração das Ações Sociais'
    coordenadoria.abreviacao = 'CIAS'
    coordenadoria.save()

    with open('csvs/coordenadoria_adjunta.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            print 'Cadastrando CoordenadoriaAdjunta: ' + row[0]

            coord_adjunta = CoordenadoriaAdjunta()
            coord_adjunta.descricao = row[0]
            coord_adjunta.abreviacao = row[1]
            coord_adjunta.coordenadoria = coordenadoria
            coord_adjunta.save()


def obter_coordenadoria_adjunta(abreviacao):
    coord_adjunta = CoordenadoriaAdjunta.objects.get(abreviacao=abreviacao)
    return coord_adjunta


def importar_departamentos():
    with open('csvs/departamentos.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            print 'Cadastrando Departamento: ' + row[0]
            departamento = Departamento()
            departamento.descricao = row[0]
            departamento.abreviacao = row[1]
            departamento.coordenadoria_adjunta = obter_coordenadoria_adjunta(
                row[2])
            departamento.ramal_dpto = row[3]
            departamento.save()


def obter_departamento(abreviacao):
    departamento = Departamento.objects.get(abreviacao=abreviacao)
    return departamento


def importar_ramal():
    with open('csvs/ramais.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            print 'Cadastrando Ramal: ' + row[0]
            ramal = Ramal()
            ramal.ramal = row[0]
            ramal.departamento = obter_departamento(row[1])

            ramal.save()

if __name__ == '__main__':
    importar_coordenadoria_adjunta()
    importar_departamentos()
    importar_ramal()
    importar_pessoas()
