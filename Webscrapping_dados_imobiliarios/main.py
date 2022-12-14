import locale
import bs4
import requests
import tabulate
from pandas import DataFrame

from modelos import trata_decimal, trata_porcentagem, FundoImobiliario, Estrategia

headers = {'User-Agent': 'Mozilla/5.0'}
resposta = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)
soup = bs4.BeautifulSoup(resposta.text, 'html.parser')
tabela = soup.find(id='tabelaResultado').find('thead').find_all('tr')
linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')
resultado = []
estrategia = Estrategia(
    cotacao_minimo=50.0,
    dividend_yield_minimo=5,
    p_vp_minimo=0.70,
    valor_mercado_minimo=200000,
    liquidez_minimo=50000,
    qto_imoveis_minimo=1,
    vacancia_media_maxima=10
)


for linha in linhas:
    dados_fundo = linha.find_all('td')
    codigo = dados_fundo[0].text
    segmento = dados_fundo[1].text
    cotacao = trata_decimal(dados_fundo[2].text)
    ffo_yield = trata_porcentagem(dados_fundo[3].text)
    dividend_yield = trata_porcentagem(dados_fundo[4].text)
    p_vp = trata_decimal(dados_fundo[5].text)
    valor_mercado = trata_decimal(dados_fundo[6].text)
    liquidez = trata_decimal(dados_fundo[7].text)
    qto_imoveis = trata_decimal(dados_fundo[8].text)
    preco_m2 = trata_decimal(dados_fundo[9].text)
    aluguel_m2 = trata_decimal(dados_fundo[10].text)
    cap_rate = trata_porcentagem(dados_fundo[11].text)
    vacancia_media = trata_porcentagem(dados_fundo[12].text)

    fundo_imobiliario = FundoImobiliario(
        codigo, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado,
        liquidez, qto_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia_media
    )

    if estrategia.aplica_estrategia(fundo_imobiliario):
        resultado.append(fundo_imobiliario)

print(f'foram encontrados {len(resultado)} resultados')

cabecalho = ['CODIGO', 'SEGMENTO', 'COTACAO ATUAL', 'DIVIDENDO YIELD']
tabela = []
for elemento  in resultado:
    tabela.append([
        elemento.codigo,
        elemento.segmento,
        locale.currency(elemento.cotacao),
        f'{locale.str(elemento.dividend_yield)} %'
    ])

    print(tabulate.tabulate(tabela, headers=cabecalho, showindex='always', tablefmt='fancy_grid'))
    tabelaxls = DataFrame(tabela, columns=cabecalho)
    print(tabelaxls)
    tabelaxls.to_excel('Webscrapping_dados_imobiliarios.xls')
