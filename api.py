from typing import List, Optional
from datetime import date, datetime
from uuid import uuid4


from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Tarefa(BaseModel):
    name: str
    descricao: str
    id: Optional [str]
    data_de_criacao: str
    data_limite: str
    

tarefas: List = []


@app.get("/tarefas")
async def listar_tarefas():
    return tarefas

@app.get("/tarefas/{id}")
async def listar_uma_tarefa(id: str):
    for tarefa in tarefas:
        if tarefa.id ==id:
            return tarefa
    
    return {"erro": "Tarefa não localizada"}

@app.post("/tarefas")
async def criar_tarefa(tarefa: Tarefa):   
    tarefa.id =str(uuid4())
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/{id}")
async def deletar_datefa(id: str):
    for index, tarefa in enumerate(tarefas):
        if(tarefa.id == id):
            tarefas.pop(index)
            return "Tarefa deletada!"
 
    return{"erro": "Tarefa não encontrada"}

@app.put("/tarefas/{id}")
async def atualizar_tarefa(id: str, nome: Optional[str], descricao: Optional[str], data_criacao: Optional[str], data_limite: Optional[str]):
    tarefa_atualizada = {
        "name": nome,
        "descricao": descricao,
        "id": id,
        "data_de_criacao": data_criacao,
        "data_limite": data_limite
    }
    for index, tarefa in enumerate(tarefas):
        if(tarefa.id == id):
            tarefas[index] = tarefa_atualizada
            return "Atualizada"
    return {"erro": "tarefa não encontrada"}
