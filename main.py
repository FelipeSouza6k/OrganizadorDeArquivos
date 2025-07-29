import os
from tkinter.filedialog import askdirectory

# Importa o módulo 'os' que fornece funções para interagir com o sistema operacional, como manipular arquivos e diretórios.
# Importa 'askdirectory' do módulo 'tkinter.filedialog'. Essa função abre uma janela de diálogo para o usuário selecionar um diretório (pasta).

caminho = askdirectory(title = "Selecione uma pasta ")
# Usa 'askdirectory' para abrir uma janela onde o usuário pode escolher uma pasta.
# O título da janela será "Selecione uma pasta".
# O caminho completo da pasta selecionada é armazenado na variável 'caminho'.

print(caminho)
# Exibe no console (terminal) o caminho da pasta que foi selecionada pelo usuário.

listaArquivos = os.listdir(caminho)
# Usa 'os.listdir()' para obter uma lista de todos os arquivos e subdiretórios presentes na pasta selecionada ('caminho').
# Essa lista é armazenada na variável 'listaArquivos'.

locais = {
    "imagens": [".png",".jpg"],
    "planilhas" : [".xlsx"],
    "pdfs" : [".pdf"],
    "csv" : [".csv"]
}
# Cria um dicionário chamado 'locais'.
# Este dicionário mapeia nomes de pastas (chaves, por exemplo, "imagens") para listas de extensões de arquivo (valores, por exemplo, [".png", ".jpg"]).
# Ele define quais tipos de arquivos irão para quais pastas.

for arquivo in listaArquivos:
    # Inicia um loop que itera sobre cada item (arquivo ou subdiretório) na 'listaArquivos'.

    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    # Para cada 'arquivo' na lista:
    # Constrói o caminho completo do arquivo usando uma f-string: f"{caminho}/{arquivo}".
    # 'os.path.splitext()' divide o nome do arquivo em duas partes: o nome base (sem extensão) e a extensão.
    # Por exemplo, para "documento.pdf", 'nome' seria "documento" e 'extensao' seria ".pdf".

    for pasta in locais:
        # Inicia um loop interno que itera sobre cada chave (nome de pasta como "imagens", "planilhas", etc.) no dicionário 'locais'.

        if extensao in locais[pasta]:
            # Verifica se a 'extensao' do arquivo atual está presente na lista de extensões associadas à 'pasta' atual no dicionário 'locais'.
            # Por exemplo, se a extensão for ".png", ele verificará se ".png" está na lista 'locais["imagens"]'.

            if not os.path.exists(f"{caminho}/{pasta}"):
                # Se a extensão corresponder, verifica se a pasta de destino (por exemplo, "imagens") já existe dentro do 'caminho' selecionado.
                # 'os.path.exists()' retorna True se o caminho existir, False caso contrário.
                # 'not' inverte o resultado, então a condição é verdadeira se a pasta *não* existir.

                os.mkdir(f"{caminho}/{pasta}")
                # Se a pasta de destino não existir, 'os.mkdir()' cria essa nova pasta.

            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            # Finalmente, move o arquivo para a pasta de destino correspondente.
            # 'os.rename()' move (ou renomeia) um arquivo ou diretório de um local para outro.
            # O primeiro argumento é o caminho atual do arquivo e o segundo é o novo caminho, que inclui a pasta de destino.