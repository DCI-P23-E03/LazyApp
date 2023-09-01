LazyApp

LazyApp is a Git repository that houses an application assistant tool with a graphical user interface (GUI). The tool utilizes OpenAI's GPT-3.5-turbo model to generate application letters, provide CV improvements, and offer cheatsheets based on job ads and CV information. The repository includes support for both English and German versions.

Features

The LazyApp application assistant offers the following features:

Application Letter Generation: The tool generates personalized application letters based on the provided job ads and CV information. It utilizes the power of GPT-3.5-turbo to create compelling and tailored letters.

CV Improvements: The assistant provides suggestions and improvements for your CV. It analyzes your existing CV and offers recommendations to enhance its content, structure, and overall presentation.

Cheatsheets: The tool generates cheatsheets based on job ads and CV information. These cheatsheets provide valuable insights and tips to help you prepare for interviews and showcase your skills effectively.

Graphical User Interface: LazyApp includes a user-friendly GUI that allows you to modify various parameters, such as AI temperature, word count, annual salary expectations, availability (full-time or part-time), and starting date. The GUI simplifies the interaction with the application assistant.

Token Counter Function: The repository includes a token_counter function that helps you estimate the costs associated with generating the AI-generated outcome. This function allows you to keep track of your token usage and manage your OpenAI API usage effectively.

Usage

To use LazyApp, follow these steps:

Clone this repository to your local machine using the following command:
   git clone https://github.com/your-username/LazyApp.git
Copy
Install the required Python modules by running the following command:
   pip install -r requirements.txt
Copy
Set up your OpenAI API credentials by creating a .env file in the project directory and adding the following lines:
   OPENAI_API_KEY=your-api-key
Copy

Replace your-api-key with your actual OpenAI API key.

Customize the assistant's behavior by modifying the following parameters in the code:

ai_temperature: Adjust the AI temperature to control the randomness of the generated responses. Higher values (e.g., 0.8) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic.
word_amount: Set the desired word count for the generated text. The recommended range is between 250 and 400 words.
annual_salary_expectations: Provide your annual salary expectations as input to the assistant. This information helps in tailoring the generated application letters.
availability: Specify your availability as either "full-time" or "part-time". This information is used to customize the generated content.
starting_date: Set your preferred starting date for the job. The assistant takes this into account while generating application letters.

Run the LazyApp application by executing the following command:

   python lazyapp.py
Copy
The GUI will open, allowing you to interact with the application assistant. Use the provided options and input fields to modify the parameters and generate application letters, CV improvements, or cheatsheets based on your requirements.
Contributions

Contributions to this project are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request on the GitHub repository.

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of this license.

Disclaimer

Please note that the generated content, including application letters and CV improvements, is based on AI-generated responses and should be reviewed and validated by humans before use. The tool provides suggestions and assistance, but the final responsibility lies with the user.