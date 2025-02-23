import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
url = URL = "https://api.groq.com/openai/v1/chat/completions"


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

#response = requests.get(url, headers=headers)

# Read reviewed code
with open("reviewed_code.py", "r") as file:
    code = file.read()

# Define the test generation prompt
prompt = f"Generate unit tests using pytest for the following Python code:\n\n{code}"

# Groq API request
DATA = {
    "model": "qwen-2.5-coder-32b",
    "messages": [
        {"role": "system", "content": "You generate accurate Python unit tests."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
}

response = requests.post(url, headers=headers, json=DATA)
print(response.json())


# Extract and save generated tests
test_code = response.json()["choices"][0]["message"]["content"]
test_file = "test_reviewed_code.py"
with open(test_file, "w") as file:
    file.write(test_code)

print(f"✅ Tests saved to {test_file}")
