from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter()

class RequestCPF(BaseModel):
    pontuacao: str
    cpf_estado: Optional[str] = None

class RequestCNPJ(BaseModel):
    pontuacao: str

@router.post("/cpf", status_code=201)
def create_cpf(request: RequestCPF):
    form_data = {
        "acao": "gerar_cpf",
        "pontuacao": request.pontuacao if request.pontuacao else "N",
        "cpf_estado": request.cpf_estado if request.cpf_estado else "",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = httpx.post(
            "https://www.4devs.com.br/ferramentas_online.php",
            data=form_data,
            headers=headers,
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "CPF processed", "response": response.text}

@router.post("/cnpj", status_code=201)
def create_cnpj(request: RequestCNPJ):
    form_data = {
        "acao": "gerar_cnpj",
        "pontuacao": request.pontuacao if request.pontuacao else "N",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = httpx.post(
            "https://www.4devs.com.br/ferramentas_online.php",
            data=form_data,
            headers=headers,
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "CNPJ processed", "response": response.text}

@router.post("/cnh", status_code=201)
def create_cnpj():
    form_data = {
        "acao": "gerar_cnh",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = httpx.post(
            "https://www.4devs.com.br/ferramentas_online.php",
            data=form_data,
            headers=headers,
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "CNH processed", "response": response.text}