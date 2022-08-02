from django.shortcuts import render

# Create your views here.
def index(request):
    dados = {
    'nome_das_receitas': {
                        1: "Lasanha",
                        2: "Sopa de Legumes",
                        3: "Sorvete",
                        4: "Bolo de chocolate"
                        }
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')