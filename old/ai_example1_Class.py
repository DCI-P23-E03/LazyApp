import openai
from dotenv import load_dotenv
import os

load_dotenv()

# hidden api key
key = os.getenv("KEY")


class ChatGPTCompletion:
    def __init__(
        self,
        api_key=key,
        engine="text-davinci-003",
        max_tokens=150,
        temperature=0.7,
        completions=3,
        best_of=3,
        presence_penalty=0.5,
        frequency_penalty=0.5,
    ):
        self.api_key = api_key
        self.engine = engine  # engine is the chatgpt model used, davinci is the smartest, fastest yet most expensive
        self.max_tokens = max_tokens  # maximum tokens allowed for response length
        self.temperature = temperature  #  0.0 is deterministic, completely strict to system role - 1.0 is creative, completely random responses (now choose)
        self.completions = completions  # number of completions per prompt
        self.best_of = best_of  # multiplies the number of completions and chooses the best of (multiplies costs too)
        self.presence_penalty = presence_penalty  # the higher the value, the more likely new topics will be introduced
        self.frequency_penalty = frequency_penalty  # the higher the value, the more likely information will be repeated
        openai.api_key = self.api_key

    def get_chatgpt_response(self, user_input):
        response = openai.Completion.create(
            engine=self.engine,  # engine/model
            prompt=user_input,  # prompt for the ai
            max_tokens=self.max_tokens,  # maximum tokens allowed
            temperature=self.temperature,  # temperature (creativeness/strictness)
            n=self.completions,  # completion number
            best_of=self.best_of,  # best of responses
            echo=False,  # echo includes the user input (prompt) in the response
            presence_penalty=self.presence_penalty,  # chosen new-topics-probability
            frequency_penalty=self.frequency_penalty,  # chosen repeat-info-probability
        )
        choices = [
            choice.text.strip() for choice in response.choices
        ]  # getting all responses from response
        return choices

    def chat_interface(self):
        print("Welcome to ChatGPT!")
        print("Type 'quit' to exit the chat.\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break
            responses = self.get_chatgpt_response(user_input)
            print("CHAT GPT: ")
            for response in responses:
                print(response)


if __name__ == "__main__":
    chat_gpt = ChatGPT()
    chat_gpt.chat_interface()
