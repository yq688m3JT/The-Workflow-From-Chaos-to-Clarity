import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def summarize_meeting(input_text, system_prompt, model=None):
    """Summarizes a meeting transcript using a local Ollama model."""
    # Use environment variables or defaults
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
    default_model = os.getenv("OLLAMA_MODEL", "gemma4:e2b")
    
    # Use the passed-in model if available, otherwise use default_model
    target_model = model if model else default_model

    client = OpenAI(
        base_url=base_url,
        api_key="ollama" 
    )
    
    response = client.chat.completions.create(
        model=target_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text}
        ],
        temperature=0.0
    )
    
    return response.choices[0].message.content

def main():
    default_model = os.getenv("OLLAMA_MODEL", "gemma4:e2b")
    parser = argparse.ArgumentParser(description="Summarize a meeting transcript or notes.")
    parser.add_argument("--input", "-i", type=str, default="input_sample.txt", help="Path to input file")
    parser.add_argument("--prompt", "-p", type=str, default="system_prompt.txt", help="Path to system prompt file")
    parser.add_argument("--output", "-o", type=str, default="summary_output.txt", help="Path to output file")
    parser.add_argument("--model", "-m", type=str, default=default_model, help=f"Model to use (default: {default_model})")

    
    args = parser.parse_args()
    
    # Read files
    try:
        with open(args.input, '\''r'\'') as f:
            input_text = f.read()
        
        with open(args.prompt, '\''r'\'') as f:
            system_prompt = f.read()
            
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
        return

    print(f"Summarizing using {args.model}...")
    summary = summarize_meeting(input_text, system_prompt, args.model)
    
    # Save output
    with open(args.output, '\''w'\'') as f:
        f.write(summary)
        
    print(f"Summary saved to {args.output}")

if __name__ == "__main__":
    main()
