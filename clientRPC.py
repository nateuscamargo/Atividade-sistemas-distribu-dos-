import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("PYRO:obj_369e8b0f96954353a3b166bc579639db@localhost:53649")  # Substitua 'obj_369e8b0f96954353a3b166bc579639db@localhost:53649' pelo URI do servidor correto
    resultado_soma = calculadora.somar(85, 3)
    print("A soma é:", resultado_soma)

    resultado_subtracao = calculadora.subtrair(85, 3)
    print("A subtração é:", resultado_subtracao)

    resultado_multiplicacao = calculadora.multiplicar(85, 3)
    print("A multiplicação é:", resultado_multiplicacao)

if __name__ == "__main__":
    main()

