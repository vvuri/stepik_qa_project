## Тестовый проект на Stepik

```bash
$ pytest -v --tb=line --language=en test_main_page.py
```

Запуск конкретного теста через ключик -k
```bash
$ pytest -v --tb=line --language=en test_main_page.py -k "guest_can_go_to_login_page"
```

Для отладки и вывода сообщений через print - ключик -s