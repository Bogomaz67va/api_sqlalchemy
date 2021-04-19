import sqlalchemy


class AlchemyApi:
    method = ['fetchall', 'fetchone', 'fetchmany']

    def __init__(self, login_db: str, password_db: str, name_db: str):
        """login_db - логин или username"""
        """password_db - пароль"""
        """name_db - имя базы данных"""
        self.login_db = login_db
        self.password_db = password_db
        self.name_db = name_db

        self.db_url = f'postgresql://{self.login_db}:{self.password_db}@localhost:5432/{name_db}'
        self.engine = sqlalchemy.create_engine(self.db_url)
        self.connection = self.engine.connect()

    def select_all(self, name: str, *args: str):
        """Возвращает таблицу"""
        """name - название таблицы"""
        """*args - через запятую поля по которым выводить, и в самом конце можно указать fetch метод
        ['fetchall', 'fetchone', 'fetchmany']
        """
        if AlchemyApi.method[1] in list(args):
            string_args = ', '.join(args[:-1])
            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name};").fetchone())
            else:
                print(self.connection.execute(f"SELECT * FROM {name};").fetchone())
        elif AlchemyApi.method[2] in list(args):
            string_args = ', '.join(args[:-2])
            if args[-1].isdigit():
                n = int(args[-1])
            else:
                print('Введите через запятую, сколько нужно записей')
                exit()

            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name};").fetchmany(n))
            else:
                print(self.connection.execute(f"SELECT * FROM {name};").fetchmany(n))
        elif AlchemyApi.method[0] in list(args):
            string_args = ', '.join(args[:-1])
            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name};").fetchall())
            else:
                print(self.connection.execute(f"SELECT * FROM {name};").fetchall())
        else:
            string_args = ', '.join(args)
            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name};").fetchall())
            else:
                print(self.connection.execute(f"SELECT * FROM {name};").fetchall())

    def select_sql(self, name: str, sql_name: str, *args: str):
        """Возвращает таблицу"""
        """name - название таблицы"""
        """sql_name - в формате SQL вводим запросы например(ORDER BY, DESC, WHERE, LIMIT, LIKE)"""
        """*args - через запятую поля по которым выводить, и в самом конце можно указать fetch метод
        ['fetchall', 'fetchone', 'fetchmany']
        """
        if AlchemyApi.method[1] in list(args):
            string_args = ', '.join(args[:-1])
            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name} {sql_name};").fetchone())
            else:
                print(self.connection.execute(f"SELECT * FROM {name} {sql_name};").fetchone())
        elif AlchemyApi.method[2] in list(args):
            string_args = ', '.join(args[:-2])
            if args[-1].isdigit():
                n = int(args[-1])
            else:
                print('Введите через запятую, сколько нужно записей')
                exit()

            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name} {sql_name};").fetchmany(n))
            else:
                print(self.connection.execute(f"SELECT * FROM {name} {sql_name};").fetchmany(n))
        elif AlchemyApi.method[0] in list(args):
            string_args = ', '.join(args[:-1])
            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name} {sql_name};").fetchall())
            else:
                print(self.connection.execute(f"SELECT * FROM {name} {sql_name};").fetchall())
        else:
            string_args = ', '.join(args)
            if string_args:
                print(self.connection.execute(f"SELECT {string_args} FROM {name} {sql_name};").fetchall())
            else:
                print(self.connection.execute(f"SELECT * FROM {name} {sql_name};").fetchall())

    def show_columns_name(self, name: str):
        """Выводит название полей таблицы"""
        print(self.connection.execute(
            f"SELECT column_name FROM information_schema.columns WHERE table_name='{name}'").fetchall())

    def insert(self, name_table: str, name_columns: str, *args):
        """Добавление данных в таблицу"""
        print(self.connection.execute(f"INSERT INTO {name_table} ({name_columns}) VALUES {args};"))

    def command_sql(self, sql: str):
        print(self.connection.execute(f"{sql}").fetchall())
