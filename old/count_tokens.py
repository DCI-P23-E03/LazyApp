import tiktoken


def count_tokens(text):
    # enc = tiktoken.encoding_for_model("text-davinci-003")
    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = len(enc.encode(text))
    tokens_left = 4096 - tokens
    return tokens, tokens_left


print("Tokens used:", count_tokens(str(conversation))[0])
print("Tokens left:", count_tokens(str(conversation))[1])
