# Experiment 1: Creative storytelling
from transformers import pipeline
generator=pipeline("text-generation", model="gpt2")
prompt="once upon a time, in a land far, far away, there was a knight"
generated_text1 = generator(
    prompt,
    max_length=150,
    num_return_sequences=3,
    do_sample=True,
    temperature=0.7
)

print("--- Experiment 1: Creative Storytelling ---")
for i, sequence in enumerate(generated_text1):
    print(f"Sequence {i+1}:\n{sequence['generated_text']}\n")

# Experiment 2: More constrained and factual-sounding text
prompt2 = "The history of the internet began in the 1960s with"
generated_text2 = generator(
    prompt2,
    max_length=100,
    num_return_sequences=1,
    do_sample=False, # Use greedy decoding for more predictable output
)

print("--- Experiment 2: Factual-sounding text ---")
print(f"Sequence 1:\n{generated_text2[0]['generated_text']}\n")