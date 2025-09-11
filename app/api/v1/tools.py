from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import httpx
import json
import os
from app.util.util import extrair_valores_inputs_bs4 as extract_values


JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), '../../../db/')

router = APIRouter()

class RequestCPF(BaseModel):
    pontuacao: str
    cpf_estado: Optional[str] = None

class RequestCNPJ(BaseModel):
    pontuacao: str

class RequestVeiculo(BaseModel):
    fipe_codigo_marca: Optional[str] = None
    estado: Optional[str] = None
    pontuacao: str

class RequestCertidao(BaseModel):
    tipo_certidao: Optional[str] = None
    pontuacao: str

@router.get("/modelos", status_code=200)
def get_modelos() -> Dict[Any, Any]:
    try:
        with open(JSON_FILE_PATH + 'modelos.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Modelos file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding JSON file")
    
@router.get("/tipos_certidao", status_code=200)
def get_tipos_certidao() -> Dict[Any, Any]:
    try:
        with open(JSON_FILE_PATH + 'tipos_certidao.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Tipos de certidão file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding JSON file")

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
def create_cnh():
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

@router.post("/renavam", status_code=201)
def create_renavam():
    form_data = {
        "acao": "gerar_renavam",
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
    
    return {"message": "RENAVAN processed", "response": response.text}

@router.post("/veiculo", status_code=201)
def create_veiculo(request: RequestVeiculo):
    form_data = {
        "acao": "gerar_veiculo",
        "pontuacao": request.pontuacao if request.pontuacao else "S",
        "estado": request.estado if request.estado else "",
        "fipe_codigo_marca": request.fipe_codigo_marca if request.fipe_codigo_marca else ""
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
        json = extract_values(response.text)
        print(response.text)
        print(json)
        response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "VEICULO processed", "response": json}

@router.post("/certidao", status_code=201)
def create_certidao(request: RequestCertidao):
    form_data = {
        "acao": "gerador_certidao",
        "pontuacao": request.pontuacao if request.pontuacao else "N",
        "tipo_certidao": request.tipo_certidao if request.tipo_certidao else "",
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

    return {"message": "CERTIDAO processed", "response": response.text}
