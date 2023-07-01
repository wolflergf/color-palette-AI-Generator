# Color Palette AI Generator

This repository hosts the Color Palette AI Generator, a Flask application that leverages OpenAI's text-based AI model to generate visually appealing color palettes based on verbal descriptions, themes, moods, or instructions provided in the prompt.

## Project Overview
The Color Palette AI Generator utilizes the power of AI to convert text prompts into aesthetically pleasing color palettes. By providing a description or set of keywords, the AI model generates a list of colors represented by hexadecimal color codes. The resulting color palettes consist of 2 to 8 colors and are provided in a JSON array format.

## Key Features and Benefits
- Simplifies the process of exploring color options for designers and creatives in various domains such as graphic design, web development, UI/UX design, and branding.
- Enables quick generation of color palettes aligned with desired themes, moods, or instructions.
- Offers flexibility by accepting textual descriptions as input, reducing the need for manual color selection.

## Getting Started
To get started with the Color Palette AI Generator, follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/wolflergf/color-palette-AI-Generator.git`
2. Navigate to the project directory: `cd color-palette-AI-Generator`
3. Install the required dependencies. It is recommended to use a virtual environment:
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate.bat`
     - On macOS and Linux: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file in the project directory and set your OpenAI API key in the following format:
   ```
   OPENAI_API_KEY=<your_openai_api_key>
   ```
5. Start the Flask application: `python app.py`
6. Open your web browser and visit `http://localhost:5000` to access the Color Palette AI Generator.

## Getting Help
If you need any assistance or have questions about the Color Palette AI Generator, please open an issue in the repository. I will be happy to help you.

## Project Maintenance and Contributions
The Color Palette AI Generator is maintained and contributed to by Wolfler (`https://github.com/wolflergf`). If you're interested in enhancing the project, you can fork the repository, make changes, and submit pull requests with your proposed improvements or bug fixes. I will review and merge the pull requests as appropriate.
