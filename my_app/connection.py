import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset='utf8',
                use_unicode=True

            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Group:
    def __init__(self, db_connection, group_name, base_date, genre):
        self.db_connection = db_connection.connection
        self.group_name = group_name
        self.base_date = base_date
        self.genre = genre

    def save(self):
        c = self.db_connection.cursor()
        c.execute('INSERT INTO my_app_groupmodel (group_name, base_date, genre) VALUES (%s, %s, %s)',
                  (self.group_name, self.base_date, self.genre))
        self.db_connection.commit()
        c.close()

    def update(self):
        c = self.db_connection.cursor()
        c.execute('UPDATE my_app_groupmodel SET genre = "Рок" WHERE id=10')
        self.db_connection.commit()
        c.close()

    def delete_item(self):
        c=self.db_connection.cursor()
        c.execute('DELETE FROM my_app_groupmodel WHERE id=11')
        self.db_connection.commit()
        c.close()

con = Connection('dbuser', '123', 'music_db')

with con:
    group = Group(con, 'Бета', '1983-01-01', 'Рок, Хард-рок, Поп-рок')
    group.save()
    group.delete_item()
    group.update()