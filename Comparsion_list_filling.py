# Импорт библиотеки для работы с временем.
import time
from array import array
# Количество элементов в массивах.
elements_count = 10000000

# Эксперимент 1
# Засекаем время начала.
start_time = time.time()
# Резервируем место в памяти на 10 млн элементов.
# При этом ОС забронирует чуть больший размер.
data1 = [None] * elements_count
for data_index in range(elements_count):
    # Заполняем элементы списка по индексу.
    data1[data_index] = f'Some new value {data_index}'
# Печатаем время выполнения.
print(
    'Создание списка с 10 млн пустых элементов и его заполнение:',
    time.time() - start_time
)

# Эксперимент 2
# Засекаем новое время.
start_time = time.time()
# Объявляем пустой список; ОС не знает его ожидаемый размер.
data2 = []
for data_index2 in range(elements_count):
    # Добавляем новые элементы в конец списка.
    data2.append(f'some new value {data_index2}')
# Печатаем время выполнения.
print(
    'Создание пустого списка и добавление в него 10 млн элементов:',
    time.time() - start_time
)

start_time = time.time()
# Объявляем пустой список; ОС не знает его ожидаемый размер.
data3 = array('L')
for data_index3 in range(elements_count):
    # Добавляем новые элементы в конец списка.
    data3.append(data_index3)
# Печатаем время выполнения.
print(
    'Создание пустого array и добавление в него 10 млн элементов:',
    time.time() - start_time
)
