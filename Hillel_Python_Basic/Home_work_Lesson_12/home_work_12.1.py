import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Читаємо наш файл
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Прибираємо html-тегі
    text = re.sub(r'<.*?>', '', html)

    # прибираємо пусті строки
    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned_text = "\n".join(cleaned_lines)

    # Записуємо у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)