# Transport Class Example

Этот проект демонстрирует использование объектно-ориентированного программирования (ООП) в Python с помощью классов и наследования. В данном примере создается родительский класс `Transport` и дочерний класс `Autobus`, который наследует свойства и методы родительского класса.

## Описание

- **Класс `Transport`**:

  - Имеет конструктор, который принимает три параметра: `name`, `max_speed` и `mileage`.
  - Эти параметры сохраняются как атрибуты экземпляра класса.

- **Класс `Autobus`**:
  - Наследует от класса `Transport`.
  - Переопределяет конструктор, чтобы инициализировать атрибуты, используя метод `super()`.
  - Содержит метод `display_info()`, который выводит информацию об автобусе.
