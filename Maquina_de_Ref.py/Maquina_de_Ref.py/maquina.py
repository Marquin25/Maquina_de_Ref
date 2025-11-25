from bebidas import BebidaFactory
from pagamentos import PagamentoMoeda, PagamentoPix, PagamentoCartao
from estoque import Estoque, PainelEstoque
from estados import SemMoeda

class MaquinaDeRefrigerante:
    def __init__(self):
        self.factory = BebidaFactory()
        self.estoque = Estoque()
        self.estado_atual = SemMoeda()
        self.valor_pago = 0
        self.tipo_bebida = None

        painel = PainelEstoque()
        self.estoque.adicionar_observador(painel)

    def inserir_pagamento(self, estrategia_pagamento, valor):
        estrategia_pagamento.pagar(valor)
        self.estado_atual.inserir_pagamento(self, valor)

    def selecionar_bebida(self, tipo):
        self.estado_atual.selecionar_bebida(self, tipo)

    def entregar(self):
        self.estado_atual.entregar(self)

    def preparar_bebida(self):
        bebida = self.factory.criar_bebida(self.tipo_bebida)
        preco = bebida.preco()

        # 1) Verifica se o valor é insuficiente
        if self.valor_pago < preco:
            print(f"❌ Valor insuficiente! A {self.tipo_bebida} custa R${preco:.2f}")
            return

        # 2) Verifica estoque antes de seguir
        if self.estoque.verificar(self.tipo_bebida) == 0:
            print(f"❌ {self.tipo_bebida} está fora de estoque.")
            return

        # 3) Calcula troco, se houver
        if self.valor_pago > preco:
            troco = self.valor_pago - preco
            print(f"💸 Pagamento aceito. Seu troco é de R${troco:.2f}.")
        else:
            print("✅ Pagamento no valor exato aceito.")

        # 4) Prepara e entrega a bebida
        bebida.preparar()
        self.estoque.reduzir_estoque(self.tipo_bebida)
        print("✅ Produto entregue! Aproveite sua bebida! 🍹")

        # (Opcional) zera o valor pago para a próxima operação
        self.valor_pago = 0
        self.tipo_bebida = None
