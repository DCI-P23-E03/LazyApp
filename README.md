LazyApp

LazyApp is a Git repository housing an application assistant tool with a graphical user interface (GUI). This tool leverages OpenAI's GPT-3.5-turbo model to generate application letters, provide CV improvements, and offer cheatsheets based on job ads and CV information. The repository includes support for both English and German versions. Having an OpenAI API key is mandatory to use LazyApp!
Features

The LazyApp application assistant offers the following features:

    Application Letter Generation: The tool generates personalized application letters based on the provided job ads and CV information. It utilizes the power of GPT-3.5-turbo to create compelling and tailored letters.

    CV Improvements: The assistant provides suggestions and improvements for your CV. It analyzes your existing CV and offers recommendations to enhance its content, structure, and overall presentation.

    Cheatsheets: The tool generates cheatsheets based on job ads and CV information. These cheatsheets provide valuable insights and tips to help you prepare for interviews and showcase your skills effectively.

    GUI - Graphical User Interface: LazyApp includes a user-friendly GUI that allows you to modify various parameters, such as AI temperature, word count, annual salary expectations, availability (full-time or part-time), and starting date. The GUI simplifies the interaction with the application assistant.

    Cost Estimation: The repository includes a cost estimation based on the tokens used for the AI-generated outcome.

Usage

To use LazyApp, follow these steps:

    Clone this repository to your local machine using the following command:

    bash

git clone https://github.com/your-username/LazyApp.git

Install the required Python modules by running the following command:

pip install -r requirements.txt

Set up your OpenAI API credentials by creating a .env file in the project directory and adding the following lines:

makefile

OPENAI_API_KEY=your-api-key

Replace your-api-key with your actual OpenAI API key.

Run the LazyApp application by executing the following command:

    python lazyapp.py

The GUI will open, allowing you to interact with the application assistant. Use the provided options and input fields to modify the parameters and generate application letters, CV improvements, or cheatsheets based on your requirements.
Contributions

Customize the outcome by modifying the following parameters of the GUI:

    CV: Uploading a CV is mandatory to use the App. The file must be a PDF.

    AI-Behavior: Adjusts the AI temperature to control the rational/creative outcome of the generated responses. Higher values (e.g., 0.8) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic.

    Word Amount: Set the desired word count for the generated text. The recommended range is between 250 and 400 words.

    Annual Salary Expectations: Provide your annual salary expectations as input to the assistant. This information helps in tailoring the generated application letters.

    Availability: Specify your availability as either "full-time" or "part-time". This information is used to customize the generated content.

    Starting Date: Set your preferred starting date for the job. The assistant takes this into account while generating application letters.

You have the choice between generating an Application Letter, Cheatsheet, or CV Improvements (multiple choice). After you've made your decision, be patient and wait for the AI to respond (it might take up to two minutes).
Disclaimer

Please note that the generated content, including application letters and CV improvements, is based on AI-generated responses and should be reviewed and validated by humans before use. The tool provides suggestions and assistance, but the final responsibility lies with the user.
