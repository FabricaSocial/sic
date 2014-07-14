from django.contrib.auth.decorators import login_required
from modelos.funcionario import Departamento, Funcionario

@login_required(login_url='/login')
def listar_telefones(request):
	lista_departamentos = obter_lista_departamentos()

def obter_lista_departamentos():
	return Departamento.objects.all()

def obter_lista_funcionarios_por_departamento():
	pass

def obter_funcionarios_json(request):
	return
