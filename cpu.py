from happytransformer import HappyTextClassification
import textwrap
from nltk.tokenize import sent_tokenize
import re

models = {
    "EnvironmentalBERT": HappyTextClassification("BERT", "Vinoth24/environmental_claims"),
    "SocialBERT": HappyTextClassification("BERT", "ESGBERT/SocialBERT-social"),
    "GovernanceBERT": HappyTextClassification("BERT", "ESGBERT/GovernanceBERT-governance")
}


def process_and_classify_content(content):
    content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
    sentences = sent_tokenize(content)
    classified_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            # Use text wrapping to avoid excessively long lines
            wrapped_text = textwrap.fill(sentence, width=80)
            for line in wrapped_text.split('\n'):
                # Check each model for classification
                for model_name, model in models.items():
                    result = model.classify_text(line)
                    if result.label == "LABEL_1" and result.score > 0.5:
                        clean_line = ' '.join(line.split())
                        classified_sentences.append(f"{model_name}: {clean_line}")
                        break  # Stop checking other models if one has classified the line already

    return '\n'.join(classified_sentences)
