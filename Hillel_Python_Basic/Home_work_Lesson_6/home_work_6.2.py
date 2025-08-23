total_seconds = int(input('Введіть, будь ласка, число від 0 до 8640000: '))
days, rem_days = divmod(total_seconds, 86400)
hours, rem_hours = divmod(rem_days, 3600)
minutes, seconds = divmod(rem_hours, 60)
# Відмінювання слова день
def word_inflection(n):
    if 11 <= n % 100 <= 19:
        return 'днів'
    elif n % 10 == 1:
        return 'день'
    elif n % 10 in (2, 3, 4):
        return 'дні'
    else:
        return 'днів'
print(f'{days} {word_inflection(days)}, {hours:02}:{minutes:02}:{seconds:02}')