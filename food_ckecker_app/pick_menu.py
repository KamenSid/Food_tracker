from tkinter import *
from database import *


class PickMenu:
    def __init__(self, root, welcome_menu):

        self.frame = root
        self.welcome_menu = welcome_menu
        self.buttons = self.button_creation()
        self.placement()

    @staticmethod
    def show_daily_intake_func():
        cursor.execute("SELECT * FROM daily_intake")
        daily_intake_list = cursor.fetchall()
        print(daily_intake_list)

    @staticmethod
    def del_daly_intake():
        cursor.execute("DELETE FROM daily_intake")
        connection.commit()

    @staticmethod
    def del_fast_foods():
        cursor.execute("SELECT * FROM fast_foods")
        cursor.execute("DELETE FROM fast_foods")
        connection.commit()

    def back_to_menu_func(self):
        self.frame.grid_forget()
        welcome_menu = self.welcome_menu()
        welcome_menu.welcome_menu_func()


    def button_creation(self):
        buttons = {}
        show_button = Button(self.frame,
                             text="Show daily intake",
                             font=("Comic sans MS", 20, "bold"),
                             bg="#6e8b3d",
                             activebackground="#51803e",
                             command=self.show_daily_intake_func,
                             height=2,
                             width=30,
                             )
        buttons["show_button"] = show_button
        delete_button = Button(self.frame,
                               text="Delete Daly",
                               font=("Comic sans MS", 20, "bold"),
                               bg="#6e8b3d",
                               activebackground="#51803e",
                               command=self.del_daly_intake,
                               height=2,
                               width=30
                               )
        buttons["delete_button"] = delete_button
        delete_fast_button = Button(self.frame,
                               text="Delete Fast Foods",
                               font=("Comic sans MS", 20, "bold"),
                               bg="#6e8b3d",
                               activebackground="#51803e",
                               command=self.del_fast_foods,
                               height=2,
                               width=30
                               )
        buttons["delete_fast_button"] = delete_fast_button
        back_button = Button(self.frame,
                             text="Back to Main menu",
                             font=("Comic sans MS", 20, "bold"),
                             bg="#6e8b3d",
                             activebackground="#51803e",
                             command=self.back_to_menu_func,
                             height=2,
                             width=30
                             )
        buttons["back_button"] = back_button
        return buttons

    def placement(self):

        row = 0
        col = 0
        for butt in self.buttons.values():
            if col == 4:
                row += 1
                col = 0
            butt.grid(row=row, column=col)
            col += 1

        self.buttons["show_button"].grid(row=1, column=0, columnspan=4)
        self.buttons["delete_button"].grid(row=3, column=0, columnspan=4)
        self.buttons["delete_fast_button"].grid(row=2, column=0, columnspan=4)
        self.buttons["back_button"].grid(row=4, column=0, columnspan=4)
        self.frame.grid()

