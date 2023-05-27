import requests
# id_number, name, calories, protein, fat, carbs
food_values = {"calories": 0, "protein_g": 0, "fat_total_g": 0, "carbohydrates_total_g": 0}

def get_food_values(food):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    query = food
    response = requests.get(api_url + query, headers={'X-Api-Key': 'AY1jWxP7bRM2nTt24HrPHA==fAwzJSUyxVV7XM7a'})
    if response.status_code == requests.codes.ok:
        data = response.text.split(", ")
        for entry in data:
            for key in food_values.keys():
                if key in entry:
                    amount = [n for n in entry.split(":")[1] if n.isalnum() or n == "."]
                    amount = float("".join(amount))
                    food_values[key] = amount

        return food_values
    else:
        print("Error:", response.status_code, response.text)
