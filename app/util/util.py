import re
import json
from html.parser import HTMLParser

def extrair_valores_inputs_bs4(html_string):
    """
    Extrai valores usando BeautifulSoup (requer: pip install beautifulsoup4)
    """
    try:
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(html_string, 'html.parser')
        inputs = soup.find_all('input', type='text')
        
        resultado = {}
        for input_tag in inputs:
            # Prioriza id, depois name
            identifier = input_tag.get('id') or input_tag.get('name')
            value = input_tag.get('value', '')
            
            if identifier:
                resultado[identifier] = value
        
        #return json.dumps(resultado, ensure_ascii=False)
        return resultado
    
    except ImportError:
        return "Erro: BeautifulSoup4 não está instalado. Use: pip install beautifulsoup4"