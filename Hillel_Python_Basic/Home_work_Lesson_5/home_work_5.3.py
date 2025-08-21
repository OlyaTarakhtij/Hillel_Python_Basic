import string

any_string = input('Введіть якусь строку, будь ласка: ')
table = str.maketrans('', '', string.punctuation)  # видалення знаків пунктуації
clean_string = any_string.translate(table)
hashtag_string = ['#' + ''.join(word.capitalize() for word in clean_string.split())] # переведення першої літери кожного слова на велику та скліювання без пробілів

if len(hashtag_string) > 140: # Перевірка довжини строки
    hashtag_string = hashtag_string[:140] # скорочення до 140 символів

print(hashtag_string)