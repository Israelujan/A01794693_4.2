"""Compute_Statistics Module

This script reads numerical data from a file, computes basic statistics, 
and saves the results. It follows PEP-8 guidelines and handles errors appropriately.
"""

import sys  # Importa el módulo sys para manejar argumentos de línea de comandos
import time  # Importa el módulo time para medir el tiempo de ejecución
from collections import Counter  # Importa Counter para calcular la moda de los números

def read_numbers(file_path):
    """Lee los números desde un archivo de texto y maneja errores en los datos."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data ignored: {line.strip()}")
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    return numbers

def compute_statistics(numbers):
    """Calcula estadísticas básicas: count, media, mediana, moda, varianza y desviación estándar."""
    if not numbers:
        return None
    count = len(numbers)  # Cantidad de números válidos
    mean = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    median = (
        sorted_numbers[count // 2] if count % 2 != 0
        else (sorted_numbers[count // 2 - 1] + sorted_numbers[count // 2]) / 2
    )
    counter = Counter(numbers)
    mode = max(counter, key=counter.get)
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = variance ** 0.5
    return count, mean, median, mode, variance, std_dev
def main():
    """Función principal que procesa los archivos de entrada y guarda los resultados."""
    if len(sys.argv) < 2:
        print("Usage: python compute_statistics.py <file1.txt> <file2.txt> ...")
        sys.exit(1)
    start_time = time.time()
    with open("StatisticsResults.txt", 'a', encoding='utf-8') as result_file:
        for file_path in sys.argv[1:]:
            numbers = read_numbers(file_path)
            stats = compute_statistics(numbers)
            elapsed_time = time.time() - start_time
            if stats:
                count, mean, median, mode, variance, std_dev = stats
                output = (
                    f"Results for {file_path}:\n"
                    f"COUNT: {count}\n"
                    f"Mean: {mean}\n"
                    f"Median: {median}\n"
                    f"Mode: {mode}\n"
                    f"Variance: {variance}\n"
                    f"Standard Deviation: {std_dev}\n"
                    f"Execution Time: {elapsed_time:.4f} seconds\n\n"
                )
                print(output)
                result_file.write(output)
            else:
                print(f"No valid numbers found in {file_path}.")
                result_file.write(f"No valid numbers found in {file_path}.\n\n")

if __name__ == "__main__":
    main()
