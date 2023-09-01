import openai
from stringcolor import *
from dotenv import load_dotenv
import os
import tiktoken


load_dotenv()

# hidden api key 
key = os.getenv("KEY")

class ChatGPTChat:
    def __init__(self, api_key=key, model="gpt-3.5-turbo", max_tokens=1000, temperature=0.5, completions=1, presence_penalty=0.5, frequency_penalty=0.5):
        self.api_key = api_key
        self.model = model # The ChatGPT model used (gpt-3.5-turbo is an example, can be replaced)
        self.max_tokens = max_tokens # Maximum tokens allowed for response length
        self.temperature = temperature # 0.0 is deterministic, 1.0 is creative
        self.completions = completions # Number of completions per prompt
        self.presence_penalty = presence_penalty # The higher the value, the more likely new topics will be introduced
        self.frequency_penalty = frequency_penalty # The higher the value, the more likely information will be repeated
        openai.api_key = self.api_key

    def get_chatgpt_response(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model, # ChatGPT model
            messages=messages, # Ongoing conversation
            temperature=self.temperature, # Chosen temperature (creativity/strictness)
            max_tokens=self.max_tokens, # Maximum tokens allowed
            n=self.completions, # Number of completions
            presence_penalty=self.presence_penalty, # Chosen new-topics-probability
            frequency_penalty=self.frequency_penalty # Chosen repeat-info-probability
        )
        choices = [choice.message['content'] for choice in response.choices] # Extracting the content of responses
        return choices
    
    # Define function to count tokens
    def count_tokens(self, text):
            enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
            tokens = len(enc.encode(text))
            token_usage_costs = tokens / 1000 * 0.015
            return tokens, token_usage_costs, print("Tokens used:", tokens, " ; " "Your Costs are :", token_usage_costs, " Euro")

    def chat_interface(self, user_input):
        # Display welcome message
        print(cs("Welcome to ChatGPT!", "blue"))
        print(cs("Type 'quit' to exit the chat.\n", "darkblue"))
        system_role = "You are a helpful expert for jobsearch and application. You adapt the wording in regards to the job the user wants to apply for and provide additional information on companies and competitive market salaries." # DEFINE SYSTEM ROLE HERE
        global messages
        messages = [{"role": "system", "content": system_role}] 
        #for prompt in user_input:
            #if application_letter_checked
            
            #user_input = user_input
            #if user_input.lower() == 'quit':
            #    break
        messages.append({"role": "user", "content": user_input})
            
             # Append user's input to messages
            
        responses = self.get_chatgpt_response(messages)
            
             # Get responses from ChatGPT
        print("CHAT GPT: ")
        print(responses)
            #for resp in responses:
            #    print(cs(resp, "green")) # Display AI's #response in green
            #    messages.append({"role": "assistant", #"content": resp}) # Append AI's response to messages
        self.count_tokens(str(messages)) # Count tokens
            #break
        return responses

if __name__ == '__main__':
    chat_gpt = ChatGPTChat() 
    chat_gpt.chat_interface(["what year is it now","","what is the capital of germany"])
