import sys  # Importa el módulo sys para manejar argumentos de la línea de comandos y la salida del programa.
import time  # Importa el módulo time para medir el tiempo de ejecución.

def read_numbers(file_path):
    """Lee números desde un archivo y filtra las entradas inválidas."""
    numbers = []  # Lista para almacenar los números válidos.
    invalid_entries = []  # Lista para almacenar las entradas no numéricas (inválidas).
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Abre el archivo en modo lectura con codificación UTF-8.
            for line in file:  # Itera sobre cada línea del archivo.
                try:
                    numbers.append(int(line.strip()))  # Intenta convertir la línea en un entero y lo agrega a la lista.
                except ValueError:
                    invalid_entries.append(line.strip())  # Si la conversión falla, agrega la línea a la lista de inválidos.
    except FileNotFoundError:
        print(f"Error: Archivo {file_path} no encontrado.")  # Mensaje de error si el archivo no se encuentra.
        sys.exit(1)  # Termina el programa con código de error 1.

    return numbers, invalid_entries  # Retorna la lista de números válidos y la lista de entradas inválidas.

def convert_numbers(numbers):
    """Convierte números a sus representaciones en binario y hexadecimal."""
    conversions = []  # Lista para almacenar los resultados de las conversiones.
    for num in numbers:  # Itera sobre cada número en la lista.
        binary = bin(num)[2:]  # Convierte el número a binario y elimina el prefijo '0b'.
        hexadec = hex(num)[2:].upper()  # Convierte el número a hexadecimal, elimina el prefijo '0x' y lo pone en mayúsculas.
        conversions.append((num, binary, hexadec))  # Almacena la tupla (decimal, binario, hexadecimal).
    
    return conversions  # Retorna la lista de conversiones.

def main():
    """Función principal del programa."""
    if len(sys.argv) != 2:  # Verifica que el programa reciba exactamente un argumento además del nombre del script.
        print("Uso: python convertNumbers.py <archivoConDatos.txt>")  # Mensaje de uso si los argumentos son incorrectos.
        sys.exit(1)  # Termina el programa con código de error 1.

    file_path = sys.argv[1]  # Obtiene el nombre del archivo desde los argumentos de la línea de comandos.
    start_time = time.time()  # Registra el tiempo de inicio de ejecución.

    numbers, invalid_entries = read_numbers(file_path)  # Llama a la función para leer y filtrar los números.
    conversions = convert_numbers(numbers)  # Convierte los números a binario y hexadecimal.
    elapsed_time = time.time() - start_time  # Calcula el tiempo total de ejecución.

    # Abre un archivo para escribir los resultados de las conversiones.
    with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
        for num, binary, hexadec in conversions:  # Itera sobre las conversiones realizadas.
            result = f"Decimal: {num}, Binario: {binary}, Hexadecimal: {hexadec}\n"  # Formatea la línea de resultado.
            print(result.strip())  # Muestra el resultado en la consola.
            result_file.write(result)  # Escribe el resultado en el archivo.

        result_file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")  # Registra el tiempo de ejecución en el archivo.

        if invalid_entries:  # Si hubo entradas inválidas en el archivo de entrada:
            result_file.write("\nEntradas inválidas ignoradas:\n")  # Agrega una sección en el archivo con las entradas inválidas.
            for entry in invalid_entries:  # Itera sobre las entradas inválidas.
                result_file.write(f"{entry}\n")  # Escribe cada entrada inválida en el archivo.
            print("Advertencia: Se ignoraron algunas entradas inválidas.")  # Muestra una advertencia en la consola.

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta directamente.
