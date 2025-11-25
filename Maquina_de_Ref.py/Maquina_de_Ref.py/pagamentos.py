from abc import ABC, abstractmethod
# Padrão: Strategy

# Strategy Pattern
class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass


class PagamentoMoeda(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"💰 Pagamento de R${valor:.2f} realizado em moedas.")


class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"📱 Pagamento de R${valor:.2f} realizado via PIX.")


class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"💳 Pagamento de R${valor:.2f} realizado no cartão.")
