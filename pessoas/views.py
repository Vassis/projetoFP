from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from pessoas.models import Pessoa

def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
    pessoas = Pessoa.objects.all()[0:10]

    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
    return render(request, 'pessoas/formPessoas.html')

def pessoaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            pessoa = Pessoa.objects.get(pk=codigo)
        except:
            pessoa = Pessoa()

        pessoa.nome = request.POST.get('nome', '').upper()
        pessoa.email = request.POST.get('email', '').upper()
        pessoa.telefone = request.POST.get('telefone', '(00) 0-0000-0000').upper()
        pessoa.logradouro = request.POST.get('logradouro', '').upper()

        pessoa.save()
    return HttpResponseRedirect('/pessoas/')

def pessoaPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                pessoas = Pessoa.objects.all()
            else: 
                pessoas = Pessoa.objects.filter(
                    (Q(nome__contains=textoBusca) |  
                    Q(email__contains=textoBusca) | 
                    Q(telefone__contains=textoBusca) | 
                    Q(logradouro__contains=textoBusca))).order_by('-nome')
        except:
            pessoas = []

        return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas, 'textoBusca': textoBusca})

def pessoaEditar(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/pessoas/')

    return render(request, 'pessoas/formPessoas.html', {'pessoa': pessoa})

def pessoaExcluir(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect('/pessoas/')
    except:
        return HttpResponseRedirect('/pessoas/')




    




