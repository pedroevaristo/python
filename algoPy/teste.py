class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print(self.valor)

# Criando uma instância da classe
objeto = MinhaClasse(42)

# Chamando um método da instância
objeto.imprimir_valor()  # Isso é equivalente a MinhaClasse.imprimir_valor(objeto)
