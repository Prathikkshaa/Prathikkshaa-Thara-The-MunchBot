import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize NLTK
nltk.download("punkt")
nltk.download("wordnet")

# Sample ingredients (you can add more)
sample_ingredients = [
    "chicken",
    "rice",
    "tomato",
    "onion",
    "garlic",
    "ginger",
    "bell pepper",
    "spinach",
    "potato",
    "carrot",
    "Rice",
    "Lentils (Dal)",
    "Wheat flour (Atta)",
    "Gram flour (Besan)",
    "Mustard oil",
    "Ghee (Clarified butter)",
    "Turmeric powder",
    "Red chili powder",
    "Cumin seeds (Jeera)",
    "Coriander powder",
    "Garam masala",
    "Cardamom",
    "Cinnamon",
    "Cloves",
    "Bay leaves",
    "Asafoetida (Hing)",
    "Ginger",
    "Garlic",
    "Green chili",
    "Onion",
    "Tomato",
    "Potatoes",
    "Cauliflower",
    "Spinach",
    "Eggplant (Brinjal)",
    "Okra (Bhindi)",
    "Bell peppers",
    "Cilantro (Coriander leaves)",
    "Mint leaves",
    "Curry leaves",
    "Lemon",
    "Yogurt",
    "Paneer (Indian cottage cheese)",
    "Milk",
    "Coconut milk",
    "Tamarind",
    "Jaggery (Gur)",
    "Sugar",
    "Salt",
    "Black pepper",
    "Fenugreek seeds (Methi)",
    "Poppy seeds (Khus khus)",
    "Sesame seeds (Til)",
    "Cashews",
    "Almonds",
    "Pistachios",
    "Raisins",
    "Desiccated coconut",
    "Fresh coconut",
    "Mustard seeds",
    "Curry powder",
    "Mango powder (Amchur)",
    "Coconut oil",
    "Sunflower oil",
    "Almond oil",
    "Vinegar",
    "Red lentils (Masoor dal)",
    "Chickpeas (Chana dal)",
    "Black lentils (Urad dal)",
    "Split pigeon peas (Toor dal)",
    "Kidney beans (Rajma)",
    "Black gram (Sabut urad dal)",
    "Semolina (Sooji/Rava)",
    "Basmati rice",
    "Saffron",
    "Rose water",
    "Wheat noodles (Seviyan)",
    "Vermicelli",
    "Indian pickles (Achaar)",
    "Green mangoes",
    
]

# Lemmatize the ingredients
lemmatizer = WordNetLemmatizer()
lemmatized_ingredients = [lemmatizer.lemmatize(ingredient) for ingredient in sample_ingredients]

