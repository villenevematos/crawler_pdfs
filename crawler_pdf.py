import requests
from scraper_simples import download_file
from bs4 import BeautifulSoup

# Função para buscar links de arquivos PDF em uma página web
def fetch_pdf_links(url, timeout=10):
    """
    Busca links de arquivos PDF na página fornecida.

    Retorna uma lista de URLs de arquivos PDF encontrados na página.
    Define o cabeçalho da requisição para simular um navegador real.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/'  # Incompleto, mas suficiente para simular um navegador
    }

    try:
        # Faz a requisição HTTP para a URL fornecida
        resp = requests.get(url, headers=headers, timeout=timeout)
        # Lança exceção se houver erro na resposta
        resp.raise_for_status()

        # Cria o objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(resp.content, 'html.parser')

        # Lista para armazenar os links de PDF encontrados
        pdf_links = []

        # Encontra todos os elementos <a> com atributo href
        links = soup.find_all('a', href=True)

        # Itera sobre os links encontrados
        for link in links:
            # Verifica se o href contém "/pdf", indicando um possível link para PDF
            if '/pdf' in link['href'].lower():
                pdf_links.append(link['href'])  # Adiciona à lista

        return pdf_links  # Retorna a lista de links encontrados

    except requests.RequestException as e:
        # Em caso de erro na requisição, imprime a mensagem e retorna lista vazia
        print(f"Erro na requisição: {e}")
        return []

# Função para baixar um arquivo de uma URL e salvar localmente
def download_file(url, save_path):
    """Baixa um arquivo da URL fornecida e salva no caminho especificado."""
    try:
        # Faz a requisição HTTP para a URL do arquivo
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            # Abre (ou cria) o arquivo no caminho especificado em modo binário
            with open(save_path, 'wb') as file:
                file.write(response.content)  # Escreve o conteúdo no arquivo
            print(f"Arquivo baixado com sucesso: {save_path}")
        else:
            # Caso o status não seja 200, exibe mensagem de erro
            print(f"Falha ao baixar o arquivo. Código de status: {response.status_code}")
    except Exception as e:
        # Captura e exibe qualquer erro ocorrido durante o processo
        print(f"Erro: {e}")

# URL da página de busca do arXiv com resultados para "python"
url = "https://arxiv.org/search/?query=python&searchtype=all&abstracts=show&order=-announced_date_first&size=50&start=0"

# Chama a função para buscar os links de PDF na página
lista_pdfs_links = fetch_pdf_links(url)

# Itera sobre cada link de PDF encontrado
for link_pdf in lista_pdfs_links:
    # Define o caminho onde o arquivo será salvo localmente
    # Usa o nome do arquivo extraído da URL e adiciona a extensão .pdf
    caminho_salvar = 'C:/Users/CASA/Downloads/documentos/.pdf/arquivos_pdfs_baixados/' + link_pdf.split('/')[-1] + '.pdf'

    # Chama a função para baixar o arquivo e salvar no caminho especificado
    download_file(link_pdf, caminho_salvar)
