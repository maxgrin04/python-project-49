<div align="center">
<h1>Игры разума / Brain games</h1>
</div>

## Описание проекта

**«Игры разума»** — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. 

Игры:
- Калькулятор. Арифметические выражения, которые необходимо вычислить
- Прогрессия. Поиск пропущенных чисел в последовательности чисел
- Определение четного числа
- Определение наибольшего общего делителя
- Определение простого числа

## Требования

- python ^3.12
- prompt ^0.4.1

## Инструкция по установке

#### Python

> Перед установкой пакета убедитесь, что у вас установлен Python версии 3.12 или выше:

```bash
python --version
# Python 3.12.0+
```
#### UV

> Проект использует менеджер зависимостей uv. Для установки uv используйте инструкцию (https://github.com/Hexlet/ru-instructions/blob/main/uv.md).

### Установка пакета

> Чтобы использовать пакет, вам нужно скопировать репозиторий на свой компьютер. Это делается с помощью команды ``git clone``:

```bash
git clone git@github.com:maxgrin04/python-project-49.git
```

> Далее выполните установку пакета:

```bash
cd python-project-49
```

```bash
uv build
uv tool install dist/*.whl
```

### Хекслет тесты и статус линтера:
[![Actions Status](https://github.com/maxgrin04/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/maxgrin04/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/0d7ecefcf286ffe5cd0d/maintainability)](https://codeclimate.com/github/maxgrin04/python-project-49/maintainability)

## Запуск игр

### _Игра: «Проверка на чётность»_

Пользователю показывается случайное число. И ему нужно ответить **"yes"**, если число чётное, или **"no"** — если нечётное.

> Для запуска игры используйте команду:
```bash
brain-even
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/f2EHDVjz3fx1ZiqrejDQntK5X.svg)](https://asciinema.org/a/f2EHDVjz3fx1ZiqrejDQntK5X)

### _Игра: «Калькулятор»_

Пользователю показывается случайное математическое выражение, например, **35 + 16**, которое нужно вычислить и записать правильный ответ.

> Для запуска игры используйте команду:
```bash
brain-calc
```

> Пример запуска игры:
[![asciicast]( https://asciinema.org/a/oy9BeTqRlYd1k9yEspRFJkTg8.svg)]( https://asciinema.org/a/oy9BeTqRlYd1k9yEspRFJkTg8)

### _Игра «НОД»_

Пользователю показывается два случайных числа, например, **25 50**. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

> Для запуска игры используйте команду:
```bash
brain-gcd
```

> Пример запуска игры:
[![asciicast]( https://asciinema.org/a/6DRiZuUvaLdhMkyW3ZFhf1aT8.svg)]( https://asciinema.org/a/6DRiZuUvaLdhMkyW3ZFhf1aT8)

### _Игра «Арифметическая прогрессия»_

Пользователю показывается ряд чисел, который образует арифметическую прогрессию. Одно из чисел скрыто двумя точками. Игрок должен определить это число.

> Для запуска игры используйте команду:
```bash
brain-progression
```

> Пример запуска игры:
[![asciicast]( https://asciinema.org/a/L9mg6QrXnyojxiR1OMBpLIBb3.svg)]( https://asciinema.org/a/L9mg6QrXnyojxiR1OMBpLIBb3)

### _Игра «Простое ли число?»_

Пользователю показывается случайное число. И ему нужно ответить **"yes"**, если число простое, или **"no"** — если составное.

> Для запуска игры используйте команду:
```bash
brain-prime
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/hWhjTYBGzVTCs6HIv5QyaKMhE.svg)](https://asciinema.org/a/hWhjTYBGzVTCs6HIv5QyaKMhE)