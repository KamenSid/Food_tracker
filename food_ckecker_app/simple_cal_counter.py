from tkinter import *
from database import *
from vizualization import viz_info

# INITIAL SETUP
root = Tk()
root.geometry("520x500+550+300")
root.title("Food Tracker")
welcome_menu = Frame(root)
add_menu = Frame(root)
pick_menu = Frame(root)
buttons_list = []
cursor.execute("SELECT * FROM fast_foods")
fast_foods = cursor.fetchall()


def initial_button_load(args):

    cursor.execute("INSERT INTO daily_intake VALUES ({}, '{}', {}, {}, {}, {})".
                   format(args[0], args[1], args[2], args[3], args[4], args[5]))
    connection.commit()


for food in fast_foods:

    button = Button(pick_menu,
                    text=f"{food[1]}",
                    font=("Comic sans MS", 20, "bold"),
                    bg="#6e8b3d",
                    activebackground="#51803e",
                    command=lambda x=food: initial_button_load(x),
                    height=1,
                    width=3,
                    )
    buttons_list.append(button)


def welcome_menu_func():
    def exit_app():
        welcome_menu.quit()

    welcome_menu.pack(fill="both", expand=1)
    welcome_label = Label(welcome_menu,
                          text="Welcome to the Food Tracker",
                          font=("Comic sans MS", 20, "bold"),
                          fg="#9ab973"
                          )
    add_food_button = Button(welcome_menu,
                             text="Add food",
                             font=("Comic sans MS", 20, "bold"),
                             bg="#6e8b3d",
                             activebackground="#51803e",
                             height=2,
                             width=30,
                             command=add_menu_func,
                             )
    pick_menu_button = Button(welcome_menu,
                              text="Check list",
                              font=("Comic sans MS", 20, "bold"),
                              bg="#6e8b3d",
                              activebackground="#51803e",
                              height=2,
                              width=30,
                              command=pick_menu_func,
                              )
    viz_day_button = Button(welcome_menu,
                            text="Show day progress",
                            font=("Comic sans MS", 20, "bold"),
                            bg="#6e8b3d",
                            activebackground="#51803e",
                            height=2,
                            width=30,
                            command=viz_info,
                            relief=RAISED,
                            )
    exit_button = Button(welcome_menu,
                         text="EXIT",
                         font=("Comic sans MS", 20, "bold"),
                         bg="#6e8b3d",
                         activebackground="#51803e",
                         height=2,
                         width=30,
                         command=exit_app,
                         relief=RAISED,
                         )
    welcome_label.grid(row=0, column=1, columnspan=3)
    add_food_button.grid(row=1, column=2)
    pick_menu_button.grid(row=2, column=2)
    viz_day_button.grid(row=3, column=2)
    exit_button.grid(row=4, column=1, columnspan=3)

    welcome_menu.pack(fill="both", expand=1)


