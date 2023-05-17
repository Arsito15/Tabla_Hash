def tokenize(code):
    tokens = []
    lines = code.split('\n')
    for row, line in enumerate(lines):
        tokens.extend(line.split())
    return tokens

def hash_tokens(tokens):
    hash_table = {}
    row = 0
    col = 0
    for token in tokens:
        key = f'{row},{col}'
        hash_table[key] = token
        col += 1
        if col >= len(tokens):
            col = 0
            row += 1
    return hash_table


def search_variable(hash_table, query):
    results = []
    for key, value in hash_table.items():
        if query == key or query == value:
            results.append(value)
    return results


def add_variable(hash_table):
    variable_name = input("Ingrese el nombre de la variable: ")
    key = input("Ingrese la clave de la variable (en formato 'fila,columna'): ")
    hash_table[key] = variable_name
    print("Variable agregada con éxito.")

def main():
    code = input("Ingrese el código fuente: ")

    tokens = tokenize(code)
    hash_table = hash_tokens(tokens)

    print("Tabla hash:")
    for key, value in hash_table.items():
        print(f'{key}: {value}')

    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar una variable")
        print("2. Agregar una variable")
        print("3. Salir")
        option = input("Ingrese una opción: ")

        if option == "1":
            query = input("Ingrese el nombre de la variable o la clave (en formato 'fila,columna'): ")
            results = search_variable(hash_table, query)
            if results:
                print(f"La clave '{query}' corresponde a la variable:")
                for result in results:
                    print(result)
            else:
                print(f"No se encontró ninguna coincidencia para '{query}'.")

        elif option == "2":
            add_variable(hash_table)

        elif option == "3":
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()
