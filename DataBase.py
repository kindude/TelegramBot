import sqlite3


class DataBase:

    #initialising database
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()

    #check if user exists
    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `user_id` FROM `users`  WHERE `user_id`= ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, data):
        user_id = data[0]
        firstname = data[1]
        lastname = data[2]
        dob = data[3]
        self.cursor.execute("INSERT INTO `users`(`user_id`, `firstname`, `lastname`, `dob`) VALUES (?,?,?,?) ", (user_id, firstname, lastname, dob))
        return self.con.commit()

    def get_users(self):
        result = self.cursor.execute("SELECT * FROM `users`")
        self.con.commit()
        return result.fetchall()

    def get_user(self, user_id):
        result = self.cursor.execute("SELECT `firstname`, `lastname`, `dob` FROM `users` WHERE `user_id` = ?", (user_id,) )
        self.con.commit()
        return result.fetchall()

    def update_user(self, data):
        user_id = data[0]
        firstname = data[1]
        lastname = data[2]
        dob = data[3]

        self.cursor.execute("UPDATE `users` SET `firstname` = ? , `lastname` = ? , `dob` = ? WHERE `user_id` = ?", (firstname, lastname, dob, user_id,))
        return self.con.commit()

    def get_accounts(self, user_id):
        res = self.cursor.execute("SELECT `account_id`, `firstname`, `lastname`,`currency`, `balance` FROM `users` JOIN `accounts` ON `users`.`user_id` = `accounts`.`id_user` WHERE `user_id` = ?;", (user_id,))
        self.con.commit()
        return res.fetchall()

    def add_account(self, user_id):
        res = self.cursor.execute("INSERT INTO `accounts`(`id_user`, `currency`, `balance`) VALUES (?,?,?) ", (user_id, "RUB", 20000))
        self.con.commit()
        return res.fetchall()

    def get_references(self):
        res = self.cursor.execute("SELECT * FROM `discounts`;")
        self.con.commit()
        return res.fetchall()

    #close connection
    def close(self):
        self.con.close()



