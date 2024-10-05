# Проект "Виджет банковских операций"

## Описание:

Это виджет, который показывает несколько последних успешных банковских операций клиента.  Проект, 
который на бэкенде будет готовить данные для отображения в новом виджете.

* Реализована функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера.
* Реализована функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
     где X — это цифра номера.
* Реализована функция, которая принимает один аргумент — строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером.
    Для карт и счетов используйте разные типы маскировки
* Реализована функция, которая принимает на вход строку с датой в формате 
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024").
* Реализована функция, которая принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
* Реализована функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
* Реализована функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции, 
    где валюта операции соответствует заданной (например, USD).
* Реализован генератор, который принимает список словарей с транзакциями 
    и возвращает описание каждой операции по очереди.
* Создан генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров.
* Создан декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор должен принимать необязательный аргумент 
    filename, который определяет, куда будут записываться логи (в файл или в консоль).
* Реализована функция, которая принимает на вход путь до JSON-файла и возвращает список словарей 
    с данными о финансовых транзакциях.
* Реализована функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
* Реализована, функция, которая обращается к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
* Реализована функция, которая считывает финансовые операции из XLSX-файлов.
* Реализована функция, которая считывает финансовые операции из CSV--файлов.
* Реализована функция, которая принимает список словарей с данными о банковских операциях 
    и строку поиска. Возвращает список словарей, у которых в описании есть данная строка.
* Реализована функция, которая принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
## Установка:

1. Клонируйте репозиторий удобным способом:
```
git@github.com:syoumanator/Homework.git
```
```
https://github.com/syoumanator/Homework.git
```

2. Установите зависимости:
```
poetry install
```
## Тестирование:
* Добавлены тесты модуля masks
* Добавлены тесты модуля widget
* Добавлены тесты модуля processing
* Добавлены тесты модуля generators
* Добавлены тесты модуля decorators
* Добавлены тесты модуля utils
* Добавлены тесты модуля external_api
* Добавлены тесты модуля read_csv
* Добавлены тесты модуля read_excel
* Добавлены тесты модуля main


Покрытие тестами составляет 100%


## Логирование:
Добавлено логирование модуля utils
Добавлено логирование модуля masks
Добавлено логирование модуля read_csv
Добавлено логирование модуля read_excel


## Использование:


## Документация:


## Лицензия:
