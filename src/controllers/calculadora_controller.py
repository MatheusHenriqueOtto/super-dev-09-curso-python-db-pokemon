from fastapi import APIRouter


router = APIRouter()


@router.get("/mensagem")
def mensagem():
    """Rota para uma mensagem de boas vindas"""
    return {"mensagem": "Olá mundo"}

@router.get("calculadora/somar")
def somar(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {
        "resultado": soma
    }

@router.get("calculadora/imc")
def calcular_imc(peso: float, altura: float):
    imc = peso / altura**2

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25: 
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return {
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }

@router.get("/concatenar")
def cancatenar(nome: str, sobrenome: str):
    concatenado = f"{nome} {sobrenome}"

    return {
        "nome completo": concatenado
    }


@router.get("/calcular/desconto")
def calcular_desconto(preco: float, percentual: float):
    preco_desconto = preco * (percentual / 100)
    preco_final = preco - preco_desconto

    return {
        "preco": preco,
        "percentual": percentual,
        "preco_final": preco_final
    }


@router.get("/calcular/media")
def calcular_media(nota1: float, nota2: float, nota3: float, nota4: float):
    media = (nota1 + nota2 + nota3 + nota4) / 4

    return {
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "nota4": nota4,
        "media": media
    } 
