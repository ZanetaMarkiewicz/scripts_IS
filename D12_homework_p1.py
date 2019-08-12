# zadanie polega na zamknięciu poniższego kodu w klasę np. RecipesGenerator
# oraz stworzeniu metody pozwalającej na wygenerowanie przepisów z użyciem podanych przez uzytkownika skladnikow
# (ingredients) - nalezy uzyc api dostepnego ponizej do generowania przepisow
# dokumentacja do API http://www.recipepuppy.com/about/api/
# (wystarczy uzyc jednego parametru 'i' (ingredients))
# nalezy spojrzec na przykladowe przepisy aby zobaczyc jakie skladniki wystepuja w przepisach
# wskazówki: najlepiej uzyc dwoch plikow - w jednym kod klasy, w drugim import oraz uzycie oraz cały workflow programu

import requests
# import json
# http://www.recipepuppy.com/api/


class RecipesGenerator(object):
    response = requests.get('http://www.recipepuppy.com/api/', params={'i': 'onions,garlic', 'q': 'omelet', 'p': '1'})
    print(response.status_code)
    recipes = response.json()['results']

    user_input = input("Enter ingredients: ")
    user_input_l = user_input.split(" ")

    recipes_l = []

    for recipe in recipes:
        print(recipe)
        recipe['ingredients'] = (recipe['ingredients']).split(", ")
        # print(recipe['title'])
        for i in user_input_l:
            if i in recipe['ingredients']:
                # przerobic tak aby w kolejnym loopie sprawdzal tylko te listy ktore zawieraja pierwszy skladnik
                recipes_l.append(recipe['title'])
    print(recipes_l)



