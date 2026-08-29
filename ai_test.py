from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

client = OpenAI()

question = input("Ask the AI anything: ")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=question
)

answer = response.output_text

print("\nAI:")
print(answer)

# Create the answers folder if it doesn't exist
answers_folder = Path("answers")
answers_folder.mkdir(exist_ok=True)

# Find the next answer number
existing_files = list(answers_folder.glob("ai_blockchain_ans*.txt"))
next_number = len(existing_files) + 1

# Create the filename
filename = answers_folder / f"ai_blockchain_ans{next_number}.txt"

# Save question + answer
filename.write_text(
    f"QUESTION:\n{question}\n\n"
    f"ANSWER:\n{answer}\n",
    encoding="utf-8"
)

print(f"\nSaved to: {filename}")