import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json

# Load environment variables from .env file
config = dotenv_values('.env')
# Set OpenAI API key
openai.api_key = config["OPENAI_API_KEY"]

# Create Flask application instance
app = Flask(__name__)


def get_colors(msg):
    # Define a prompt for generating color palettes based on text prompts
    prompt = f"""
    You are a color palette generating assistant. Your task is to generate color palettes based on verbal descriptions, themes, moods, or instructions provided in the prompt. The color palettes should consist of 2 to 8 colors.

    **Example:**

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

    **Desired Format:**
    The color palettes should be provided in a JSON array format, where each element is a hexadecimal color code.

    Q: Convert the following verbal description of a color palette into a list of colors: {msg}
    A:

    """
    # Send completion request to OpenAI API to generate color palette
    response = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=200,
    )

    # Extract the generated colors from the API response
    colors = json.loads(response["choices"][0]["text"])
    return colors


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}


# Route to handle POST requests for generating color palettes.
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
