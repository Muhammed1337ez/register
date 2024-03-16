import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("../d22.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key ,
                full_name varchar not null ,
                email varchar,
                phone integer, 
                birth integer )
        """)

    def insert_user(self, full_name, email):
        self.cursor.execute("insert into user (full_name, email) values (?, ?)",
                            (full_name, email))
        self.connection.commit()

    def read_all_user(self):
        users = self.cursor.execute("select * from user").fetchall()
        return users

    def get_user(self, id):
        user = self.cursor.execute("select * from user where id=?", (id,)).fetchone()
        return user

    def update_user(self, id, full_name, email):
        self.cursor.execute("update user set full_name=?, email=? where id=?",
                            (id, full_name, email))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("delete from user where id=?", (id,))
        self.connection.commit()





