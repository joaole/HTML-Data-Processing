import pandas as pd
from bs4 import BeautifulSoup
from hmtl_c import html_c

def html_to_dataframe(html_content):
    # Analisa o HTML com BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Cria uma lista vazia para armazenar os dados das linhas
    data = []

    # Encontra todas as linhas no corpo da tabela
    rows = soup.find_all('tr')

    # Itere por cada linha e extrai os dados
    for row in rows:
        columns = row.find_all('td')
        if len(columns) < 4:
            continue
        comprador = columns[1].text.strip()
        licitacao = columns[2].text.strip()
        descricao_tag = columns[3]
        descricao = descricao_tag.find('a').text.strip()
        
        # Extraindo outros detalhes da tag de descrição
        details = descricao_tag.find_all('b')
        modalidade = details[1].text.strip()
        n_edital = details[2].text.strip()
        n_processo = details[3].text.strip()

        # Adiciona os dados extraídos à lista
        data.append([comprador, licitacao, descricao, modalidade, n_edital, n_processo])

    # Cria um DataFrame
    df = pd.DataFrame(data, columns=["Comprador", "Licitação", "Descrição", "UF", "Modalidade", "N Edital"])

    return df
