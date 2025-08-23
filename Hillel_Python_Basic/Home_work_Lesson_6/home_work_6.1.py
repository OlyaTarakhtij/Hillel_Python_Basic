import string

new_text = input('Введить діапазон літер через "-": ')
first_letter, last_letter = new_text.split('-')
first_index = string.ascii_letters.index(first_letter)
last_index = string.ascii_letters.index(last_letter)
all_letters = string.ascii_letters[first_index : last_index + 1]
print('Літери у вказаному діапазоні: ', ' '.join(all_letters))