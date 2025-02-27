from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

# Simple prompt
simple_prompt = "Tell me a story"
result1 = generator(simple_prompt, max_length=40)
print("Simple: ", result1[0]['generated_text'])

# Detailed prompt
detailed_prompt = "Tell me a story about a pirate with a wooden leg"
result2 = generator(detailed_prompt, max_length=40)
print("Detailed", result2[0]['generated_text'])