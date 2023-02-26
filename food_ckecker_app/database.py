import sqlite3

create_fast_food_table = "CREATE TABLE IF NOT EXISTS fast_foods(in_number INTEGER, name TEXT," \
                   " calories INTEGER, protein INTEGER, fat INTEGER, carbs INTEGER)"
create_daily_table = "CREATE TABLE IF NOT EXISTS daily_intake(in_number INTEGER, name TEXT," \
                   " calories INTEGER, protein INTEGER, fat INTEGER, carbs INTEGER)"
try_insert = "INSERT INTO fast_foods VALUES" \
             " (1, 'Hesburger', 400, 35, 46, 85)," \
             " (2, 'Pizza', 700, 40, 35, 80)," \
             " (3, 'Chinese', 600, 50, 60, 35) "
try_select = "SELECT * FROM fast_foods"


connection = sqlite3.connect("food.db")
cursor = connection.cursor()
cursor.execute(create_fast_food_table)
cursor.execute(create_daily_table)


class Food:
    def __init__(self, id_number=-1, name="", cal=0, protein=0, fat=0, carbs=0,):
        self.id_number = id_number
        self.name = name
        self.cal = cal
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.connection = sqlite3.connect("food.db")
        self.cursor = self.connection.cursor()

    def show_food(self, id_number):
        self.cursor.execute("SELECT FROM fast_foods WHERE in_number = {}".format(id_number))
        result = self.cursor.fetchone()
        self.id_number = id_number
        self.name = result[1]
        self.cal = result[2]
        self.protein = result[3]
        self.fat = result[4]
        self.carbs = result[5]

    def add_food(self):
        self.cursor.execute("INSERT INTO fast_foods VALUES ({}, '{}', {}, {}, {}, {})".
                            format(self.id_number, self.name, self.cal, self.protein, self.fat, self.carbs))
        self.connection.commit()
        # self.connection.close()



