"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import xmlrpc.client

class HelloOdoo(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # user 
        user_label = toga.Label(
            'User: ',
            style=Pack(padding=(0, 5))
        )
        self.user_input = toga.TextInput(style=Pack(flex=1))

        user_box = toga.Box(style=Pack(direction=ROW, padding=5))
        user_box.add(user_label)
        user_box.add(self.user_input)

        # pwd
        pwd_label = toga.Label(
            'Password: ',
            style=Pack(padding=(0, 5))
        )
        self.pwd_input = toga.PasswordInput(style=Pack(flex=1))

        pwd_box = toga.Box(style=Pack(direction=ROW, padding=5))
        pwd_box.add(pwd_label)
        pwd_box.add(self.pwd_input)

        # url
        url_label = toga.Label(
            'Url: ',
            style=Pack(padding=(0, 5))
        )
        self.url_input = toga.TextInput(style=Pack(flex=1))

        url_box = toga.Box(style=Pack(direction=ROW, padding=5))
        url_box.add(url_label)
        url_box.add(self.url_input)

        # db
        db_label = toga.Label(
            'Db: ',
            style=Pack(padding=(0, 5))
        )
        self.db_input = toga.TextInput(style=Pack(flex=1))

        db_box = toga.Box(style=Pack(direction=ROW, padding=5))
        db_box.add(db_label)
        db_box.add(self.db_input)

        # output
        output_label = toga.Label(
            'Output: ',
            style=Pack(padding=(0, 5))
        )
        self.output_input = toga.TextInput(style=Pack(flex=1))

        output_box = toga.Box(style=Pack(direction=ROW, padding=5))
        output_box.add(output_label)
        output_box.add(self.output_input)

        button = toga.Button(
            'Login',
            on_press=self.do_login,
            style=Pack(padding=5)
        )

        main_box.add(user_box)
        main_box.add(pwd_box)
        main_box.add(url_box)
        main_box.add(db_box)
        main_box.add(output_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def do_login(self, widget):
        db = self.db_input.value
        url = self.url_input.value
        username = self.user_input.value
        password = self.pwd_input.value
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        res = common.version()
        uid = common.authenticate(db, username, password, {})
        print("DEBUG", str(res), uid)
        self.output_input.value = str(res) + ' - ' + str(uid)

def main():
    return HelloOdoo()
