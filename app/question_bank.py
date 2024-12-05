from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import random

# Initialize the text generation pipeline
generator = pipeline(
    "text-generation",
    model="EleutherAI/gpt-neo-1.3B",  # Your chosen model
    device=0  # Use GPU if available; set to -1 to force CPU
)

def generate_question(role):
    """Generate a concise and professional interview question to evaluate the role."""
    prompt = f"Generate a concise and professional interview question to evaluate {role} skills."
    inputs = {"inputs": prompt}
    output = generator(**inputs, max_length=50, num_return_sequences=1, do_sample=True, temperature=0.7)
    return output[0]["generated_text"]
# Load a pre-trained model for better text generation
model_name = "EleutherAI/gpt-neo-1.3B"  # Replace with a larger, more advanced model if required
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Pre-defined prompt templates for variety
question_templates = [
    "Generate a concise interview question to evaluate {role} skills.",
    "Write a professional interview question for a {role} candidate.",
    "Provide a technical question to assess {role} knowledge and problem-solving skills."
]

def clean_generated_text(text):
    """Ensure the output is concise and relevant."""
    lines = text.split(".")  # Split into sentences
    return lines[0].strip()  # Return only the first, relevant sentence

def generate_question(role):
    """Generate a role-specific interview question."""
    # Randomly select a template for question generation
    prompt = random.choice(question_templates).format(role=role)
    
    # Generate the question using the model
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50, num_return_sequences=1, do_sample=True, temperature=0.7)
    raw_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    return clean_generated_text(raw_text)