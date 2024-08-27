# Hacker.mindset

1 - Definição do nome do arquivo:

nome_arquivo = "darkweb2017-top100.txt"

. DESCRIÇÃO: Este script defini uma variável denominada "darkweb2017-top100.txt".

2 - Estruturação da manipulação dos arquivos:

try:
    with open(nome_arquivo, 'r') as arquivo:
        # ...
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except IOError:
    print(f"Ocorreu um erro ao tentar ler o arquivo '{nome_arquivo}'.")

. DESCRIÇÃO: Esta estrutura tentará abrir o arquivo em evidência. Caso não existir o ('FileNotFoundError') ou haja algum erro em sua saída/entrada o script irá printar a mensagem de erro apropriada. exemplo ('I0Error').

3 - Abrindo e lendo o conteúdo do arquivo:

with open(nome_arquivo, 'r') as arquivo:
    # ...

. DESCRIÇÃO: Nesta linha ele abrirá o arquivo em modo de leitura ('r') e usará o 'with' para garantir que o arquivo esteja corretamente fechado após a leitura, mesmo ocorrendo durante a execução durante o processo.

4- Lendo & imprimindo a solicitação das 10 primeiras linhas (printando)

for i, linha in enumerate(arquivo):
    if i < 10:
        print(linha, end='')
    else:
        break

. DESCRIÇÃO: O 'for' percorre o loop em cada linha do arquivo aberto e a função 'enumerate' irá obter o índice de cada linha com o (i) e a linha em sí com o ('linha').
Cujo o mesmo se o índice for menor que '10' deverá ser printada a linha , caso não for o loop é brecado com o 'break' . No argumento "end='' " e no 'print' é utilizado para evitar a adição de uma nova linha extra, já que cada linha já finaliza com uma nova linha dentro do arquivo sendo usado o ('\n')


