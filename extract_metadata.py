import os
import re
import fitz
import json

def extract_data_from_pdfs(dir_path, ndir):
    """Extracts metadata from PDF files and saves the first page as a PNG image.

    Args:
        dir_path (str): Path of the directory where the PDF files are located.
        ndir (str): Path of the directory where the renamed PDF files will be saved.
    """
    ...
    books_data = []
    # Iterar sobre todos os arquivos no diretório
    for file in os.listdir(dir_path):
        # Verificar se o arquivo é um PDF
        if file.endswith('.pdf'):
            
            short_name = generate_short_name(file)

            # Abrir o arquivo PDF
            with fitz.open(os.path.join(dir_path, file)) as doc:
                
                image_file_name = short_name+'.png'


                # Obter a primeira página do PDF
                page = doc[0]
                # Verificar se a página possui uma imagem
                if page.get_images():
                    # Extrair os dados da imagem
                    pix = page.get_pixmap()
                    temp_file_path = os.path.join(dir_path, 'temp.png')
                    pix.save(temp_file_path)
                    with open(temp_file_path, 'rb') as image_file:
                        image_data = image_file.read()
                    os.remove(temp_file_path)
                    # Salvar a imagem em um arquivo com o nome do PDF e da página
                    with open(os.path.join('images/', image_file_name), 'wb') as image_file:
                        image_file.write(image_data)
                        print(f'Imagem {image_file_name} salva!')

                else:
                    # Converter a primeira página do PDF em imagem
                    pix = page.get_pixmap()
                    temp_file_path = os.path.join(ndir, 'temp.png')
                    pix.save(temp_file_path)
                    with open(temp_file_path, 'rb') as image_file:
                        image_data = image_file.read()
                    os.remove(temp_file_path)
                    # Salvar a imagem
                    with open(os.path.join('images/', image_file_name), 'wb') as image_file:
                        image_file.write(image_data)
                        print(f'Imagem {image_file_name} salva')
                        
                # Renomear arquivo PDF para o nome curto
                new_file_name = os.path.join(ndir, short_name+'.pdf')
                os.rename(os.path.join(dir_path, file), new_file_name)
                print(f'Arquivo <{file}> renomeado para <{new_file_name}>.')


                # Adicionar os dados do livro ao dicionário
                book_data = get_metadata(new_file_name)
                books_data.append(book_data)
                # Gerar nome curto para o arquivo
    # Salvar os dados dos livros em formato JSON
    with open('books_data.json', 'w') as json_file:
        json.dump(books_data, json_file)



def get_metadata(file_path):
    with fitz.open(file_path) as doc:
        metadata = {}
        #short_name
        metadata['short_name'] = os.path.basename(file_path)
        # título
        metadata['title'] = doc.metadata.get('title', 'Sem título')
        # autor
        metadata['author'] = doc.metadata.get('author', 'Autor desconhecido')
        # ISBN
        metadata['isbn'] = doc.metadata.get('isbn', 'Sem ISBN')
        # linguagem
        metadata['language'] = doc.metadata.get('language', 'Desconhecida')
        # editora
        metadata['publisher'] = doc.metadata.get('publisher', 'Desconhecida')
        # data de publicação
        metadata['creation_date'] = doc.metadata.get('creationDate', 'Desconhecida')
        # descrição
        metadata['description'] = doc.metadata.get('description', '')
        
        return metadata
    
    
def generate_short_name(file_name):
    # Remover os parênteses
    file_name = file_name.replace('(', ' ').replace(')', ' ')
    
    # Remover a extensão do arquivo
    file_name = os.path.splitext(file_name)[0]
    
    # Gerar o nome curto
       
    short_name = re.sub(r'\s*-\s*', '_', file_name[:30]).replace(' ', '_').replace('__', '_')
    
    return short_name
