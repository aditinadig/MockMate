import random

questions = {
    "Software Developer": [
        "What is polymorphism in OOP?",
        "Describe a challenging coding problem you solved.",
        "How do you ensure your code is scalable?"
    ],
    "Data Scientist": [
        "Explain supervised vs unsupervised learning.",
        "How do you handle missing data?",
        "What is overfitting and how do you prevent it?"
    ],
    "Product Manager": [
        "How do you prioritize features in a roadmap?",
        "Describe a time you resolved a team conflict.",
        "How do you measure product success?"
    ]
}

def generate_question(role):
    return random.choice(questions.get(role, ["Tell me about yourself."]))