
class Test:
    @property
    def create(self):
        return '123'

# Создаем экземпляр класса
a = Test()
# Вызываем свойство без скобочек
result = a.create
print(type(result))  # Вывод: 123