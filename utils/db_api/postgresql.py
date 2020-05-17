import asyncpg
from data import config


class Database:
    def __init__(self):
        self.pool: asyncpg.pool.Pool = await asyncpg.create_pool(user=config.PGUSER,
                                                                 password=config.PGPASSWORD,
                                                                 host=config.ip)

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            PRIMARY KEY (id)
            );
"""
        self.pool.execute(sql)

    def add_user(self, id: int, name: str, email: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email) VALUES(?, ?, ?)
        """
        self.pool.execute(sql, id, name, email)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.pool.fetchval(sql)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"

        parameters = " AND ".join([
            f"{item} = ?" for item in kwargs
        ])
        sql = f"""
        SELECT * FROM Users WHERE {parameters}
        """
        return self.pool.fetchval(sql, parameters=tuple(kwargs.values()))

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id, **kwargs):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


if __name__ == '__main__':
    db = Database()
    # db.create_table_users()
    # db.add_user(1, "One", "email")
    # db.add_user(2, "Vasya", "vv@gmail.com")
    # db.add_user(3, 1, 1)
    # db.add_user(4, 1, 1)
    # db.add_user(5, "John", "john@mail.com")

    users = db.select_all_users()
    print(f"Получил всех пользователей: {users}")

    user = db.select_user(Name="John", id=5)
    print(f"Получил пользователя: {user}")

    users = db.select_all_users()
    print(f"Получил всех пользователей: {users}")
