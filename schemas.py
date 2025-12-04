from pydantic import BaseModel

__all__ = ["Mensagem", "Produto"]


class Mensagem(BaseModel):
    titulo: str
    conteudo: str
    publicada: bool = True


class Produto(BaseModel):
    produto: str
    preco: float
    site: str