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
def listar_tarefas():
    return tarefas

@app.get("/tarefas/{id}")
def listar_uma_tarefa(id: str):
    for tarefa in tarefas:
        if tarefa.id ==id:
            return tarefa
    
    return {"erro": "Tarefa não localizada"}

@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):   
    tarefa.id =str(uuid4())
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/{id}")
def deletar_datefa(id: str):
    for index, tarefa in enumerate(tarefas):
        if(tarefa.id == id):
            posicao = index
            tarefas.pop(posicao)
            return "Tarefa deletada!"
 
    return{"erro": "Tarefa não encontrada"}

