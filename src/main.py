"""
Compactador e Descompactador de Arquivos
"""

import os
import zipfile
import pandas as pd
from rich.console import Console
from datetime import datetime

console = Console()

def compactar(pasta_entrada, arquivo_saida):
    with zipfile.ZipFile(arquivo_saida, 'w') as zipf:
        for pasta_atual, _, arquivos in os.walk(pasta_entrada):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_atual, arquivo)
                zipf.write(caminho_completo, os.path.relpath(caminho_completo, pasta_entrada))
    console.print(f"[green]Compactação concluída: {arquivo_saida}[/green]")

def descompactar(arquivo_zip, pasta_destino):
    with zipfile.ZipFile(arquivo_zip, 'r') as zipf:
        zipf.extractall(pasta_destino)
    console.print(f"[cyan]Arquivos extraídos para: {pasta_destino}[/cyan]")

if __name__ == "__main__":
    console.print("[bold]Compactador de Arquivos[/bold]")
    # Exemplo de uso:
    compactar("data/entrada", "data/saida/arquivos.zip")
    descompactar("data/saida/arquivos.zip", "data/saida/descompactado")
