# Organizador de Arquivos Simples

Este é um script Python simples que ajuda a organizar automaticamente os arquivos em uma pasta selecionada, movendo-os para subpastas baseadas em suas extensões.

## Funcionalidades

* **Seleção de Pasta:** Permite ao usuário selecionar graficamente a pasta que deseja organizar.
* **Organização por Tipo:** Move arquivos de imagem, planilhas, PDFs e CSVs para suas respectivas subpastas (`imagens`, `planilhas`, `pdfs`, `csv`).
* **Criação de Pastas:** Se as pastas de destino não existirem, o script as criará automaticamente.

## Como Usar

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado em seu sistema. Este script utiliza a biblioteca `tkinter`, que geralmente já vem com a instalação padrão do Python.
2.  **Baixe o Script:** Salve o código fornecido em um arquivo chamado `organizador.py` (ou qualquer outro nome com a extensão `.py`).
3.  **Execute o Script:** Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute-o com o seguinte comando:

    ```bash
    python organizador.py
    ```

4.  **Selecione a Pasta:** Uma janela de diálogo aparecerá. Navegue e selecione a pasta que você deseja organizar.
5.  **Organização Automática:** O script então processará os arquivos dentro da pasta selecionada e os moverá para as subpastas apropriadas.

## Tipos de Arquivos Suportados

Atualmente, o script organiza os seguintes tipos de arquivos:

* **Imagens:** `.png`, `.jpg`
* **Planilhas:** `.xlsx`
* **PDFs:** `.pdf`
* **CSVs:** `.csv`

## Personalização (Opcional)

Você pode facilmente adicionar ou modificar os tipos de arquivos e suas pastas de destino editando o dicionário `locais` no código:

```python
locais = {
    "imagens": [".png",".jpg"],
    "planilhas" : [".xlsx"],
    "pdfs" : [".pdf"],
    "csv" : [".csv"],
    # Exemplo: Para adicionar arquivos de texto para uma pasta "documentos"
    # "documentos": [".txt", ".doc", ".docx"]
}