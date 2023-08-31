import datetime
from tkinter import *
from database import *
from API_comunication import *
import time


class AddMenu:
    def __init__(self, root, pick_menu, welcome_menu):
        self.frame = root
        self.buttons = self.button_creation()
        self.labels = self.label_creation()
        self.entries = self.entries_creation()
        self.pick_menu = pick_menu
        self.welcome_menu = welcome_menu
        self.get_food_vals = get_food_values
        self.placement()

    def label_creation(self):
        labels = {}
        search_question = Label(self.frame,
                                text=f"Input the name of the food\nto search automatically",
                                font=("Comic sans MS", 15, "bold"),
                                fg="#3ab675"
                                )
        labels["search"] = search_question
        id_label = Label(self.frame,
                         text="Food ID:",
                         font=("Comic sans MS", 10, "bold"),
                         fg="#9ab973"
                         )
        labels["id"] = id_label
        name_label = Label(self.frame,
                           text="Food Name:",
                           font=("Comic sans MS", 10, "bold"),
                           fg="#9ab973"
                           )
        labels["name"] = name_label
        calories_label = Label(self.frame,
                               text="Calories count:",
                               font=("Comic sans MS", 10, "bold"),
                               fg="#9ab973"
                               )
        labels["calories"] = calories_label
        protein_label = Label(self.frame,
                              text="Protein amount:",
                              font=("Comic sans MS", 10, "bold"),
                              fg="#9ab973"
                              )
        labels["protein"] = protein_label
        fat_label = Label(self.frame,
                          text="Fat amount:",
                          font=("Comic sans MS", 10, "bold"),
                          fg="#9ab973"
                          )
        labels["fat"] = fat_label
        carbs_label = Label(self.frame,
                            text="Carbs amount:",
                            font=("Comic sans MS", 10, "bold"),
                            fg="#9ab973"
                            )
        labels["carbs"] = carbs_label
        return labels

        # ENTRY CREATION

    def entries_creation(self):
        entries = {}
        id_entry = Entry(self.frame,
                         font=("Comic sans MS", 15, "bold"),
                         )
        entries["id"] = id_entry
        name_entry = Entry(self.frame,
                           font=("Comic sans MS", 15, "bold"),
                           )
        entries["name"] = name_entry
        calories_entry = Entry(self.frame,
                               font=("Comic sans MS", 15, "bold"),
                               )
        entries["calories"] = calories_entry
        protein_entry = Entry(self.frame,
                              font=("Comic sans MS", 15, "bold"),
                              )
        entries["protein"] = protein_entry
        fat_entry = Entry(self.frame,
                          font=("Comic sans MS", 15, "bold"),
                          )
        entries["fat"] = fat_entry
        carbs_entry = Entry(self.frame,
                            font=("Comic sans MS", 15, "bold"),
                            )
        entries["carbs"] = carbs_entry
        return entries

    def initial_button_load(self, args):
        cursor.execute("INSERT INTO daily_intake VALUES ({}, '{}', {}, {}, {}, {})".
                       format(args[0], args[1], args[2], args[3], args[4], args[5]))
        connection.commit()

    @staticmethod
    def show_fast_food_func():
        cursor.execute("SELECT * FROM fast_foods")
        fast_food_list = cursor.fetchall()
        print(fast_food_list)

    def add_food_func(self):

        name = self.entries["name"].get()
        calories = float(self.entries["calories"].get())
        protein = float(self.entries["protein"].get())
        fat = float(self.entries["fat"].get())
        carbs = float(self.entries["carbs"].get())
        print(f"{name} added")
        # button_info = (id_number, name, calories, protein, fat, carbs)
        new_food = Food(name, calories, protein, fat, carbs)
        new_food.add_food()

        # button = Button(self.pick_menu,
        #                 text=f"{name}",
        #                 font=("Comic sans MS", 20, "bold"),
        #                 bg="#6e8b3d",
        #                 activebackground="#51803e",
        #                 command=lambda x=button_info: self.initial_button_load(x),
        #                 height=1,
        #                 width=3,
        #                 )
        #
        # self.pick_menu.buttons.append(button)
        self.entries["id"].delete(0, END)
        self.entries["name"].delete(0, END)
        self.entries["calories"].delete(0, END)
        self.entries["protein"].delete(0, END)
        self.entries["fat"].delete(0, END)
        self.entries["carbs"].delete(0, END)

    def get_food_vals(self):
        food = self.entries["name"].get()
        food_data = get_food_values(food)

        self.entries["calories"].delete(0, END)
        self.entries["calories"].insert(0, food_data["calories"])

        self.entries["protein"].delete(0, END)
        self.entries["protein"].insert(0, food_data["protein_g"])

        self.entries["fat"].delete(0, END)
        self.entries["fat"].insert(0, food_data["fat_total_g"])

        self.entries["carbs"].delete(0, END)
        self.entries["carbs"].insert(0, food_data["carbohydrates_total_g"])

    def back_to_menu_func(self):
        main_menu = self.welcome_menu()
        main_menu.welcome_menu_func()

    def button_creation(self):
        buttons = {}

        get_food_values_from_API = Button(self.frame,
                                          text="Get values",
                                          font=("Comic sans MS", 20, "bold"),
                                          bg="#6e8b3d",
                                          activebackground="#51803e",
                                          command=self.get_food_vals,
                                          height=1,
                                          width=10
                                          )
        buttons["get_food_val"] = get_food_values_from_API
        add_food = Button(self.frame,
                          text="Add food",
                          font=("Comic sans MS", 20, "bold"),
                          bg="#6e8b3d",
                          activebackground="#51803e",
                          command=self.add_food_func,
                          height=1,
                          width=10
                          )
        buttons["add_food"] = add_food
        show_fast_food = Button(self.frame,
                                text="Show\nfast food",
                                font=("Comic sans MS", 20, "bold"),
                                bg="#6e8b3d",
                                activebackground="#51803e",
                                command=self.show_fast_food_func,
                                height=1,
                                width=10
                                )
        buttons["show_fast_food"] = show_fast_food
        back_to_menu = Button(self.frame,
                              text="Back to\nmain menu",
                              font=("Comic sans MS", 20, "bold"),
                              bg="#6e8b3d",
                              activebackground="#51803e",
                              command=self.back_to_menu_func,
                              relief=RAISED,
                              height=1,
                              width=10
                              )
        buttons["back_to_menu"] = back_to_menu
        return buttons

    def placement(self):
        # WELLCOME LABEL

        self.labels["search"].place(x=5, y=10)
        # NAME
        self.labels["name"].place(x=30, y=180)
        self.entries["name"].place(x=30, y=200)
        # CALORIES
        self.labels["calories"].place(x=30, y=230)
        self.entries["calories"].place(x=30, y=250)
        # PROTEIN
        self.labels["protein"].place(x=30, y=280)
        self.entries["protein"].place(x=30, y=300)
        # FAT
        self.labels["fat"].place(x=30, y=330)
        self.entries["fat"].place(x=30, y=350)
        # CARBS
        self.labels["carbs"].place(x=30, y=380)
        self.entries["carbs"].place(x=30, y=400)

        # BUTTONS PLACE
        self.buttons["get_food_val"].place(x=300, y=60)
        self.buttons["add_food"].place(x=300, y=150)
        self.buttons["show_fast_food"].place(x=300, y=250)
        self.buttons["back_to_menu"].place(x=300, y=350)
