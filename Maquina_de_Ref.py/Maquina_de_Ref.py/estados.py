from abc import ABC, abstractmethod
# Padrão: State

# State Pattern
class Estado(ABC):
    @abstractmethod
    def inserir_pagamento(self, maquina, valor):
        pass

    @abstractmethod
    def selecionar_bebida(self, maquina, tipo):
        pass

    @abstractmethod
    def entregar(self, maquina):
        pass


class SemMoeda(Estado):
    def inserir_pagamento(self, maquina, valor):
        maquina.valor_pago = valor
        print("✅ Pagamento recebido.")
        maquina.estado_atual = ComMoeda()

    def selecionar_bebida(self, maquina, tipo):
        print("❌ Insira o pagamento antes de selecionar a bebida.")

    def entregar(self, maquina):
        print("❌ Nenhum pagamento foi realizado ainda.")


class ComMoeda(Estado):
    def inserir_pagamento(self, maquina, valor):
        print("❌ Pagamento já foi realizado. Escolha a bebida.")

    def selecionar_bebida(self, maquina, tipo):
        maquina.tipo_bebida = tipo
        maquina.estado_atual = EntregandoProduto()

    def entregar(self, maquina):
        print("❌ Escolha a bebida antes de entregar.")


class EntregandoProduto(Estado):
    def inserir_pagamento(self, maquina, valor):
        print("❌ Já estamos processando o pedido.")

    def selecionar_bebida(self, maquina, tipo):
        print("❌ Bebida já foi selecionada.")

    def entregar(self, maquina):
        maquina.preparar_bebida()
        maquina.estado_atual = SemMoeda()


# Import circular safe — Colocamos aqui no final:
from estados import *
