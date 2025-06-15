import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(
        prog="Boot.dev AI Chatbot", usage="%(prog)s [options]"
    )
    parser.add_argument("prompt", help="prompt to go to the AI")
    parser.add_argument(
        "--verbose", action="store_true", help="Print Additional Debug Info"
    )

    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )

    if args.verbose:
        print(f"User prompt: {response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(f"{response.text}")


if __name__ == "__main__":
    main()