def add_menu_func():
    def show_fast_food_func():
        cursor.execute("SELECT * FROM fast_foods")
        fast_food_list = cursor.fetchall()
        print(fast_food_list)

    def add_food_func():
        id_number = int(id_entry.get())
        name = name_entry.get()
        calories = int(calories_entry.get())
        protein = int(protein_entry.get())
        fat = int(fat_entry.get())
        carbs = int(carbs_entry.get())
        print(f"{name} added")
        button_info = (id_number, name, calories, protein, fat, carbs)
        new_food = Food(id_number, name, calories, protein, fat, carbs)
        new_food.add_food()

        button = Button(pick_menu,
                        text=f"{name}",
                        font=("Comic sans MS", 20, "bold"),
                        bg="#6e8b3d",
                        activebackground="#51803e",
                        command=lambda x=button_info: initial_button_load(x),
                        height=1,
                        width=3,
                        )
        buttons_list.append(button)
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        calories_entry.delete(0, END)
        protein_entry.delete(0, END)
        fat_entry.delete(0, END)
        carbs_entry.delete(0, END)

    def back_to_menu_func():
        welcome_menu.pack(fill="both", expand=1)
        add_menu.pack_forget()

    # LABELS CREATION
    add_question = Label(add_menu,
                         text=f"Add new food to\nthe DATABASE",
                         font=("Comic sans MS", 30, "bold"),
                         fg="#9ab973"
                         )
    id_label = Label(add_menu,
                     text="Food ID:",
                     font=("Comic sans MS", 10, "bold"),
                     fg="#9ab973"
                     )
    name_label = Label(add_menu,
                       text="Food Name:",
                       font=("Comic sans MS", 10, "bold"),
                       fg="#9ab973"
                       )
    calories_label = Label(add_menu,
                           text="Calories count:",
                           font=("Comic sans MS", 10, "bold"),
                           fg="#9ab973"
                           )
    protein_label = Label(add_menu,
                          text="Protein amount:",
                          font=("Comic sans MS", 10, "bold"),
                          fg="#9ab973"
                          )
    fat_label = Label(add_menu,
                      text="Fat amount:",
                      font=("Comic sans MS", 10, "bold"),
                      fg="#9ab973"
                      )
    carbs_label = Label(add_menu,
                        text="Carbs amount:",
                        font=("Comic sans MS", 10, "bold"),
                        fg="#9ab973"
                        )
    # BUTTON CREATION
    add_food = Button(add_menu,
                      text="Add food",
                      font=("Comic sans MS", 20, "bold"),
                      bg="#6e8b3d",
                      activebackground="#51803e",
                      command=add_food_func,
                      height=1,
                      width=10
                      )
    show_fast_food = Button(add_menu,
                            text="Show\nfast food",
                            font=("Comic sans MS", 20, "bold"),
                            bg="#6e8b3d",
                            activebackground="#51803e",
                            command=show_fast_food_func,
                            height=1,
                            width=10
                            )
    back_to_menu = Button(add_menu,
                          text="Back to\nmain menu",
                          font=("Comic sans MS", 20, "bold"),
                          bg="#6e8b3d",
                          activebackground="#51803e",
                          command=back_to_menu_func,
                          relief=RAISED,
                          height=1,
                          width=10
                          )

    # ENTRY CREATION
    id_entry = Entry(add_menu,
                     font=("Comic sans MS", 15, "bold"),
                     )
    name_entry = Entry(add_menu,
                       font=("Comic sans MS", 15, "bold"),
                       )
    calories_entry = Entry(add_menu,
                           font=("Comic sans MS", 15, "bold"),
                           )
    protein_entry = Entry(add_menu,
                          font=("Comic sans MS", 15, "bold"),
                          )
    fat_entry = Entry(add_menu,
                      font=("Comic sans MS", 15, "bold"),
                      )
    carbs_entry = Entry(add_menu,
                        font=("Comic sans MS", 15, "bold"),
                        )
    # WELLCOME LABEL
    add_question.place(x=150, y=20)
    # ID
    id_label.place(x=30, y=130)
    id_entry.place(x=30, y=150)
    # NAME
    name_label.place(x=30, y=180)
    name_entry.place(x=30, y=200)
    # CALORIES
    calories_label.place(x=30, y=230)
    calories_entry.place(x=30, y=250)
    # PROTEIN
    protein_label.place(x=30, y=280)
    protein_entry.place(x=30, y=300)
    # FAT
    fat_label.place(x=30, y=330)
    fat_entry.place(x=30, y=350)
    # CARBS
    carbs_label.place(x=30, y=380)
    carbs_entry.place(x=30, y=400)
    # BUTTONS PLACE
    add_food.place(x=300, y=150)
    show_fast_food.place(x=300, y=250)
    back_to_menu.place(x=300, y=350)
    # SHOW FRAME
    add_menu.pack(fill="both", expand=1)
    welcome_menu.pack_forget()


def pick_menu_func():
    def show_daily_intake_func():
        cursor.execute("SELECT * FROM daily_intake")
        daily_intake_list = cursor.fetchall()
        print(daily_intake_list)

    def del_daly_intake():
        cursor.execute("DELETE FROM daily_intake")
        connection.commit()

    def del_fast_foods():
        cursor.execute("SELECT * FROM fast_foods")
        cursor.execute("DELETE FROM fast_foods")
        connection.commit()

    def back_to_menu_func():
        welcome_menu.pack(fill="both", expand=1)
        pick_menu.pack_forget()

    row = 0
    col = 0
    for butt in buttons_list:
        if col == 4:
            row += 1
            col = 0
        butt.grid(row=row, column=col)
        col += 1

    show_button = Button(pick_menu,
                         text="Show daily intake",
                         font=("Comic sans MS", 20, "bold"),
                         bg="#6e8b3d",
                         activebackground="#51803e",
                         command=show_daily_intake_func,
                         height=2,
                         width=30,

                         )
    delete_button = Button(pick_menu,
                           text="Delete Daly",
                           font=("Comic sans MS", 20, "bold"),
                           bg="#6e8b3d",
                           activebackground="#51803e",
                           command=del_daly_intake,
                           height=2,
                           width=30
                           )
    delete_fast_button = Button(pick_menu,
                           text="Delete Fast Foods",
                           font=("Comic sans MS", 20, "bold"),
                           bg="#6e8b3d",
                           activebackground="#51803e",
                           command=del_fast_foods,
                           height=2,
                           width=30
                           )
    back_button = Button(pick_menu,
                         text="Back to Main menu",
                         font=("Comic sans MS", 20, "bold"),
                         bg="#6e8b3d",
                         activebackground="#51803e",
                         command=back_to_menu_func,
                         height=2,
                         width=30
                         )
    show_button.grid(row=79, column=0, columnspan=4)
    delete_button.grid(row=81, column=0, columnspan=4)
    delete_fast_button.grid(row=80, column=0, columnspan=4)
    back_button.grid(row=99, column=0, columnspan=4)
    pick_menu.pack()
    welcome_menu.forget()


welcome_menu_func()
root.mainloop()
