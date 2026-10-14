from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

text = "Machine Learning is Awesome!"

tokens = tokenizer.tokenize(text)
print(tokens)

token_ids = tokenizer.encode(text)
print(token_ids)