import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
def trata_porcentagem(porcentagem_str):
    return locale.atof(porcentagem_str.split('%')[0])


def trata_decimal(decimal_str):
    return locale.atof(decimal_str)


class FundoImobiliario:
    def __init__(self, codigo, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado,
                 liquidez, qto_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia_media):
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao = cotacao
        self.ffo_yield = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qto_imoveis = qto_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia_media = vacancia_media

class Estrategia:
    def __init__(self, segmento='', cotacao_minimo=0 , ffo_yield_minimo=0, dividend_yield_minimo=0,
                 p_vp_minimo=0, valor_mercado_minimo=0, liquidez_minimo=0, qto_imoveis_minimo=0, preco_m2_minimo=0,
                 aluguel_m2_minimo=0, cap_rate_minimo=0, vacancia_media_maxima=0):
        self.segmento = segmento
        self.cotacao_minimo = cotacao_minimo
        self.ffo_yield_minimo = ffo_yield_minimo
        self.dividend_yield_minimo = dividend_yield_minimo
        self.p_vp_minimo = p_vp_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minimo = liquidez_minimo
        self.qto_imoveis_minimo = qto_imoveis_minimo
        self.preco_m2_minimo = preco_m2_minimo
        self.aluguel_m2_minimo = aluguel_m2_minimo
        self.cap_rate_minimo = cap_rate_minimo
        self.vacancia_media_maxima = vacancia_media_maxima


    def aplica_estrategia(self, fundo: FundoImobiliario):
        if self.segmento != '':
            if fundo.segmento != self.segmento:
                return False

        if fundo.cotacao < self.cotacao_minimo \
                or fundo.ffo_yield < self.ffo_yield_minimo \
                or fundo.dividend_yield < self.dividend_yield_minimo \
                or fundo.p_vp < self.p_vp_minimo \
                or fundo.valor_mercado < self.valor_mercado_minimo \
                or fundo.liquidez < self.liquidez_minimo \
                or fundo.qto_imoveis < self.qto_imoveis_minimo \
                or fundo.preco_m2< self.preco_m2_minimo \
                or fundo.aluguel_m2 < self.aluguel_m2_minimo \
                or fundo.cap_rate < self.cap_rate_minimo \
                or fundo.vacancia_media > self.vacancia_media_maxima:
            return False
        else:
            return True
