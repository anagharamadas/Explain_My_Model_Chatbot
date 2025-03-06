**Explain My Model
A chatbot application that provides detailed descriptions of machine learning models based on user input. Built using Streamlit, LangChain's ChatPerplexity, and Perplexity AI's API, this tool enables users to gain insights into various ML models interactively.**

Features
Interactive Chatbot: Enter the name of a machine learning model to get a detailed explanation.

Powered by Perplexity AI: Uses the sonar-reasoning model for generating high-quality responses.

Secure API Key Handling: Users can securely input their Perplexity API key directly in the app.

Streamlit UI: Simple and intuitive interface for seamless interaction.

Installation
Follow these steps to set up and run the application locally:

1. Clone the Repository
   
git clone https://github.com/your-username/explain-my-model.git
cd explain-my-model

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

4. Run the Application
Start the Streamlit app:

streamlit run app.py

Usage
Open the application in your browser (usually at http://localhost:8501).

Enter your Perplexity API Key in the provided field.

Input the name of a machine learning model (e.g., "GPT-4", "XGBoost").

Click on the "Get Description" button to generate a detailed explanation of the model.

Code Overview
The main functionality of the app is implemented in app.py. Here's a quick breakdown of its components:

Streamlit UI:

Accepts user input for the Perplexity API key and model name.

Displays generated descriptions or error messages.

LangChain Integration:

Uses ChatPerplexity from LangChain's community package to interact with Perplexity's API.

Error Handling:

Handles invalid API keys, missing inputs, and API response errors gracefully.

Dependencies
The application requires the following Python libraries:

streamlit

langchain-community

langchain-core

requests

You can install all dependencies using the provided requirements.txt.

Environment Variables
The application uses an environment variable for securely handling the Perplexity API key. The key is entered via the UI and stored temporarily in os.environ.

Troubleshooting
Common Errors:
401 Authorization Required:

Ensure your Perplexity API key is valid and correctly entered.

Verify that your account has sufficient credits.

Empty Response:

Check if the model name you entered is supported by Perplexity's API.

Application Not Running:

Ensure all dependencies are installed correctly.

Verify that you're running Python 3.8 or higher.

Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

Fork this repository.

Create a new branch for your feature or bug fix:


git checkout -b feature-name

Commit your changes and push them to your forked repository.

Submit a pull request with a detailed description of your changes.

Acknowledgments
Streamlit for providing an easy-to-use framework for building web apps.

LangChain for enabling seamless integration with LLMs.

Perplexity AI for their powerful LLM API.
