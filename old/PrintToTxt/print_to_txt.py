import openai  # Assuming you're using the OpenAI GPT library

# Your OpenAI API key
openai.api_key = "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"


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=100  # Adjust as needed
    )
    return response.choices[0].text.strip()


prompts = [
    "Once upon a time, in a land far away...",
    "What are the benefits of exercising daily?",
    "Describe the process of photosynthesis.",
]

for index, prompt in enumerate(prompts, start=1):
    response_text = generate_response(prompt)

    # Create a new text file for each response
    filename = f"response_{index}.txt"
    with open(filename, "w") as file:
        file.write(response_text)

    print(f"Response saved to {filename}")
