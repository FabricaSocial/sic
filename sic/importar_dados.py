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


def cria_funcionario(usuario, pessoa, dados):
    if Funcionario.objects.filter(pessoa=pessoa).count() == 0:
        funcionario = Funcionario()
        funcionario.pessoa = pessoa
        funcionario.usuario = usuario

        funcionario.departamento = obter_departamento(dados[1])
        ramal = obter_ramal(dados[2])

        if ramal is not None:
            funcionario.ramal = ramal

        funcionario.save()
    else:
        print 'Funcionário ' + pessoa.nome + ' já cadastrado.'


def cria_usuario(pessoa, dados):
    nome = gera_nome_de_usuario(pessoa.nome)

    if User.objects.filter(username=nome).count() == 0:
        user = User.objects.create_user(nome, password='12345678')
        user.save()
    else:
        print 'Usuário ' + nome + ' já cadastrado.'

    cria_funcionario(user, pessoa, dados)


def gera_nome_de_usuario(nome, codif='utf-8'):
    nome_split = nome.split(' ')
    nome = nome_split[0] + '.' + nome_split[-1]
    nome = normalize('NFKD', nome.decode(codif)).encode('ASCII', 'ignore')

    nome = nome.lower()
    return nome


def cria_pessoa(dados):
    if Pessoa.objects.filter(nome=dados[0]).count() == 0:
        print 'Cadastrando Pessoa: ' + dados[0]
        pessoa = Pessoa()
        pessoa.nome = dados[0]

        pessoa.save()
        cria_usuario(pessoa, dados)
    else:
        print 'Pessoa ' + dados[0] + ' já cadastrada.'


def importar_pessoas():
    with open('csvs/pessoas.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            cria_pessoa(row)


def importar_coordenadoria_adjunta():
    coordenadoria = Coordenadoria()
    coordenadoria.descricao = 'Coordenadoria de Integração das Ações Sociais'
    coordenadoria.abreviacao = 'CIAS'
    coordenadoria.save()

    with open('csvs/coordenadoria_adjunta.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            coord_count = CoordenadoriaAdjunta.objects.filter(
                abreviacao=row[1]).count()
            if coord_count == 0:
                print 'Cadastrando CoordenadoriaAdjunta: ' + row[0]

                coord_adjunta = CoordenadoriaAdjunta()
                coord_adjunta.descricao = row[0]
                coord_adjunta.abreviacao = row[1]
                coord_adjunta.coordenadoria = coordenadoria
                coord_adjunta.save()
            else:
                print 'CoordenadoriaAdjunta ' + row[0] + ' já cadastrada.'


def obter_coord_adjunta(abreviacao):
    coord_adjunta = CoordenadoriaAdjunta.objects.get(abreviacao=abreviacao)
    return coord_adjunta


def importar_departamentos():
    with open('csvs/departamentos.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            if Departamento.objects.filter(abreviacao=row[1]).count() == 0:
                print 'Cadastrando Departamento: ' + row[0]
                departamento = Departamento()
                departamento.descricao = row[0]
                departamento.abreviacao = row[1]
                departamento.coordenadoria_adjunta = obter_coord_adjunta(
                    row[2])

                if row[3] != '':
                    departamento.ramal_dpto = row[3]

                departamento.save()
            else:
                print 'Departamento ' + row[0] + ' já cadastrado.'


def obter_departamento(abreviacao):
    departamento = Departamento.objects.get(abreviacao=abreviacao)
    return departamento


def obter_ramal(ramal):
    try:
        ramal = Ramal.objects.get(ramal=ramal)
    except:
        ramal = None

    return ramal


def importar_ramal():
    with open('csvs/ramais.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            if Ramal.objects.filter(ramal=row[0]).count() == 0:
                print 'Cadastrando Ramal: ' + row[0]
                ramal = Ramal()
                ramal.ramal = row[0]
                ramal.departamento = obter_departamento(row[1])

                ramal.save()
            else:
                print 'Ramal ' + row[0] + ' já cadastrado.'

if __name__ == '__main__':
    importar_coordenadoria_adjunta()
    importar_departamentos()
    importar_ramal()
    importar_pessoas()
