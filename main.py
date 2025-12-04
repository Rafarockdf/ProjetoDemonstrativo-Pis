from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
# Certifique-se de que estes arquivos existem no seu projeto
from schemas import Mensagem
import models
from database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuração para permitir que o React converse com o FastAPI
origins = [
    "http://localhost:3001", # Porta padrão do React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Rota POST corrigida para salvar no Banco (Baseado na Aula 6)
@app.post("/mensagens", status_code=status.HTTP_201_CREATED)
def criar_mensagem(nova_mensagem: Mensagem, db: Session = Depends(get_db)):
    # Cria o modelo do SQLAlchemy a partir do esquema Pydantic
    mensagem_criada = models.Model_Mensagem(**nova_mensagem.model_dump())
    
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    
    return mensagem_criada

# Rota GET corrigida (Seu foco principal)
@app.get("/mensagens", response_model=List[Mensagem], status_code=status.HTTP_200_OK)
def buscar_valores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Faz a query no banco com paginação (offset e limit)
    mensagens = db.query(models.Model_Mensagem).offset(skip).limit(limit).all()
    
    return mensagens


# No topo do arquivo main.py, adicione os novos imports:
# from schemas import Mensagem, Produto
# import models
'''
@app.post("/produtos", status_code=status.HTTP_201_CREATED)
def criar_produto(novo_produto: Produto, db: Session = Depends(get_db)):
    produto_criado = models.Model_Produto(**novo_produto.model_dump())
    db.add(produto_criado)
    db.commit()
    db.refresh(produto_criado)
    return produto_criado'''