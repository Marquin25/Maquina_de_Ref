# Singleton + Observer Pattern
# Padrões:
#   - Singleton: garante que só exista um Estoque na aplicação.
#   - Observer: permite que observadores (ex.: PainelEstoque) sejam notificados quando um produto zera no estoque.

class Estoque:
    _instancia = None
    _observadores = []

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._itens = {"coca": 5, "guarana": 5, "fanta": 5}
        return cls._instancia

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def notificar_observadores(self, bebida):
        for obs in self._observadores:
            obs.atualizar(bebida)

    def reduzir_estoque(self, bebida):
        if self._itens[bebida] > 0:
            self._itens[bebida] -= 1
            if self._itens[bebida] == 0:
                self.notificar_observadores(bebida)
        else:
            raise Exception(f"❌ {bebida} está esgotado!")

    def verificar(self, bebida):
        return self._itens.get(bebida, 0)

 
    def mostrar_estoque(self):
        print("\n Estoque atual:")
        for k, v in self._itens.items():
            print(f" - {k.capitalize()}: {v} unidades")


class PainelEstoque:
    def atualizar(self, bebida):
        print(f"⚠️  Alerta: {bebida.upper()} está esgotado no estoque!")



