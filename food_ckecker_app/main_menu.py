from add_menu import *
from pick_menu import *
from vizualization import *


class WelcomeMenu:
    __TITLE = "Food Tracker"
    __GEOMETRY = "520x500+550+300"
    ROOT = Tk()

    def __init__(self):

        self.title = self.ROOT.title(self.__TITLE)
        self.geometry = self.ROOT.geometry(self.__GEOMETRY)
        self.frame = Frame(self.ROOT)


    def exit_app(self):
        self.frame.quit()

    def add_menu(self):
        self.frame.pack_forget()
        add_menu = AddMenu(self.ROOT, self.pick_menu, WelcomeMenu)
        return add_menu.placement

    def pick_menu(self):
        self.frame.pack_forget()
        pick_menu = PickMenu(self.frame, WelcomeMenu)
        return pick_menu.placement

    def welcome_menu_func(self):

        self.frame.pack(fill="both", expand=1)
        welcome_label = Label(self.frame,
                              text="Welcome to the Food Tracker",
                              font=("Comic sans MS", 20, "bold"),
                              fg="#9ab973"
                              )
        add_food_button = Button(self.frame,
                                 text="Add food",
                                 font=("Comic sans MS", 20, "bold"),
                                 bg="#6e8b3d",
                                 activebackground="#51803e",
                                 height=2,
                                 width=30,
                                 command=self.add_menu,
                                 )
        pick_menu_button = Button(self.frame,
                                  text="Options",
                                  font=("Comic sans MS", 20, "bold"),
                                  bg="#6e8b3d",
                                  activebackground="#51803e",
                                  height=2,
                                  width=30,
                                  command=self.pick_menu,
                                  )
        viz_day_button = Button(self.frame,
                                text="Show day progress",
                                font=("Comic sans MS", 20, "bold"),
                                bg="#6e8b3d",
                                activebackground="#51803e",
                                height=2,
                                width=30,
                                command=viz_info,
                                relief=RAISED,
                                )
        exit_button = Button(self.frame,
                             text="EXIT",
                             font=("Comic sans MS", 20, "bold"),
                             bg="#6e8b3d",
                             activebackground="#51803e",
                             height=2,
                             width=30,
                             command=self.exit_app,
                             relief=RAISED,
                             )
        welcome_label.grid(row=0, column=1, columnspan=3)
        add_food_button.grid(row=1, column=2)
        pick_menu_button.grid(row=2, column=2)
        viz_day_button.grid(row=3, column=2)
        exit_button.grid(row=4, column=1, columnspan=3)

        self.frame.pack(fill="both", expand=1)
        self.ROOT.mainloop()


menu = WelcomeMenu()
menu.welcome_menu_func()

