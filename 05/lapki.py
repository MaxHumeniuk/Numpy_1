import csv

# Шлях до вихідного файлу CSV
input_csv_file = '/home/max/ppi-labs/05/data/NVDA.csv'

# Шлях до нового файлу CSV, у якому будуть додані лапки
output_csv_file = '/home/max/ppi-labs/05/data/NVDA_with_quotes.csv'

# Відкриття вихідного файлу для читання та нового файлу для запису
with open(input_csv_file, mode='r', newline='') as infile, open(output_csv_file, mode='w', newline='') as outfile:
    # Читаємо дані з вхідного файлу
    data = infile.readlines()
    
    # Додаємо лапки до кожного значення у кожному рядку
    data_with_quotes = ['"' + line.strip().replace(',', '","') + '"' for line in data]
    
    # Записуємо оновлені дані у новий файл
    outfile.write('\n'.join(data_with_quotes))

print("Лапки були додані до кожного значення у файлі AMD.csv і результат збережено у файлі AMD_with_quotes.csv")
