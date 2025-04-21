
import requests

MODEL = "gemma3:1b"

def chat():
    print("🤖 DeepSeek Chat Assistant (type 'exit' or 'q' to quit)")
    while True:
        user_input = input("\n👤 You: ").strip()
        if user_input.lower() in ["exit", "q"]:
            print("👋 Goodbye!")
            break

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": f"""

                answer this user question: {user_input}

                """,
                "stream": False
            }
        )

        data = response.json()
        reply = data.get("response", "").strip()
        print(f"🤖 DeepSeek: {reply}")

if __name__ == "__main__":
    chat()
