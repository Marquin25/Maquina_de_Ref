from maquina import MaquinaDeRefrigerante
from pagamentos import PagamentoMoeda, PagamentoPix, PagamentoCartao

def escolher_pagamento():
    print("\n💳 Escolha o método de pagamento:")
    print("1. Moedas")
    print("2. PIX")
    print("3. Cartão")

    opcao = input("➡️  Opção: ").strip()
    if opcao == "1":
        return PagamentoMoeda()
    elif opcao == "2":
        return PagamentoPix()
    elif opcao == "3":
        return PagamentoCartao()
    else:
        print("❌ Opção inválida! Pagamento em moedas selecionado por padrão.")
        return PagamentoMoeda()

def main():
    maquina = MaquinaDeRefrigerante()

    while True:
        print("\n=== 🥤 MÁQUINA DE REFRIGERANTE ===")
        maquina.estoque.mostrar_estoque()
        print("\nEscolha sua bebida:")
        print("1. Coca-Cola (R$5.00)")
        print("2. Guaraná (R$4.50)")
        print("3. Fanta (R$4.00)")
        print("0. Sair")

        escolha = input("➡️  Opção: ").strip()
        if escolha == "0":
            print("\n👋 Encerrando o programa. Até mais!")
            break

        bebidas_opcoes = {"1": "coca", "2": "guarana", "3": "fanta"}
        tipo_bebida = bebidas_opcoes.get(escolha)

        if not tipo_bebida:
            print("❌ Opção inválida, tente novamente.")
            continue

        pagamento = escolher_pagamento()

        try:
            valor = float(input("💵 Insira o valor pago: R$").replace(",", "."))
        except ValueError:
            print("❌ Valor inválido. Tente novamente.")
            continue

        # Fluxo da máquina
        maquina.inserir_pagamento(pagamento, valor)
        maquina.selecionar_bebida(tipo_bebida)
        maquina.entregar()

if __name__ == "__main__":
    main()
