# Install transformers if you haven’t: pip install transformers
from transformers import pipeline

# Load a text generation model (e.g., GPT-2)
generator = pipeline("text-generation", model="gpt2")

# Generate text
text = generator("Once upon a time", max_length=100, num_return_sequences=1)
print(text[0]["generated_text"])