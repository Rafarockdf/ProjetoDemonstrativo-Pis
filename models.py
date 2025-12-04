from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Float
from sqlalchemy.sql import text
from database import Base


class Model_Mensagem(Base):
    __tablename__ = 'mensagem'
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    publicada = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class Model_Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String, nullable=False)  # Nome do produto
    preco = Column(Float, nullable=False)     # Preço
    site = Column(String, nullable=False)     # Fonte de onde veio o dado (Ex: "Amazon", "Mercado Livre")