# Sample recipe data (you can add more)
recipes = {
    "Chicken Curry": ["chicken", "onion", "garlic", "ginger", "tomato", "green chili", "garam masala", "turmeric powder", "red chili powder", "coriander powder", "cumin seeds", "bay leaves", "curry leaves", "salt", "oil", "water"],
    "Vegetable Fried Rice": ["rice", "onion", "garlic", "ginger", "bell peppers", "carrot", "green peas", "green chili", "soy sauce", "salt", "oil"],
    "Paneer Tikka": ["paneer", "bell peppers", "onion", "yogurt", "ginger-garlic paste", "garam masala", "turmeric powder", "red chili powder", "cumin powder", "coriander powder", "lemon juice", "kasuri methi", "salt", "oil"],
    "Aloo Gobi": ["potatoes", "cauliflower", "onion", "tomato", "ginger", "garlic", "green chili", "turmeric powder", "red chili powder", "coriander powder", "cumin seeds", "garam masala", "salt", "oil", "water"],
    "Dal Tadka": ["yellow lentils", "onion", "tomato", "ginger", "garlic", "green chili", "cumin seeds", "mustard seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "asafoetida", "salt", "oil", "water"],
    "Palak Paneer": ["spinach", "paneer", "onion", "tomato", "ginger", "garlic", "green chili", "cumin seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "cream", "salt", "butter"],
    "Vegetable Biryani": ["basmati rice", "mixed vegetables", "onion", "tomato", "ginger", "garlic", "green chili", "cumin seeds", "bay leaves", "cinnamon", "cloves", "cardamom", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "salt", "oil", "water"],
    "Chana Masala": ["chickpeas", "onion", "tomato", "ginger", "garlic", "green chili", "cumin seeds", "coriander seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "amchur powder", "asafoetida", "salt", "oil", "water"],
    "Aloo Paratha": ["whole wheat flour", "potatoes", "onion", "green chili", "coriander leaves", "cumin seeds", "garam masala", "salt", "oil", "butter"],
    "Matar Paneer": ["paneer", "green peas", "onion", "tomato", "ginger", "garlic", "green chili", "cumin seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "salt", "oil", "water"],
    "Mango Lassi": ["mango", "yogurt", "sugar", "cardamom powder", "ice cubes"],
    "Pav Bhaji": ["potatoes", "mixed vegetables", "onion", "tomato", "ginger", "garlic", "green chili", "pav bhaji masala", "butter", "lemon", "coriander leaves", "pav (bread rolls)"],
    "Rasgulla": ["milk", "lemon juice", "sugar", "water", "cardamom", "rose water"],
    "Chicken Biryani": ["chicken pieces", "basmati rice", "onion", "tomato", "yogurt", "mint leaves", "cilantro leaves", "ginger-garlic paste", "green chili", "cumin seeds", "bay leaves", "cinnamon", "cloves", "cardamom", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "salt", "oil", "water"],
    "Vegetable Pulao": ["basmati rice", "mixed vegetables", "onion", "ginger", "garlic", "green chili", "cumin seeds", "bay leaves", "cinnamon", "cloves", "cardamom", "turmeric powder", "garam masala", "salt", "oil", "water"],
    "Chicken Korma": ["chicken pieces", "onion", "tomato", "cashews", "ginger", "garlic", "green chili", "yogurt", "garam masala", "turmeric powder", "red chili powder", "coriander powder", "cumin powder", "kasuri methi", "cream", "oil"],
    "Gajar Halwa": ["carrots", "milk", "sugar", "ghee", "cardamom", "cashews", "raisins"],
    "Masoor Dal": ["red lentils", "onion", "tomato", "ginger", "garlic", "green chili", "cumin seeds", "mustard seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "asafoetida", "salt", "oil", "water"],
    "Poha": ["flattened rice", "onion", "potato", "peanut", "green chili", "curry leaves", "mustard seeds", "turmeric powder", "lemon", "coriander leaves", "salt", "oil"],
    "Malai Kofta": ["paneer", "potato", "cashews", "ginger", "garlic", "green chili", "onion", "tomato", "cream", "garam masala", "turmeric powder", "red chili powder", "coriander powder", "salt", "oil", "water", "fresh cilantro"],
    "Idli": ["rice", "urad dal", "fenugreek seeds", "salt"],
    "Masala Dosa": ["rice", "split black lentils (urad dal)", "fenugreek seeds", "potato", "onion", "green chili", "ginger", "mustard seeds", "curry leaves", "turmeric powder", "oil", "salt"],
    "Rava Upma": ["semolina (sooji/rava)", "onion", "green chili", "ginger", "curry leaves", "mustard seeds", "urad dal", "chana dal", "cashews", "water", "salt"],
    "Sambar": ["toor dal", "vegetables (such as drumsticks, carrots, potatoes, eggplant, pumpkin)", "sambar powder", "tamarind", "onion", "tomato", "green chili", "mustard seeds", "curry leaves", "fenugreek seeds", "coriander leaves", "oil", "salt"],
    "Rasam": ["tomato", "tamarind", "garlic", "green chili", "curry leaves", "mustard seeds", "cumin seeds", "fenugreek seeds", "turmeric powder", "black pepper", "coriander leaves", "oil", "salt"],
    "Medu Vada": ["split black lentils (urad dal)", "ginger", "green chili", "curry leaves", "onion", "cumin seeds", "black pepper", "coriander leaves", "oil", "salt"],
    "Pongal": ["rice", "split yellow lentils (moong dal)", "ginger", "black pepper", "cumin seeds", "cashews", "curry leaves", "ghee", "salt"],
    "Coconut Chutney": ["coconut", "green chili", "ginger", "curry leaves", "mustard seeds", "urad dal", "chana dal", "tamarind", "coriander leaves", "salt"],
    "Idiyappam": ["rice flour", "water", "salt", "coconut", "sugar"],
    "Appam": ["rice", "coconut", "yeast", "sugar", "salt"],
    "Vada Curry": ["medu vada", "onion", "tomato", "ginger-garlic paste", "coriander powder", "red chili powder", "turmeric powder", "garam masala", "coconut milk", "coriander leaves", "oil", "salt"],
    "Avial": ["mixed vegetables (such as carrots, beans, potatoes, drumsticks, pumpkin)", "coconut", "curd", "green chili", "curry leaves", "cumin seeds", "mustard seeds", "turmeric powder", "coconut oil", "salt"],
    "Kootu": ["yellow lentils (toor dal)", "mixed vegetables (such as ash gourd, pumpkin, beans, carrots)", "coconut", "green chili", "cumin seeds", "mustard seeds", "turmeric powder", "curry leaves", "coconut oil", "salt"],
    "Thakkali Sadam (Tomato Rice)": ["rice", "tomato", "onion", "ginger", "garlic", "green chili", "curry leaves", "mustard seeds", "cumin seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "coriander leaves", "oil", "salt"],
    "Bisi Bele Bath": ["rice", "toor dal", "mixed vegetables (such as carrots, beans, peas, potatoes, capsicum)", "tamarind", "onion", "tomato", "ginger", "garlic", "green chili", "curry leaves", "mustard seeds", "cumin seeds", "turmeric powder", "red chili powder", "coriander powder", "garam masala", "coconut", "coriander leaves", "oil", "salt"],
    "Pesarattu": ["green gram (whole moong dal)", "rice", "ginger", "green chili", "cumin seeds", "black pepper", "onion", "coriander leaves", "oil", "salt"],
    "Curry Leaves Rice": ["rice", "curry leaves", "ginger", "green chili", "mustard seeds", "urad dal", "chana dal", "cashews", "grated coconut", "lemon juice", "oil", "salt"],
    "Kerala Style Fish Curry": ["fish", "coconut", "ginger", "garlic", "green chili", "shallots", "curry leaves", "turmeric powder", "red chili powder", "coriander powder", "tamarind", "coconut oil", "salt"],
    "Kerala Parotta": ["all-purpose flour", "water", "salt", "oil"],
    "Kuzhi Paniyaram": ["rice", "black gram (urad dal)", "fenugreek seeds", "leftover dosa batter", "onion", "green chili", "curry leaves", "mustard seeds", "oil", "salt"],
    "Ada Pradhaman": ["ada (rice flakes)", "coconut milk", "jaggery", "cashews", "raisins", "ghee", "cardamom"],
    "Potato Curry": ["potato", "onion", "garlic", "ginger", "tomato"],
    "Butter Chicken": ["chicken", "butter", "onion", "garlic", "ginger", "tomato", "cream", "chili powder", "coriander powder", "garam masala", "kasuri methi", "cashew nuts"],
    "Paneer Butter Masala": ["paneer", "butter", "onion", "garlic", "ginger", "tomato", "cream", "chili powder", "coriander powder", "garam masala", "kasuri methi", "cashew nuts"],
    "Biryani": ["rice", "chicken", "onion", "yogurt", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "saffron", "mint leaves", "coriander leaves"],
    "Samosa": ["potato", "peas", "onion", "ginger", "garlic", "chili powder", "garam masala", "coriander leaves", "cumin seeds"],
    "Dosa": ["rice", "split black lentils", "fenugreek seeds"],
    "Idli": ["rice", "split black lentils"],
    "Raita": ["yogurt", "cucumber", "tomato", "onion", "coriander leaves", "cumin powder"],
    "Chole Bhature": ["chickpeas", "flour", "yogurt", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Aloo Tikki": ["potato", "peas", "onion", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Rasgulla": ["milk", "sugar", "lemon juice"],
    "Gulab Jamun": ["milk powder", "flour", "cream", "sugar", "ghee"],
    "Jalebi": ["flour", "yogurt", "sugar", "saffron", "cardamom"],
    "Pani Puri": ["semolina", "flour", "potato", "onion", "chickpeas", "tamarind", "chili powder", "coriander powder"],
    "Vada Pav": ["potato", "flour", "onion", "green chili", "coriander leaves", "garlic", "ginger"],
    "Rajma Chawal": ["kidney beans", "rice", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Dhokla": ["gram flour", "semolina", "yogurt", "green chili", "ginger", "mustard seeds", "curry leaves"],
    "Kachori": ["flour", "moong dal", "onion", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Pav Bhaji": ["mixed vegetables", "butter", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "bun"],
    "Mutton Curry": ["mutton", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "curry leaves"],
    "Chicken Biryani": ["rice", "chicken", "onion", "yogurt", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "saffron", "mint leaves", "coriander leaves"],
    "Pulao": ["rice", "vegetables", "onion", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "mint leaves", "coriander leaves"],
    "Malai Kofta": ["paneer", "potato", "cashew nuts", "onion", "ginger", "garlic", "cream", "chili powder", "coriander powder", "garam masala"],
    "Aloo Paratha": ["whole wheat flour", "potato", "onion", "ginger", "chili powder", "coriander leaves", "ghee"],
    "Gobi Manchurian": ["cauliflower", "flour", "ginger", "garlic", "chili powder", "soy sauce", "tomato ketchup"],
    "Matar Paneer": ["paneer", "green peas", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Masala Chai": ["tea leaves", "milk", "water", "sugar", "cardamom"],
    "Aloo Gobi": ["potato", "cauliflower", "onion", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Palak Paneer": ["paneer", "spinach", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Chicken Tikka": ["chicken", "yogurt", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "lemon juice"],
    "Dahi Vada": ["split black lentils", "yogurt", "ginger", "green chili", "tamarind", "coriander leaves"],
    "Chicken 65": ["chicken", "yogurt", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "curry leaves"],
    "Gajar Ka Halwa": ["carrots", "milk", "sugar", "ghee", "cardamom", "cashew nuts", "raisins"],
    "Rava Upma": ["semolina", "onion", "ginger", "green chili", "mustard seeds", "curry leaves"],
    "Rajma": ["kidney beans", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Pav Bhaji": ["mixed vegetables", "butter", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala", "bun"],
    "Kadhi Pakora": ["yogurt", "gram flour", "onion", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Aloo Matar": ["potato", "green peas", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Bhindi Masala": ["okra", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Chana Masala": ["chickpeas", "onion", "tomato", "ginger", "garlic", "chili powder", "coriander powder", "garam masala"],
    "Chicken Curry": ["chicken", "onion", "garlic", "ginger", "tomato", "bell pepper"],
    "Vegetable Fried Rice": ["rice", "onion", "garlic", "ginger", "bell pepper", "carrot"],
    "Spaghetti Carbonara": ["spaghetti", "pancetta", "egg", "Parmesan cheese", "black pepper", "garlic"],
    "Margherita Pizza": ["pizza dough", "tomato sauce", "mozzarella cheese", "fresh basil", "olive oil"],
    "Lasagna": ["lasagna noodles", "ground beef", "tomato sauce", "ricotta cheese", "mozzarella cheese", "Parmesan cheese", "onion", "garlic"],
    "Risotto": ["Arborio rice", "chicken broth", "Parmesan cheese", "butter", "onion", "garlic", "white wine"],
    "Tiramisu": ["ladyfingers", "mascarpone cheese", "eggs", "sugar", "espresso", "cocoa powder"],
    "Bruschetta": ["baguette", "tomato", "garlic", "basil", "olive oil", "balsamic vinegar"],
    "Caprese Salad": ["tomato", "mozzarella cheese", "fresh basil", "olive oil", "balsamic vinegar", "salt", "black pepper"],
    "Pasta Alfredo": ["fettuccine pasta", "heavy cream", "butter", "Parmesan cheese", "garlic", "black pepper", "parsley"],
    "Minestrone Soup": ["vegetable broth", "cannellini beans", "carrot", "celery", "zucchini", "onion", "garlic", "tomato", "pasta", "spinach"],
    "Ravioli": ["ravioli pasta", "ricotta cheese", "Parmesan cheese", "egg", "nutmeg", "salt", "black pepper"],
    "Pesto Pasta": ["spaghetti", "basil pesto", "Parmesan cheese", "olive oil", "pine nuts", "garlic"],
    "Margherita Flatbread": ["flatbread", "tomato sauce", "mozzarella cheese", "fresh basil", "olive oil"],
    "Sushi": ["sushi rice", "nori (seaweed)", "fish (such as tuna, salmon)", "avocado", "cucumber", "wasabi", "soy sauce", "pickled ginger"],
    "Pad Thai": ["rice noodles", "shrimp", "tofu", "bean sprouts", "eggs", "garlic chives", "peanuts", "lime", "soy sauce", "tamarind paste"],
    "Hamburger": ["ground beef", "hamburger bun", "lettuce", "tomato", "onion", "pickle", "cheese", "ketchup", "mustard", "mayonnaise"],
    "Peking Duck": ["duck", "hoisin sauce", "cucumber", "scallion", "pancakes"],
    "Miso Soup": ["dashi (fish stock)", "miso paste", "tofu", "seaweed", "green onion"],
    "Pasta Carbonara": ["spaghetti", "pancetta", "egg", "Parmesan cheese", "black pepper"],
    "Paella": ["rice", "chicken", "chorizo", "shrimp", "mussels", "bell pepper", "onion", "tomato", "saffron", "garlic", "olive oil"],
    "Gyoza": ["ground pork", "cabbage", "garlic", "ginger", "green onion", "soy sauce", "sesame oil", "wrapper"],
    "Pho": ["rice noodles", "beef (or chicken)", "onion", "ginger", "star anise", "cinnamon", "cloves", "bean sprouts", "lime", "Thai basil", "hoisin sauce", "sriracha"],
    "Falafel": ["chickpeas", "onion", "garlic", "parsley", "cilantro", "cumin", "coriander", "flour", "baking powder", "salt", "pepper", "pita bread", "tahini sauce"],
    "Tacos": ["tortillas", "ground beef (or chicken)", "lettuce", "tomato", "onion", "cheese", "salsa", "guacamole", "sour cream"],
    "Samosa": ["potatoes", "peas", "onion", "ginger", "garlic", "turmeric", "cumin", "coriander", "garam masala", "chili powder", "coriander leaves", "mint leaves", "pastry dough"],
    "Croissant": ["all-purpose flour", "butter", "milk", "sugar", "yeast", "salt", "egg"],
    "Schnitzel": ["veal (or chicken)", "breadcrumbs", "flour", "egg", "lemon", "parsley", "butter"],
    "Tom Yum Goong": ["shrimp", "lemongrass", "galangal", "kaffir lime leaves", "chili", "fish sauce", "lime juice", "mushroom", "coriander"],
    "Pierogi": ["potatoes", "cheddar cheese", "onion", "bacon", "sour cream", "flour", "egg", "butter"],
    "Moussaka": ["eggplant", "ground lamb", "onion", "garlic", "tomato", "cinnamon", "oregano", "bechamel sauce", "Parmesan cheese"],
    "Goulash": ["beef", "onion", "bell pepper", "potatoes", "tomato", "paprika", "caraway seeds"],
    "Baklava": ["phyllo dough", "walnuts", "almonds", "cinnamon", "sugar", "honey", "butter"],
    "Jollof Rice": ["rice", "tomato", "onion", "bell pepper", "scotch bonnet pepper", "ginger", "garlic", "thyme", "bay leaves", "stock cube", "vegetable oil"],
    "Pavlova": ["egg whites", "sugar", "cornstarch", "white vinegar", "whipped cream", "fruit (such as berries, kiwi)"],
    "Laksa": ["rice noodles", "coconut milk", "shrimp", "fish cake", "tofu puffs", "bean sprouts", "hard-boiled egg", "curry paste", "chili"],
    "Sauerbraten": ["beef", "onion", "carrot", "celery", "vinegar", "water", "ginger", "cloves", "bay leaves", "sugar", "flour", "butter"],
    "Poutine": ["fries", "cheese curds", "gravy"],
    "Kebab": ["meat (such as lamb, beef, chicken)", "onion", "bell pepper", "tomato", "cucumber", "pita bread", "tzatziki sauce"],
    "Shepherd's Pie": ["ground beef (or lamb)", "onion", "carrot", "peas", "tomato paste", "beef broth", "mashed potatoes", "butter"],
    "Ceviche": ["fish (such as tilapia, snapper)", "lime juice", "lemon juice", "orange juice", "onion", "tomato", "cilantro", "avocado", "jalapeno"],
    "Moules Frites": ["mussels", "white wine", "shallots", "garlic", "butter", "parsley", "fries"],
    "Baklava": ["phyllo dough", "walnuts", "almonds", "cinnamon", "sugar", "honey", "butter"],
    "Chicken Adobo": ["chicken thighs", "soy sauce", "vinegar", "garlic", "bay leaves", "black peppercorns"],

}

def find_matching_recipes(ingredients):
    matching_recipes = []
    for recipe, recipe_ingredients in recipes.items():
        if sum(ingredient in recipe_ingredients for ingredient in ingredients) >= 2:
            matching_recipes.append(recipe)
    return matching_recipes

def find_ingredients_for_recipe(recipe_name):
    recipe_name_lower = recipe_name.lower()
    for recipe, recipe_ingredients in recipes.items():
        if recipe_name_lower == recipe.lower():
            return f"Ingredients for {recipe}:\n{', '.join(recipe_ingredients)}"
    return "We are currently checking that out."

def chatbot_response(user_input, mode):
    tokens = word_tokenize(user_input.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    if mode == "ingredients_for_recipe":
        recipe_name = ' '.join(lemmatized_tokens)
        return find_ingredients_for_recipe(recipe_name)

    matching_ingredients = [ingredient for ingredient in lemmatized_tokens if ingredient in lemmatized_ingredients]

    if not matching_ingredients:
        return "I'm sorry, I couldn't find any matching ingredients."

    matching_recipes = find_matching_recipes(matching_ingredients)

    if matching_recipes:
        recipes_list = "\n".join(matching_recipes)  # Join recipes with newline characters
        return f"Here are some recipes you can make with {', '.join(matching_ingredients)}:\n{recipes_list}"
    else:
        return "I found matching ingredients, but no specific recipes. Try a different combination!"

while True:
    # Get user input for mode selection
    mode_input = input("Choose mode:\n1. Recipes for your ingredients\n2. Ingredients for your recipe\nEnter your choice (1 or 2): ")

    if mode_input == "1":
        user_input = input("Enter the ingredients you have (comma-separated): ")
        mode = "recipes_based_on_ingredients"
    elif mode_input == "2":
        user_input = input("Enter the name of the recipe: ")
        mode = "ingredients_for_recipe"
    else:
        print("Invalid choice. Exiting.")
        break

    # Get chatbot response
    response = chatbot_response(user_input, mode)
    print(response)

    # Ask the user if they want to continue
    continue_input = input("Do you want to continue? (yes/no): ")
    if continue_input.lower() != "yes":
        break


def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    matching_ingredients = [ingredient for ingredient in lemmatized_tokens if ingredient in lemmatized_ingredients]

    if not matching_ingredients:
        return "I'm sorry, I couldn't find any matching ingredients."

    # Check if user is asking for ingredients for a specific recipe
    if "for" in lemmatized_tokens and "recipe" in lemmatized_tokens:
        recipe_index = lemmatized_tokens.index("for")
        recipe_name = ' '.join(lemmatized_tokens[recipe_index+1:])
        return find_ingredients_for_recipe(recipe_name)

    matching_recipes = find_matching_recipes(matching_ingredients)

    if matching_recipes:
        recipes_list = "\n".join(matching_recipes)  # Join recipes with newline characters
        return f"Here are some recipes you can make with {', '.join(matching_ingredients)}:\n{recipes_list}"
    else:
        return "I found matching ingredients, but no specific recipes. Try a different combination!"

# Get user input
user_input = input("Enter your query: ")

# Get chatbot response
response = chatbot_response(user_input)
print(response)

# Get user input for ingredients
user_input = input("Enter the ingredients you have (comma-separated): ")

# Get chatbot response
response = chatbot_response(user_input)
print(response)

# Get user input for ingredients
user_input = input("Enter the ingredients you have (comma-separated): ")

# Get chatbot response
response = chatbot_response(user_input)
print(response)