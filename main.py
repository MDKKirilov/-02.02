input = input("Введите строку: ")

def text(text):
    return ' '.join(word.capitalize() for word in text.split())

print(text(input))