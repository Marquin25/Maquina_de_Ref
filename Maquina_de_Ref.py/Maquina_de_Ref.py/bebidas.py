from abc import ABC, abstractmethod
# Padrão: Factory Method

# Produto Abstrato
class Bebida(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def preco(self) -> float:
        pass


# Produtos Concretos
class CocaCola(Bebida):
    def preparar(self):
        print("🍶 Preparando uma Coca-Cola gelada...")

    def preco(self):
        return 5.00


class Guarana(Bebida):
    def preparar(self):
        print("🥤 Preparando um Guaraná refrescante...")

    def preco(self):
        return 4.50


class Fanta(Bebida):
    def preparar(self):
        print("🧃 Preparando uma Fanta sabor laranja...")

    def preco(self):
        return 4.00


# Fábrica (Factory Method)
class BebidaFactory:
    def criar_bebida(self, tipo: str) -> Bebida:
        tipo = tipo.lower()
        if tipo == "coca":
            return CocaCola()
        elif tipo == "guarana":
            return Guarana()
        elif tipo == "fanta":
            return Fanta()
        else:
            raise ValueError("Tipo de bebida desconhecido!")
