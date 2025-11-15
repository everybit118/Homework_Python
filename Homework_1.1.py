print ("Скрипт по ДЗ 1. Насонова Ю.А. - Mid_letters")

word = input("Пожалуйста, введите слово на латинице: ")

length = len(word)
middle_index = length // 2

if length % 2 == 0:
    result = word[middle_index - 1:middle_index + 1]
else:
    result = word[middle_index]

print ("Результат операции:")
print(result)
