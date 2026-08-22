from typing import List

from src.database.conexao import conectar
from src.schemas.categoria import Categoria

def consultar_todos() -> List[Categoria]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, nome FROM categorias")
            registros = cursor.fetchall()

    categorias = []
    for registro in registros:
        categoria = Categoria(id=registro["id"], nome=registro["nome"])
        categorias.append(categoria)
    return categorias
