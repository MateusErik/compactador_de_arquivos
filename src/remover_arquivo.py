def remover_arquivo(arquivos):
    """
    Permite ao usuário remover um arquivo da lista de arquivos.
    """
    if not arquivos:
        print("Nenhum arquivo para remover.")
        return arquivos
    print("Arquivos selecionados:")
    for idx, arquivo in enumerate(arquivos, 1):
        print(f"{idx}. {arquivo}")
    try:
        idx_remover = int(input("Digite o número do arquivo que deseja remover (ou '0' para cancelar): "))
        if idx_remover == 0:
            return arquivos
        if 1 <= idx_remover <= len(arquivos):
            removido = arquivos.pop(idx_remover - 1)
            print(f"Removido: {removido}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
    return arquivos

def listar_arquivos(arquivos):
    """
    Exibe a lista de arquivos selecionados.
    """
    if not arquivos:
        print("Nenhum arquivo selecionado.")
        return
    print("Arquivos selecionados:")
    for idx, arquivo in enumerate(arquivos, 1):
        print(f"{idx}. {arquivo}")