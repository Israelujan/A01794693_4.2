import sys  # Importa el módulo sys para manejar argumentos de la línea de comandos y salida del programa.
import time  # Importa el módulo time para medir el tiempo de ejecución.
import string  # Importa string para manejar caracteres de puntuación.
from collections import Counter  # Importa Counter para contar la frecuencia de palabras de manera eficiente.

def read_words(file_path):
    """Lee palabras desde un archivo, normalizando el texto y eliminando la puntuación."""
    words = []  # Lista para almacenar las palabras extraídas.
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Abre el archivo en modo lectura con codificación UTF-8.
            for line in file:  # Itera sobre cada línea del archivo.
                # Elimina espacios en blanco alrededor de la línea, convierte a minúsculas y elimina la puntuación.
                cleaned_line = line.strip().lower().translate(str.maketrans('', '', string.punctuation))
                words.extend(cleaned_line.split())  # Divide la línea en palabras y las agrega a la lista.
    except FileNotFoundError:  
        print(f"Error: Archivo {file_path} no encontrado.")  # Muestra un mensaje de error si el archivo no existe.
        sys.exit(1)  # Termina el programa con código de error 1.

    return words  # Retorna la lista de palabras normalizadas.

def count_words(words):
    """Cuenta la frecuencia de cada palabra en una lista."""
    return Counter(words)  # Utiliza Counter para contar la cantidad de veces que aparece cada palabra.

def main():
    """Función principal del programa."""
    if len(sys.argv) != 2:  # Verifica que el programa reciba exactamente un argumento además del nombre del script.
        print("Uso: python wordCount.py <archivoConDatos.txt>")  # Muestra el uso correcto si los argumentos son incorrectos.
        sys.exit(1)  # Termina el programa con código de error 1.

    file_path = sys.argv[1]  # Obtiene el nombre del archivo desde los argumentos de la línea de comandos.
    start_time = time.time()  # Registra el tiempo de inicio de ejecución.

    words = read_words(file_path)  # Llama a la función para leer y normalizar las palabras.
    word_freq = count_words(words)  # Cuenta la cantidad de veces que aparece cada palabra.
    elapsed_time = time.time() - start_time  # Calcula el tiempo total de ejecución.

    # Abre un archivo para escribir los resultados del conteo de palabras.
    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        # Ordena las palabras por frecuencia en orden descendente y las recorre.
        for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
            result = f"{word}: {count}\n"  # Formatea la línea con la palabra y su frecuencia.
            print(result.strip())  # Muestra el resultado en la consola.
            result_file.write(result)  # Escribe el resultado en el archivo.

        result_file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")  # Guarda el tiempo de ejecución en el archivo.

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta directamente.
