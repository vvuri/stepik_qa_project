## Page Object Model
- это паттерн программирования
- каждую страницу веб-приложения можно описать в виде объекта класса
- cпособы взаимодействия пользователя со страницей можно описать с помощью методов класса
- Page Object, должен описывать бизнес-логику тестового сценария и скрывать Selenium-методы взаимодействия с браузером и страницей
- отделяем логику действий, например, авторизовать пользователя, от конкретной реализации 
- это абстрактный объект, который содержит в себе методы для работы с конкретной веб-страницей. 
- бывают двух типов: сделать что-то и проверить что-то.

[обработка исключение](https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html)

символ * в (*MainPageLocators.LOGIN_LINK) указывает на то, что мы передали пару значений, и этот кортеж нужно распаковать




#### Дополнительные фреймворки
- *Splinter* - довольно мощная надстройка над Selenium WebDriver, имеет множество дополнительных методов. Для работы совместно с PyTest существует специальный плагин pytest-splinter, включающий собственные фикстуры.
    - Использование двух сессий браузера в тесте одновременно, например, для настройки окружения через админскую часть сайта.
    - Возможность задавать паузу после каждой команды WebDriver для дебага или презентации работы тестов.
    - Задание директории по умолчанию для скачивания файлов, что является проблемой в обычном Selenium, который не умеет работать с нативным диалогом сохранения файлов в ОС.
    - Возможность автоматического создания скриншотов в случае падения тестов.
- *Selene* - реализация для Python идей популярного Java-фреймворка Selenide.
- *PyPOM* - библиотека для реализации Page Object Model от разработчиков из проекта Mozilla. Поддерживает работу со [Splinter](https://github.com/mozilla/PyPOM)
- *Webium* - легковесная реализация Page Object Model от разработчиков и тестировщиков Wargaming.net
- pytest-bdd - Gherkin language: @scenario, @given, @when, @then. (документация)[https://pytest-bdd.readthedocs.io/en/latest/] 