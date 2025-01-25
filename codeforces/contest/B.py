"""B. Кевин и Геометрия
ограничение по времени на тест
1 секунда
ограничение по памяти на тест
256 мегабайт

У Кевина есть n
палочек с длинами a1,a2,…,an

.

Кевин хочет выбрать из них 4
палочки, чтобы сформировать равнобедренную трапецию∗ с положительной площадью. Обратите внимание, что прямоугольники и квадраты также считаются равнобедренными трапециями. Помогите Кевину найти решение. Если решения не существует, выведите −1

.

∗

Равнобедренная трапеция — это выпуклый четырехугольник с осью симметрии, делящей пополам одну пару противоположных сторон. В любой равнобедренной трапеции две противоположные стороны (основания) параллельны, а две другие стороны (боковые) равны по длине.
Входные данные

Каждый тест состоит из нескольких наборов входных данных. В первой строке находится одно целое число t
(1≤t≤104

) — количество наборов входных данных. Далее следует описание наборов входных данных.

Первая строка каждого набора входных данных содержит одно целое число n
(4≤n≤2⋅105

).

Вторая строка содержит n
целых чисел a1,a2,…,an (1≤ai≤108

).

Гарантируется, что сумма значений n
по всем наборам входных данных не превосходит 2⋅105

.
Выходные данные

Для каждого набора входных данных выведите 4
целых числа — длины палочек. Если решения не существует, выведите −1

.

Если существует несколько решений, выведите любое из них.
Пример
Входные данные
Скопировать

7
4
5 5 5 10
4
10 5 10 5
4
1 2 3 4
4
1 1 1 3
6
4 2 1 5 7 1
6
10 200 30 300 30 100
4
100000000 100000000 1 2

Выходные данные
Скопировать

5 5 5 10
5 5 10 10
-1
-1
1 1 4 5
-1
100000000 100000000 1 2

Примечание

В первом наборе входных данных можно сформировать равнобедренную трапецию с основаниями длиной 5
и 10 и двумя боковыми сторонами длиной 5

.

Во втором наборе входных данных можно сформировать равнобедренную трапецию с двумя основаниями длиной 5
и двумя боковыми сторонами длиной 10

. Прямоугольник также считается равнобедренной трапецией.

В третьем наборе входных данных нет палочек одинаковой длины. Следовательно, невозможно сформировать равнобедренную трапецию.

В четвертом наборе входных данных невозможно сформировать равнобедренную трапецию с положительной площадью."""

t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    a = list(map(int, input().split(' ')))
    for






