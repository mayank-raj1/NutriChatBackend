import json
from typing import List

from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-pro")

sampleRecipe = '''
{
"name": "Teriyaki Tofu Stir-Fry",
"category": "Main Dish",
"ingredients": [
  "1 block tofu, pressed and cubed",
  "2 tbsp sesame oil",
  "Assorted vegetables (broccoli, bell peppers, snap peas)",
  "1/4 cup soy sauce",
  "2 tbsp rice vinegar",
  "2 tbsp honey",
  "2 cloves garlic, minced",
  "1 tsp ginger, grated",
  "Cooked rice or noodles",
  "Sliced green onions",
  "Sesame seeds"
],
"steps": [
  "1. Press tofu to remove excess moisture, then cut into cubes.",
  "2. Heat sesame oil in a large skillet or wok over medium-high heat.",
  "3. Add cubed tofu and cook until golden brown on all sides.",
  "4. Push tofu to one side of the skillet and add chopped vegetables. Cook until tender-crisp.",
  "5. In a small bowl, mix together soy sauce, rice vinegar, honey, garlic, and ginger. Pour over tofu and vegetables.",
  "6. Cook for another 2-3 minutes until sauce has thickened and coated tofu and vegetables.",
  "7. Serve over cooked rice or noodles. Garnish with sliced green onions and sesame seeds."
],
"tags": ["Asian", "Vegan", "Stir-Fry"]
}
'''

def get_recipe_names(user_data):
    output_parser_user = JsonOutputParser()
    template = ChatPromptTemplate.from_template(
        'For this user, suggest 15 recipes. Only output names in JSON format such as this: ["sandwich", "pizza", "salad"]. Here is the user:  {user}')
    recommendation_chain = template | llm | output_parser_user
    return recommendation_chain.invoke({"user": user_data})

def get_recipe(recipe):
    output_parser_recipe = JsonOutputParser()
    template_recipe_response = ChatPromptTemplate.from_template(
        "Please provide the recipe details for this recipe: {recipe} in this JSON format: {sampleRecipe}"
    )
    recipe_chain = template_recipe_response | llm | output_parser_recipe
    return recipe_chain.invoke({"recipe": recipe, "sampleRecipe": sampleRecipe})

def generate_recipe(user_data):
    recipes_name_list = get_recipe_names(user_data)
    recipes = []
    for recipe in recipes_name_list:
        try:
            recipes.append(get_recipe(recipe))
        except Exception as e:
            continue

    return recipes
