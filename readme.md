## Результат порівняльного аналізу

```
+----------------------+--------------------+--------------------+---------------------+
|                      |   Час для 1000 ел. |   Час для 5000 ел. |   Час для 10000 ел. |
+======================+====================+====================+=====================+
| Сортування злиттям   |         0.00164213 |        0.00902929  |         0.0198944   |
+----------------------+--------------------+--------------------+---------------------+
| Сортування вставками |         0.0184561  |        0.467182    |         1.81846     |
+----------------------+--------------------+--------------------+---------------------+
| Сортування злиттям   |         7.1167e-05 |        0.000422417 |         0.000937542 |
+----------------------+--------------------+--------------------+---------------------+
```

## Висновки

- Сортування злиттям продемонструвало кращі результати, ніж сортування вставками, зокрема на великих масивах, підтверджуючи його ефективність для різноманітних сценаріїв.
- Сортування вставками виявилося найменш ефективним для великих масивів, але може бути корисним для малих або майже відсортованих даних.
- Timsort виявився найшвидшим, підтверджуючи свою високу ефективність, особливо для великих даних. 