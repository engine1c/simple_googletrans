
import csv
from googletrans import Translator
translator = Translator()
with open('d:\mir_z\input.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # ���������� ���������, ���� ��� ����

    # ������� ������ ������ ��� �������� ������������ �����
    translated_rows = []

    # ��������� ������ ������ �� ����� CSV
    for row in csv_reader:
        ukr_text = row[0]  # ��������������, ��� ����� �� ���������� ����� ��������� � ������ �������

        # ��������� ����� � ����������� �� ��������
        translated_text = translator.translate(ukr_text, src='uk', dest='pl').text

        # �������� ������������ ������ � ������
        translated_rows.append([translated_text])

# �������� ������������ ������ � ����� ���� CSV
with open('d:\mir_z\output.csv', 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(translated_rows)
