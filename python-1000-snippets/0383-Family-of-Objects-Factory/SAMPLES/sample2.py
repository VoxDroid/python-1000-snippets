# sample2.py
# Factory that returns database connectors for different databases

class DatabaseConnection:
    def connect(self):
        raise NotImplementedError


class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to MySQL"


class PostgresConnection(DatabaseConnection):
    def connect(self):
        return "Connected to Postgres"


class DBFactory:
    def create_connection(self):
        raise NotImplementedError


class MySQLFactory(DBFactory):
    def create_connection(self):
        return MySQLConnection()


class PostgresFactory(DBFactory):
    def create_connection(self):
        return PostgresConnection()


def main():
    factory = PostgresFactory()
    conn = factory.create_connection()
    print(conn.connect())


if __name__ == "__main__":
    main()
