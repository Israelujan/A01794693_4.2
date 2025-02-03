"""Word Count Module

Este script cuenta la frecuencia de palabras en archivos de texto, eliminando signos de puntuación,
convirtiendo a minúsculas y generando un archivo de salida con los resultados.
"""

import sys  # Manejo de argumentos de línea de comandos
import time  # Medición del tiempo de ejecución
import string  # Para eliminar signos de puntuación
from collections import Counter  # Para contar la frecuencia de palabras

def read_words(file_path):
    """Lee palabras desde archivo, eliminando signos de puntuación y normalizando a minúsculas."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip().lower().translate(
                    str.maketrans('', '', string.punctuation))
                words.extend(cleaned_line.split())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}.")
        sys.exit(1)
    return words

def count_words(words):
    """Cuenta la frecuencia de cada palabra en la lista."""
    return Counter(words)

def main():
    """Procesa múltiples archivos y genera un archivo de salida separado para cada TC."""
    if len(sys.argv) < 2:
        print("Uso: python word_count.py <archivo1.txt> <archivo2.txt> ...")
        sys.exit(1)
    start_time = time.time()  # Registro del tiempo de inicio
    for file_path in sys.argv[1:]:
        words = read_words(file_path)  # Leer palabras del archivo
        word_freq = count_words(words)  # Contar frecuencia de palabras
        elapsed_time = time.time() - start_time  # Calcular tiempo de ejecución
        # Generar un archivo de salida separado para cada TC con formato correcto
        output_file = f"WordCountResults_{file_path}"
        with open(output_file, 'w', encoding='utf-8') as result_file:
            result_file.write(f"Resultados para {file_path}:\n\n")
            result_file.write("Palabra            Frecuencia\n")
            result_file.write("-----------------------------\n")
            for word, count in sorted(word_freq.items(), key=lambda x: (-x[1], x[0])):
                result_file.write(f"{word:<20}{count}\n")
            result_file.write(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n")
        print(f"Resultados guardados en {output_file}")
if __name__ == "__main__":
    main()
