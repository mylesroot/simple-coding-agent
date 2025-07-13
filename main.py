import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simple coding agent using Google GenAI")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("prompt", nargs="?", help="The prompt to send to the AI")

    # Use sys to print usage instructions if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize Google GenAI client
    client = genai.Client(api_key=api_key)

    # Use provided prompt or default
    user_prompt = args.prompt or "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    if args.verbose:
        print(f"User prompt: {user_prompt}")

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=user_prompt
    )

    text = response.text
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"Prompt tokens: {input_tokens}")
        print(f"Response tokens: {output_tokens}")

    print(text)

if __name__ == "__main__":
    main()
