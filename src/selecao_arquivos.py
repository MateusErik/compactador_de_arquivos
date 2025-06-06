from rich.prompt import Prompt
from rich.console import Console
import os

console = Console()

def selecionar_arquivos():
    arquivos = []
    console.print("[bold cyan]Digite os caminhos dos arquivos que deseja compactar (digite 'fim' para terminar):[/]")
    while True:
        caminho = Prompt.ask("Arquivo")
        if caminho.lower() == "fim":
            break
        elif os.path.isfile(caminho):
            arquivos.append(caminho)
            console.print(f"[green]Adicionado:[/] {caminho}")
        else:
            console.print(f"[red]Arquivo não encontrado:[/] {caminho}")
    return arquivos
