from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def evaluate_response(role, question, response):
    sentiment = analyzer.polarity_scores(response)
    tone = "Positive" if sentiment["compound"] > 0.2 else "Neutral" if sentiment["compound"] > -0.2 else "Negative"
    feedback = []
    if len(response.split()) < 20:
        feedback.append("Your response could be more detailed.")
    if tone == "Negative":
        feedback.append("Try to maintain a more positive tone.")
    feedback.append("Good job staying relevant to the question!")
    return " ".join(feedback)