"""Convert Numbers Module

Este script lee números enteros desde archivos de texto, los convierte a formato binario y 
hexadecimal, y genera un archivo de salida con los resultados en formato tabular.
"""

import sys  # Manejo de argumentos de línea de comandos
import time  # Medición del tiempo de ejecución

def read_numbers(file_path):
    """Lee números enteros desde un archivo de texto y maneja errores."""
    numbers = []
    invalid_entries = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    invalid_entries.append(line.strip())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}.")
        sys.exit(1)
    return numbers, invalid_entries

def convert_numbers(numbers):
    """Convierte números enteros a binario y hexadecimal."""
    conversions = []
    for idx, num in enumerate(numbers, start=1):
        binary = bin(num)[2:]  # Convierte a binario y elimina el prefijo '0b'
        hexadec = hex(num)[2:].upper()  # Convierte hexadecimal, elimina '0x' y pone en mayúsculas
        conversions.append((idx, num, binary, hexadec))
    return conversions

def main():
    """Procesa múltiples archivos y guarda los resultados en un solo archivo de salida."""
    if len(sys.argv) < 2:
        print("Uso: python convert_numbers.py <archivo1.txt> <archivo2.txt> ...")
        sys.exit(1)
    start_time = time.time()  # Registro del tiempo de inicio
    with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
        for file_path in sys.argv[1:]:
            numbers, invalid_entries = read_numbers(file_path)
            conversions = convert_numbers(numbers)
            elapsed_time = time.time() - start_time
            result_file.write(f"\nResultados para {file_path}:\n")
            result_file.write("ITEM\tDECIMAL\tBIN\tHEX\n")
            for idx, num, binary, hexadec in conversions:
                result_file.write(f"{idx}\t{num}\t{binary}\t{hexadec}\n")
            if invalid_entries:
                result_file.write("\nEntradas inválidas ignoradas:\n")
                for entry in invalid_entries:
                    result_file.write(f"{entry}\n")
                print("Advertencia: Algunas entradas inválidas fueron ignoradas.")
            result_file.write(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n\n")
if __name__ == "__main__":
    main()
