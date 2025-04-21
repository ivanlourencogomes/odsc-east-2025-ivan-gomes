
import sys
import requests
import os

MODEL = "deepseek-coder"

if len(sys.argv) < 2:
    print("❌ Usage: python to_es6_file.py <filename.js>")
    sys.exit(1)

input_path = sys.argv[1]

if not os.path.isfile(input_path):
    print(f"❌ File not found: {input_path}")
    sys.exit(1)

# Read the original file
with open(input_path, "r") as f:
    original_code = f.read()

# Build the prompt
prompt = f"""
You are a JavaScript expert. Convert the following code to modern ES6+ syntax.

Return only the updated code in JavaScript.

Code:
{original_code}
"""

# Send to Ollama
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

raw_response = data.get("response", "").strip()

if "```javascript" in raw_response and "```" in raw_response:
    parts = raw_response.split("```javascript", 1)[1].split("```", 1)
    updated_code = parts[0].strip()
else:
    updated_code = raw_response

# Write to new file
output_path = input_path.replace(".js", "_es6.js")
with open(output_path, "w") as f:
    f.write(updated_code)

print(f"✅ Modernized code written to: {output_path}")
