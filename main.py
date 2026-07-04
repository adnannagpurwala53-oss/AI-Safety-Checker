import os
from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
def check_text_safety(text):
    """
    Sends the given text to Claude and asks it to classify
    whether the text is safe or unsafe, with a short reason.
    """
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[
            {
                "role": "user",
                "content": (
                    "You are a content safety classifier. "
                    "Analyze the following text and respond in this exact format:\n"
                    "Verdict: SAFE or UNSAFE\n"
                    "Reason: <one short sentence>\n\n"
                    f"Text to analyze: \"{text}\""
                )
            }
        ]
    )
    return response.content[0].text
if __name__ == "__main__":
    print("=== AI Safety Checker ===")
    print("Type a sentence to check, or 'quit' to exit.\n")
    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        result = check_text_safety(user_input)
        print("\n" + result + "\n")
        