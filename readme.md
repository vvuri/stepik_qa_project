## Тестовый проект на Stepik

```bash
$ pytest -v --tb=line --language=en test_main_page.py
```

Запуск конкретного теста через ключик -k
```bash
$ pytest -v --tb=line --language=en test_main_page.py -k "guest_can_go_to_login_page"
```

Для отладки и вывода сообщений через print - ключик -s
```bash
$ pytest -s test_foo.py
```

Прогон по всем после рефакторинга:
```
$ pytest -v --tb=line --language=en
=== 23 passed, 20 skipped, 1 xfailed in 330.50 seconds ===
```