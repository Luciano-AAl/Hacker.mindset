# Nome do arquivo a ser lido
nome_arquivo = "darkweb2017-top100.txt"

# Abrir e ler o arquivo alvo
try:
    # Tenta abrir o arquivo em modo de leitura ('r')
    with open(nome_arquivo, 'r') as arquivo:
        # Lê somente as 10 primeiras linhas do arquivo
        for i, linha in enumerate(arquivo):
            if i < 10:
                print(linha, end='')  # Imprime a linha atual sem adicionar nova linha
            else:
                break  # Sai do loop após a décima linha
except FileNotFoundError:
    # Caso o arquivo não seja encontrado, imprime uma mensagem de erro
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except IOError:
    # Caso ocorra um erro de entrada/saída, imprime uma mensagem de erro
    print(f"Ocorreu um erro ao tentar ler o arquivo '{nome_arquivo}'.")
