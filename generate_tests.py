import requests
import os
import logging
import subprocess
from datetime import datetime

# ────── Logging Configuration ──────
log_file = "test_generation.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("🔧 Starting test generation process")

# ────── Load Groq API Key ──────
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    except ModuleNotFoundError:
        logging.error("Missing dotenv module. Set GROQ_API_KEY manually.")
        print("❌ Missing API key. Set GROQ_API_KEY as an environment variable.")
        exit(1)

# ────── API Config ──────
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"  

# ────── Read Reviewed Code ──────
try:
    with open("reviewed_code.py", "r") as file:
        reviewed_code = file.read()
        logging.info("✅ Successfully read reviewed_code.py")
except FileNotFoundError:
    logging.error("❌ reviewed_code.py not found.")
    print("❌ reviewed_code.py not found.")
    exit(1)

# ────── Prompt ──────
prompt = f"""
Generate unit tests using pytest for the following Python code:

{reviewed_code}

Requirements:
- Test both valid and invalid inputs.
- Include edge cases, such as None, negative values, empty strings, zero, large values, etc.
- Validate incorrect behavior: tests MUST fail if the logic in reviewed_code.py is wrong.
- Use meaningful assertions that will fail if code is incorrect.
- Import using 'from reviewed_code import <function>'.
- Only output raw test code. No explanations. No markdown. Just test code.

These tests should enforce correctness, not just check if the function runs.
"""


# ────── Payload ──────
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": "You are a helpful AI that writes clean, structured Python unit tests."},
        {"role": "user", "content": prompt},
    ],
    "temperature": 0.3,
}

# ────── API Call ──────
try:
    response = requests.post(
        GROQ_API_URL,
        headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
        json=payload,
    )
except Exception as e:
    logging.error(f"❌ Request failed: {e}")
    print("❌ Request to Groq API failed.")
    exit(1)

# ────── Handle Response ──────
if response.status_code == 200:
    test_code = response.json()["choices"][0]["message"]["content"]
    test_code = test_code.strip("```python").strip("```").strip()
    
    with open("test_reviewed_code.py", "w") as test_file:
        test_file.write(test_code)
    
    logging.info("✅ Test cases generated and saved successfully")
    print("✅ Test cases generated and saved successfully!")
else:
    logging.error(f"❌ API error: {response.status_code} - {response.text}")
    print(f"❌ API Error: {response.status_code}")
    
# ────── Run Tests and Log Output ──────
try:
    result = subprocess.run(
        ["pytest", "test_reviewed_code.py", "--tb=short"],
        capture_output=True,
        text=True
    )
    
    test_output = result.stdout + "\n" + result.stderr

    # Write to log with timestamp
    with open(log_file, "a") as f:
        f.write(f"\n\n======= 🚀 Test Run - {datetime.now()} =======\n")
        f.write("===== 🧪 Pytest Output =====\n")
        f.write(test_output)

    # Print to console
    print(test_output)

    if result.returncode != 0:
        logging.error("❌ One or more tests failed.")
        print("❌ Tests failed. Check log.")
    else:
        logging.info("✅ All tests passed.")
        print("✅ All tests passed.")

except Exception as e:
    logging.error(f"❌ Failed to run tests: {e}")
    print("❌ Error while running tests.")

