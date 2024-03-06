# 🥑 NutriChat Backend API 🍲

## Introduction 🌟

Welcome to the NutriChat Backend API! This powerful tool is designed to generate delicious recipes tailored to users' preferences. Whether you're developing for the NutriChat iOS app or any other platform, this API has you covered.

## Development 💻

### Technologies 🛠️

1. **Flask:** Crafted with Flask, a lightweight Python web framework, making development a breeze.
2. **Gemini 🤖:** Powered by Google's Gemini Pro model, delivering top-notch recipe recommendations.
3. **Langchain 🦜🔗:** Leveraging Langchain for structured interactions with AI models, ensuring smooth communication.

### Chaining Usage 🔗

Chaining simplifies interactions with AI models, ensuring seamless recipe generation. Here's how it works:

- **Prompt Template Definition:** Define templates with `ChatPromptTemplate` for clear inputs and desired outputs.
- **AI Model Initialization:** Initialize `ChatGoogleGenerativeAI` with Gemini Pro for quality responses.
- **Prompt Chaining:** Chain templates for coherent interactions, streamlining recipe generation.
- **Output Parsing:** Utilize parsers like `JsonOutputParser` to extract accurate recipe details.
- **Error Handling:** Gracefully handle errors for smooth execution of functionalities.

## Setup ⚙️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mayank-raj1/NutriChatBackend.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd NutriChatBackend
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```plaintext
     FLASK_APP=main.py
     FLASK_ENV=development
     GOOGLE_API_KEY = "Your Google Gemini API Key"
     ```

7. **Run the Flask application:**
   ```bash
   flask run
   ```

## Endpoints 🚀

### Recipe Generation and Retrieval

- **URL:** `/suggest`
- **Method:** `POST`
- **Request Body:**
  
  ```json
  {
    "name": "John Doe",
    "age": 30,
    "preferences": {
      "dietary_restrictions": ["vegetarian", "gluten-free"],
      "allergies": ["peanuts"]
    }
  }
  ```
  
- **Response:**
  
  ```json
  {
    "recipes": [
      {
        "name": "Oatmeal with Berries",
        "ingredients": ["oats", "berries", "milk"],
        "tags": ["quick", "healthy", "breakfast"],
        "category": "breakfast",
        "steps": [
          "Boil oats in milk",
          "Add berries",
          "Serve hot"
        ]
      },
      {
        "name": "Avocado Toast",
        "ingredients": ["avocado", "bread", "tomato", "salt", "pepper"],
        "tags": ["quick", "healthy", "breakfast"],
        "category": "breakfast",
        "steps": [
          "Toast bread",
          "Mash avocado",
          "Spread avocado on toast",
          "Add sliced tomato, salt, and pepper"
        ]
      }
    ]
  }
  ```

## Contributors 🌟

- [Mayank Raj](https://github.com/mayank-raj1)

Feel free to contribute by submitting pull requests or opening issues!
