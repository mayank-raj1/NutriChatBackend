from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize ChatGoogleGenerativeAI instance with Gemini Pro model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Sample recipe JSON
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


# Function to get recipe names based on user data
def get_recipe_names(user_data):
    # Initialize output parser
    output_parser_user = JsonOutputParser()
    # Define prompt template
    template = ChatPromptTemplate.from_template(
        'For this user, suggest 10 recipes. Only output names in JSON format such as this: ["sandwich", "pizza", "salad"]. Here is the user:  {user}')
    # Chain prompts and AI model for recommendation
    recommendation_chain = template | llm | output_parser_user
    # Invoke recommendation chain with user data
    return recommendation_chain.invoke({"user": user_data})


# Function to get recipe details based on recipe name
def get_recipe(recipe):
    # Initialize output parser
    output_parser_recipe = JsonOutputParser()
    # Define prompt template for recipe response
    template_recipe_response = ChatPromptTemplate.from_template(
        "Please provide the recipe details for this recipe: {recipe} in this JSON format: {sampleRecipe}"
    )
    # Chain prompts and AI model for recipe details
    recipe_chain = template_recipe_response | llm | output_parser_recipe
    # Invoke recipe chain with recipe name and sample recipe JSON
    return recipe_chain.invoke({"recipe": recipe, "sampleRecipe": sampleRecipe})


# Function to generate recipes based on user data
def generate_recipe(user_data):
    # Get list of recipe names for the user
    recipes_name_list = get_recipe_names(user_data)
    recipes = []
    # Iterate through recipe names and retrieve recipe details
    for recipe in recipes_name_list:
        try:
            # Attempt to get recipe details
            recipes.append(get_recipe(recipe))
        except Exception as e:
            # If an error occurs, continue to the next recipe
            continue

    return recipes
