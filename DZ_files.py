recipes = []
with open('recipes.txt', encoding='utf-8') as rec_fail:
    for text in rec_fail:
        dish_name = text.strip()
        dish = {'name': dish_name, 'ingredients': []}
        ingredients_count = rec_fail.readline()
        for ing in range(int(ingredients_count)):
            ingredients = rec_fail.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish['ingredients'].append({'ingredient_name': name, 'quantity': quantity, 'measure': measure})
        blank_line = rec_fail.readline()
        recipes.append(dish)
def get_shop_list_by_dishes(dishes, person_count):
    purchases = {}
    for dish in dishes:
        for dish_book in recipes:
            if dish_book['name'] == dish:
                for ing in dish_book['ingredients']:
                    if ing['ingredient_name'] not in purchases.keys():
                        measure = ing['measure']
                        quantity = person_count * int(ing['quantity'])
                        purchases[ing['ingredient_name']] = {'measure': measure, 'quantity': quantity}

                    elif ing['ingredient_name'] in purchases.keys():
                        measure = ing['measure']
                        quantity = person_count * int(ing['quantity']) + int((purchases[ing['ingredient_name']])['quantity'])
                        purchases[ing['ingredient_name']] = {'measure': measure, 'quantity': quantity}
    return purchases
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
