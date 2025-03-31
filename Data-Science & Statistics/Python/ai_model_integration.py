-- pip install transformers pandas torch Pillow requests
-- python ai_model_integration.py

import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification, GPT2LMHeadModel, GPT2Tokenizer
import torch
from PIL import Image
import requests
from io import BytesIO

# Data Transformation with Pandas
data = {
    'text': [
        "I love machine learning!",
        "Transformers are amazing for NLP.",
        "DALL·E can create images from text."
    ]
}

df = pd.DataFrame(data)

# 1. Using BERT for Text Classification
bert_model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(bert_model_name)
model = TFBertForSequenceClassification.from_pretrained(bert_model_name)

# Tokenizing input
inputs = tokenizer(df['text'].tolist(), return_tensors='tf', padding=True, truncation=True)

# Performing inference
predictions = model(inputs).logits
print("BERT Predictions:", predictions.numpy())

# 2. Using GPT-2 for Text Generation
gpt_model_name = 'gpt2'
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_name)
gpt_model = GPT2LMHeadModel.from_pretrained(gpt_model_name)

# Generating text
prompt = "Once upon a time in a land far, far away"
input_ids = gpt_tokenizer.encode(prompt, return_tensors='pt')

# Generate text
gpt_output = gpt_model.generate(input_ids, max_length=50, num_return_sequences=1)
generated_text = gpt_tokenizer.decode(gpt_output[0], skip_special_tokens=True)
print("GPT-2 Generated Text:", generated_text)

# 3. Function to generate image from text prompt uing OpenAI's DALL·E
def generate_image_from_text(prompt):
    
  # Replace with your actual API endpoint for DALL·E
    api_url = "https://api.openai.com/v1/images/generations"
    
    # Replace with your actual API key
    api_key = "YOUR_API_KEY"
    
    # Prepare the headers for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the data payload
    data = {
        "prompt": prompt,
        "n": 1,  # Number of images to generate
        "size": "1024x1024"  # Specify the size of the generated image
    }
    
    # Make the API request to generate the image
    response = requests.post(api_url, headers=headers, json=data)
    
    # Check for a successful response
    if response.status_code == 200:
        # Extract the URL of the generated image
        image_url = response.json()["data"][0]["url"]
        
        # Load the image from the URL
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        img.show()  # Display the generated image
    else:
        print("Error:", response.json())

# usage
generate_image_from_text("A futuristic city skyline at sunset")

# Note: You may need to set up an API key for DALL·E, and this part may require an actual API call.
