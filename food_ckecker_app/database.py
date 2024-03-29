import sqlite3

create_fast_food_table = "CREATE TABLE IF NOT EXISTS fast_foods(id_number INTEGER, name TEXT," \
                         " calories INTEGER, protein INTEGER, fat INTEGER, carbs INTEGER)"

create_daily_table = "CREATE TABLE IF NOT EXISTS daily_intake(id_number INTEGER, name TEXT," \
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
    id_counter = 0

    def __init__(self, name="", cal=0, protein=0, fat=0, carbs=0, ):
        Food.id_counter += 1
        self.id_number = Food.id_counter
        self.name = name
        self.cal = cal
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.connection = sqlite3.connect("food.db")
        self.cursor = self.connection.cursor()

    def show_food(self, id_number):
        self.cursor.execute("SELECT FROM fast_foods WHERE id_number = {}".format(id_number))
        result = self.cursor.fetchone()
        self.id_number = id_number
        self.name = result[1]
        self.cal = result[2]
        self.protein = result[3]
        self.fat = result[4]
        self.carbs = result[5]

    def add_food(self):
        self.cursor.execute("INSERT INTO daily_intake VALUES ({}, '{}', {}, {}, {}, {})".
                            format(self.id_number, self.name, self.cal, self.protein, self.fat, self.carbs))
        self.connection.commit()
