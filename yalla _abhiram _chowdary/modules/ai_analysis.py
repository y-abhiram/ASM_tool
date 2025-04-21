import json
from transformers import pipeline, set_seed

# Load the tiny GPT-2 model (lightweight)
generator = pipeline(
    "text-generation", 
    model="sshleifer/tiny-gpt2", 
    tokenizer="sshleifer/tiny-gpt2", 
    device=-1  # -1 for CPU, change to 0 for GPU if CUDA is available
)

# Optional: make results consistent across runs
set_seed(42)

def generate_summary(data):
    prompt = f"""Analyze this data and provide a risk assessment summary:\nDATA: {json.dumps(data)}\nSummary:"""

    # Use max_new_tokens to control the output length (number of new tokens generated)
    result = generator(
        prompt, 
        max_new_tokens=100,  # Generate up to 100 new tokens
        num_return_sequences=1, 
        pad_token_id=generator.tokenizer.eos_token_id,  # Avoids warning about pad_token_id
        truncation=True  # Ensure text is truncated correctly
    )[0]['generated_text']

    return {"risk_summary": result}
'''import json

import openai
client = openai.OpenAI(api_key="apikey")  # Use OpenAI client

def generate_summary(data):
    prompt = f"""Analyze this data and provide:
1. Summary of Key Risks
2. Severity Level
3. Suggest Remediation
DATA: {json.dumps(data)}"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"risk_summary": response.choices[0].message.content}'''

