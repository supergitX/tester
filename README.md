# 🧪 Auto Tester for AI-Generated Code

This repository automates the process of testing AI-generated code. It generates test cases using LLMs, runs the tests, and logs the failures — allowing AI or developers to improve and re-optimize the code iteratively.

---

## 🚀 Features

- ✅ Automatically generates test cases using `generate_tests.py`
- 🧪 Runs those tests using `pytest`
- 📋 Logs failed test cases and reasons in `test_generation.log`
- 🔁 GitHub Actions-based CI/CD to test and push code from `master` ➡️ `test` branch
- 🧠 Feedback loop for AI-based optimizations

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/tester.git
cd tester
```

### 2. Install Requirements
Make sure you have Python 3.10+ installed. Then install dependencies:
```python
pip install pytest requests
```

### 3. How It Works
You push reviewed_code.py to master.

GitHub Action is triggered:

generate_tests.py generates test_reviewed_code.py and test_generation.log.

These files are committed to the test branch.

CI/CD switches to the test branch, runs the tests using pytest.

Failures and logs are stored in test_generation.log.

Your optimization agent (AI or human) can use this log to fix the code.


### 4. File Structure

```.
├── .github/
│   └── workflows/
│       └── run_tests.yml        # GitHub Action workflow
├── reviewed_code.py             # Your AI-reviewed code file
├── generate_tests.py            # LLM-powered test generator
├── test_reviewed_code.py        # Auto-generated test cases
├── test_generation.log          # Test failures & explanations
└── README.md                    # You're here!

```
### 5. Running Manually
``` python
python generate_tests.py
pytest test_reviewed_code.py --tb=short
cat test_generation.log
```
### 6. Setting up Secrets
To enable test generation via LLM (GROQ or other APIs):

Go to your GitHub repository > ⚙️ Settings > Secrets and variables > Actions

Add your API key:

Name: API_KEY NAME

Value: your_api_key_here

### 7. Customization
Modify generate_tests.py to change how tests are generated

Edit the GitHub Actions YAML (.github/workflows/run_tests.yml) to adapt to different workflows (e.g., auto-merge, Slack/Discord alerts)

