from idlelib import query

import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import os

class Database:
    def __init__(self):
        self.config = {
            "host": "localhost",
            'database': 'shop_db',
            'user': 'RaineWhispers',
            'password': 'F@byf_102360'
        }
        self.connection = None
        self.connect()

        def connect(self):
            try:
                self.connection = mysql.connector.connect(**self.config)
                if self.connection.is_connected():
                    print('Connected to MySQL database')
            except Error as e:
                messagebox.showerror("Ошибка БД", e)

        def execute_query(self, query, params=None):
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, params or ())
                self.connection.commit()
                return True
            except Error as e:
                messagebox.showerror("Ошибка БД", e)
                return []
            finally:
                cursor.close()

            def fetch_all(self, query, params=None):
                cursor = self.connection.cursor(dictionary=True)
                try:
                    cursor.execute(query, params or ())
                    return cursor.fetchall()
                except Error as e:
                    messagebox.showerror("Ошибка БД", e)
                    return []
                finally:
                    cursor.close()

class ShoeStoreShop:
    def __init__(self, root):
        self.root = root
        self.root.title("Чудо Обувь - демэкзамен")
        self.root.geometry("1000x700")

        self.colors = {
            'primary': '#FFFFFF',
            'secondary': '#D2F6E7',
            'accent': '#70B2AF',
            'malo_tovarov': '#FF8080'
        }

        self.root.configure(bg=self.colors['primary'])

        self.current_user = None

        self.show_login_window()

    def show_login_window(self):
        self.clear_window()
        login_frame = tk.Frame(self.root, bg=self.colors['primary'])
        login_frame.place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(login_frame,text='Вход в систему', font=('Calibri', 20, 'bold'), bg=self.colors['primary']).pack(pady=20)
        self.login_entry = tk.Entry(login_frame, font=('Calibri', 12), bg=self.colors['primary'], width=30)
        self.login_entry.pack(pady=5)

        btn = tk.Button(login_frame, text = "Войти",font=('Calibri', 12),bg=self.colors['primary'], fg='white', width=20, command=self.login)
        btn.pack(pady=20)

    def login(self):
        login_input = self.login_entry.get().strip()
        if not login_input:
            messagebox.showwarning("Внимание", "Пожалуйста, введи логин, собака!")
            return

        query = "SELECt id, last_name, first_name, otchestvo, role FROM users WHERE login = %s"
        user = self.db.fetch_all(query, (login_input,))

        if user:
            self.current_user = user[0]
            self.show_main_window()
        else:
            messagebox.showerror('Аттэншн','неверные данные, пёс!!!')

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
if os.path.exists('/Users/electron/Downloads/Прил_ОЗ_КИМ_09.02.07-2-2027/ПА/Задание 1/Прил_2_ОЗ_КИМ_09.02.07-2-2027/Чудо Обувь.ico'):
    root.iconbitmap('/Users/electron/Downloads/Прил_ОЗ_КИМ_09.02.07-2-2027/ПА/Задание 1/Прил_2_ОЗ_КИМ_09.02.07-2-2027/Чудо Обувь.ico')

app = ShoeStoreShop(root)
root.mainloop()