from rich.prompt import Prompt
from rich.console import Console
import os

console = Console()

def selecionar_arquivos():
    console.print("[bold cyan]Como deseja selecionar os arquivos para compactação?[/]")
    console.print("1 - Digitar manualmente os caminhos dos arquivos")
    console.print("2 - Selecionar todos os arquivos de uma pasta")

    opcao = Prompt.ask("Escolha uma opção", choices=["1", "2"], default="1")

    arquivos = []

    if opcao == "1":
        console.print("[bold cyan]Digite os caminhos dos arquivos (digite 'fim' para encerrar):[/]")
        while True:
            caminho = Prompt.ask("Arquivo")
            if caminho.lower() == "fim":
                break
            elif os.path.isfile(caminho):
                arquivos.append(caminho)
                console.print(f"[green]Adicionado:[/] {caminho}")
            else:
                console.print(f"[red]Arquivo não encontrado:[/] {caminho}")

    elif opcao == "2":
        pasta = Prompt.ask("Digite o caminho da pasta")
        if os.path.isdir(pasta):
            arquivos = [
                os.path.join(pasta, f)
                for f in os.listdir(pasta)
                if os.path.isfile(os.path.join(pasta, f))
            ]
            console.print(f"[green]{len(arquivos)} arquivos encontrados na pasta {pasta}[/]")
        else:
            console.print(f"[red]Pasta não encontrada:[/] {pasta}")

    return arquivos