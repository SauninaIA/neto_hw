from pprint import pprint

file = "cook_book.txt"


def catalog_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        result = {}
        for line in file_obj:
            meal = line.strip()
            quantity = file_obj.readline().strip()
            ingredients = []
            for item in range(int(quantity)):
                ingredient = file_obj.readline()
                ingredient = ingredient.split('|')
                ingredient_ = {}
                ingredient_['ingredient_name'] = ingredient[0].strip()
                ingredient_['quantity'] = ingredient[1].strip()
                ingredient_['measure'] = ingredient[2].strip()
                ingredients.append(ingredient_)

            result[meal] = ingredients
            file_obj.readline()
        return result


catalog = catalog_reader(file)
pprint(catalog)
print()
print()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in catalog:
            for ingredient in catalog[dish]:
                res = {}
                if ingredient['ingredient_name'] not in result:
                    res['measure'] = ingredient['measure']
                    res['quantity'] = int(ingredient['quantity']) * person_count
                    result[ingredient['ingredient_name']] = res
                else:
                    result[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return result


shopping_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(shopping_list)