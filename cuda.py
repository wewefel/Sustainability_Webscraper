import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import textwrap
from nltk.tokenize import sent_tokenize
import re

model_info = {
    "EnvironmentalBERT": ("Vinoth24/environmental_claims", None),
    "SocialBERT": ("ESGBERT/SocialBERT-social", None),
    "GovernanceBERT": ("ESGBERT/GovernanceBERT-governance", None)
}

# Initialize models and tokenizers and move models to GPU
for key, (model_name, _) in model_info.items():
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForSequenceClassification.from_pretrained(model_name).to('cuda')
   model_info[key] = (model, tokenizer)

def process_and_classify_content(content):
    content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
    sentences = sent_tokenize(content)
    classified_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            # Use text wrapping to manage long lines
            wrapped_text = textwrap.fill(sentence, width=150)
            for line in wrapped_text.split('\n'):
                # Check each model for classification
                for model_name, (model, tokenizer) in model_info.items():
                    inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True, max_length=512).to('cuda')
                    with torch.no_grad():
                        outputs = model(**inputs)
                        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
                        score, predicted_class = probs.max(1)
                        if score.item() > 0.6 and predicted_class.item() == 1:
                            clean_line = ' '.join(line.split())
                            classified_sentences.append(f"{model_name}: {clean_line}")
                            break  # Stop checking other models if one has classified the line already

    return '\n'.join(classified_sentences)