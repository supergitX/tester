import requests
import os
#from dotenv import load_dotenv
#load_dotenv()
# Groq API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Store API Key securely in GitHub Secrets
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Read the reviewed code
with open("reviewed_code.py", "r") as file:
    reviewed_code = file.read()

# Define the prompt for generating test cases
# Define the prompt for generating test cases
prompt = f"""
Generate unit tests using pytest for the following Python code:

{reviewed_code}

Ensure:
- Test coverage for different scenarios.
- Proper function validation.
- Meaningful assertions.
- Include "from reviewed_code import <function_name>" at the top.
Provide only the code output, no extra explanations.
"""


# API request payload
payload = {
    "model": "qwen-2.5-coder-32b",  # Adjust model if needed
    "messages": [
        {"role": "system", "content": "You are a helpful AI that writes unit tests."},
        {"role": "user", "content": prompt},
    ],
    "temperature": 0.3,
}

# Make API request
response = requests.post(
    GROQ_API_URL,
    headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
    json=payload,
)

# Parse response
if response.status_code == 200:
    test_code = response.json()["choices"][0]["message"]["content"]
    
    # Save generated tests to file
    with open("test_reviewed_code.py", "w") as test_file:
        test_file.write(test_code)
    
    print("✅ Test cases successfully generated and saved!")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")


