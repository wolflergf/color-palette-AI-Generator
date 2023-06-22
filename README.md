# Color Palette AI Generator

This repository contains a Color Palette AI Generator. This Flask application uses OpenAI's text-based AI model to generate colour palettes based on verbal descriptions, themes, moods, or instructions provided in the prompt.

## What the project does
The Color Palette AI Generator utilizes the power of AI to convert text prompts into visually appealing colour palettes. The AI model generates a list of colours represented by hexadecimal colour codes by providing a description or set of keywords. The colour palettes consist of 2 to 8 colours, and the generated results are provided in a JSON array format.

## Why the project is useful
The Color Palette AI Generator can be helpful in various design-related scenarios, such as graphic design, web development, UI/UX design, branding, and more. It helps designers and creatives to quickly explore colour options based on textual descriptions, allowing them to generate colour palettes that align with their desired themes, moods, or instructions.

### How users can get started with the project
To get created with the Color Palette AI Generator, follow these steps:

1. Clone the repository to your local machine: git clone https://github.com/wolflergf/color-palette-AI-Generator.git
2. Navigate to the project directory: cd color-palette-AI-Generator
3. Install the required dependencies. It is recommended to use a virtual environment:
  - Create a virtual environment: python -m venv venv
  - Activate the virtual environment:
    - On Windows: venv\Scripts\activate.bat
    - On macOS and Linux: source venv/bin/activate
  - Install dependencies: pip install -r requirements.txt
4. Create a .env file in the project directory and set your OpenAI API key in the following format:
makefile
Copy code
OPENAI_API_KEY=<your_openai_api_key>

5. Start the Flask application: python app.py
6. Open your web browser and visit http://localhost:5000 to access the Color Palette AI Generator.

## Where users can get help with your project
If you need any assistance or have questions about the Color Palette AI Generator, please open an issue in the repository. I will be happy to help you.

## Who maintains and contributes to the project
I, Wolfler (https://github.com/wolflergf), maintain and contribute to the Color Palette AI Generator. If you're interested in contributing to the project, you can fix the repository, make changes, and submit pull requests with your proposed improvements or bug fixes. I will be sure to merge pull requests as appropriate.
