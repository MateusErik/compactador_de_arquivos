"""
Compactador e Descompactador de Arquivos
"""

import os
import zipfile
import pandas as pd
from rich.console import Console
from rich.prompt import Prompt
from datetime import datetime
from selecao_arquivos import selecionar_arquivos
from remocao import remover_arquivo, listar_arquivos

console = Console()

def compactar_varios(arquivos, arquivo_saida):
    registros = []

    with zipfile.ZipFile(arquivo_saida, 'w') as zipf:
        for caminho in arquivos:
            if os.path.isfile(caminho):
                nome_arquivo = os.path.basename(caminho)
                zipf.write(caminho, nome_arquivo)

                tamanho = os.path.getsize(caminho)
                modificado = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime('%Y-%m-%d %H:%M:%S')

                registros.append({
                    "arquivo": nome_arquivo,
                    "tamanho (bytes)": tamanho,
                    "modificado em": modificado
                })

    os.makedirs("logs", exist_ok=True)
    df = pd.DataFrame(registros)
    df.to_csv("logs/relatorio_compactados.csv", index=False)

    console.print(f"[green]Compactação concluída: {arquivo_saida}[/green]")
    console.print(f"[yellow]Relatório salvo em: logs/relatorio_compactados.csv[/yellow]")

def descompactar(arquivo_zip, pasta_destino):
    registros = []

    with zipfile.ZipFile(arquivo_zip, 'r') as zipf:
        zipf.extractall(pasta_destino)
        for nome_arquivo in zipf.namelist():
            caminho_extraido = os.path.join(pasta_destino, nome_arquivo)
            if os.path.isfile(caminho_extraido):
                tamanho = os.path.getsize(caminho_extraido)
                agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                registros.append({
                    "arquivo": nome_arquivo,
                    "extraído para": caminho_extraido,
                    "tamanho (bytes)": tamanho,
                    "extraído em": agora
                })

    os.makedirs("logs", exist_ok=True)
    df = pd.DataFrame(registros)
    df.to_csv("logs/relatorio_descompactados.csv", index=False)

    console.print(f"[cyan]Arquivos extraídos para: {pasta_destino}[/cyan]")
    console.print(f"[yellow]Relatório salvo em: logs/relatorio_descompactados.csv[/yellow]")

if __name__ == "__main__":
    console.print("[bold blue]Compactador de Arquivos[/bold blue]")

    arquivos = selecionar_arquivos()

    while True:
        listar_arquivos(arquivos)
        opcao = Prompt.ask("Deseja remover algum arquivo da lista? (s/n)", default="n").lower()
        if opcao == "s":
            arquivos = remover_arquivo(arquivos)
        else:
            break

    if arquivos:
        arquivo_saida = "data/saida/arquivos.zip"
        os.makedirs("data/saida", exist_ok=True)

        compactar_varios(arquivos, arquivo_saida)
        descompactar(arquivo_saida, "data/saida/descompactado")
    else:
        console.print("[red]Nenhum arquivo foi selecionado para compactação.[/red]")

    # Perguntar se deseja limpar os arquivos compactados
    limpar = Prompt.ask("Quer limpar os arquivos compactados? (s/n)", default="n").lower()
    if limpar == "s":
        if os.path.exists("data/saida/arquivos.zip"):
            os.remove("data/saida/arquivos.zip")
            console.print("[green]Arquivo compactado removido com sucesso.[/green]")
        else:
            console.print("[red]Nenhum arquivo compactado encontrado para remover.[/red]")

    # Perguntar se deseja listar os arquivos do relatório
    listar = Prompt.ask("Quer listar os arquivos compactados? (s/n)", default="n").lower()
    if listar == "s":
        if os.path.exists("logs/relatorio_compactados.csv"):
            df = pd.read_csv("logs/relatorio_compactados.csv")
            console.print("[bold cyan]Arquivos compactados:[/bold cyan]")
            console.print(df.to_string(index=False))
        else:
            console.print("[red]Nenhum relatório de arquivos compactados encontrado.[/red]")
