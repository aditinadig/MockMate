from transformers import pipeline

# Use top_k=None instead of return_all_scores=True
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def analyze_emotion(response):
    emotions = emotion_analyzer(response)
    top_emotion = max(emotions, key=lambda x: x["score"])["label"]
    return f"Emotion detected: {top_emotion}"