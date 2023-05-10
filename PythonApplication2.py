
import csv
from googletrans import Translator
translator = Translator()
with open('d:\mir_z\input.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Пропустить заголовки, если они есть

    # Создать пустой список для хранения переведенных строк
    translated_rows = []

    # Прочитать каждую строку из файла CSV
    for row in csv_reader:
        ukr_text = row[0]  # Предполагается, что текст на украинском языке находится в первом столбце

        # Перевести текст с украинского на польский
        translated_text = translator.translate(ukr_text, src='uk', dest='pl').text

        # Добавить переведенную строку в список
        translated_rows.append([translated_text])

# Записать переведенные строки в новый файл CSV
with open('d:\mir_z\output.csv', 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(translated_rows)
