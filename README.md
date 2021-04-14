## API по работе с postgres

### *Методы:*

* select_all - Возвращает таблицу, name - название таблицы, *args - через запятую поля по которым выводить, и в самом конце можно указать fetch методы 'fetchall', 'fetchone', 'fetchmany'    
* select_sql - Возвращает таблицу, name - название таблицы, sql_name - в формате SQL вводим запросы например(ORDER BY, DESC, WHERE, LIMIT, LIKE), *args - через запятую поля по которым выводить, и в самом конце можно указать fetch методы 'fetchall', 'fetchone', 'fetchmany'
* show_columns_name - Выводит название полей таблицы
* insert - Добавление данных в таблицу

#### Перед использование создать экземпляр класса AlchemyApi
##### Пример заполнения методов
```html
user = AlchemyApi('username', 'password', 'database')
user.select_all('executor', 'name', 'id', 'fetchone')
user.select_sql('album', 'ORDER BY id', 'name', 'year_of_issue', 'fetchone')
user.show_columns_name('track')
user.insert('track', 'id, name, duration, id_album', 19, 'name', 3.03, 1)
```