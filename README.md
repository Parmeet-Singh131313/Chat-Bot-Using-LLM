# Gemini Pro Q/A App

A simple Streamlit application that leverages Google Generative AI (Gemini Pro) to answer user questions. This project showcases how to integrate Google’s Generative AI with a Streamlit interface to create an interactive Q/A tool.

## Features

- **Interactive UI**: Users can input questions through a text field and receive answers from the Gemini Pro model.
- **Generative AI Integration**: Uses Google’s Generative AI for natural language processing and response generation.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.7 or later
- A Google Cloud API key for Gemini Pro

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/gemini-qa-app.git
    cd gemini-qa-app
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

    Create a `.env` file in the root directory of the project and add your API key:

    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Streamlit App**:

    ```bash
    streamlit run app.py
    ```

2. **Interact with the App**:
   
   Open your web browser and navigate to `http://localhost:8501`. You will see the app interface where you can enter your questions and get responses from the Gemini Pro model.

## Code Overview

- `app.py`: Main script for running the Streamlit app. Configures the Streamlit UI and handles user interactions with the Gemini Pro model.
- `.env`: Environment file for storing sensitive information such as API keys.
- `requirements.txt`: Lists the dependencies required to run the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License

## Contact

For any questions or inquiries, please contact parmeetsingh1313n@gmail.com
