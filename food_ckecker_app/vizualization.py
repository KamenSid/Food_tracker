import matplotlib.pyplot as plt
import numpy as np
from database import *

cal_goal = 3000
pro_goal = 180
fat_goal = 80
carbs_goal = 300


def viz_info():
    cursor.execute("SELECT * FROM daily_intake")
    consumed_food = cursor.fetchall()
    print(consumed_food)
    calories_sum = sum(food[2] for food in consumed_food)
    protein_sum = sum(food[3] for food in consumed_food)
    fat_sum = sum(food[3] for food in consumed_food)
    carbs_sum = sum(food[4] for food in consumed_food)
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].pie([protein_sum, fat_sum, carbs_sum], labels=["Proteins", "Fat", "Carbs"],
                  autopct=lambda p: f'{p:.2f}%')
    axs[0, 0].set_title("Distribution")
    axs[0, 1].bar(["Protein", "Fat", "Carbs"], [protein_sum, fat_sum, carbs_sum], width=0.4)
    axs[0, 1].bar([0.5, 1.5, 2.5], [pro_goal, fat_goal, cal_goal], width=0.4)
    axs[0, 1].set_title("Progress")
    axs[1, 0].pie([calories_sum, cal_goal - calories_sum], labels=["Calories", "Remaining"],
                  autopct=lambda p: f'{p:.2f}%')
    axs[1, 0].set_title("Calories goal progress")
    axs[1, 1].plot(list(range(len(consumed_food))), np.cumsum([food[2] for food in consumed_food]),
                   label="Calories eaten")
    axs[1, 1].plot(list(range(len(consumed_food))), [cal_goal] * len(consumed_food), label="Calories eaten")
    axs[1, 1].legend()
    axs[1, 1].set_title("Calories over time")
    fig.tight_layout()
    plt.show()
