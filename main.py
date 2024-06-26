# Запросить строку у пользователя
input = input("Введите строку: ")

# Функция для преобразования первых букв в прописные
def text(text):
    return ' '.join(word.capitalize() for word in text.split())

# Вывести результат
print(text(input))