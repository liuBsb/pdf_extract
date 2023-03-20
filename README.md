# Extrator de Dados de PDF

Este script em Python extrai metadados de arquivos PDF e salva a primeira página como uma imagem PNG.

## Como Usar

Para utilizar este script, siga as instruções abaixo:

1. Certifique-se de ter instalado as seguintes bibliotecas:
    - os
    - re
    - fitz
    - json

2. Faça o download deste repositório.

3. Na linha de comando, navegue até o diretório onde o script está localizado.

4. Execute o seguinte comando para extrair os dados dos arquivos PDF e salvar as imagens PNG:

```python extract_data_from_pdfs.py /caminho/do/diretorio/com/os/pdf /caminho/do/diretorio/de/destino```


Substitua `/caminho/do/diretorio/com/os/pdf` pelo caminho completo do diretório que contém os arquivos PDF que você deseja extrair dados e `/caminho/do/diretorio/de/destino` pelo caminho completo do diretório onde os arquivos PDF renomeados e as imagens PNG serão salvos.

5. Verifique se os dados dos livros foram salvos com sucesso no arquivo `books_data.json`.

## Função extract_data_from_pdfs

Esta função recebe dois argumentos: `dir_path` e `new_dir`.

- `dir_path`: Path do diretório onde os arquivos PDF que você deseja extrair dados estão localizados.
- `new_dir`: Path do diretório onde os arquivos PDF renomeados e as imagens PNG serão salvos.

```python
def extract_data_from_pdfs(dir_path, new_dir):
 """Extracts metadata from PDF files and saves the first page as a PNG image.

 Args:
     dir_path (str): Path of the directory where the PDF files are located.
     ndir (str): Path of the directory where the renamed PDF files will be saved.
 """
 ...
