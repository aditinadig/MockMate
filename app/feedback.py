from app.relevance_analysis import compute_similarity
from app.emotion_analysis import analyze_emotion

def compute_score(relevance, tone, word_count):
    """Compute a score for the response."""
    # Relevance: Semantic similarity (scaled from 0–4)
    relevance_score = (
        4 if relevance > 0.8 else
        3 if relevance > 0.6 else
        2 if relevance > 0.4 else
        1 if relevance > 0.2 else 0
    )
    
    # Tone: Positive or confident tone (scaled from 0–3)
    tone_score = (
        3 if tone in ["confident", "positive"] else
        2 if tone in ["neutral"] else
        1 if tone in ["anxious"] else 0
    )
    
    # Length: Appropriateness of response length (scaled from 0–3)
    length_score = (
        3 if 20 <= word_count <= 100 else
        2 if 10 <= word_count < 20 or 100 < word_count <= 150 else
        1 if word_count < 10 or word_count > 150 else 0
    )
    
    # Total score (max 10 points)
    total_score = min(relevance_score + tone_score + length_score, 10)
    return total_score, relevance_score, tone_score, length_score

def evaluate_response(role, question, response):
    """Evaluate the user's response, provide feedback, and assign a score."""

    # Length analysis
    word_count = len(response.split())
    length_feedback = (
        "Your response length is appropriate."
        if 20 <= word_count <= 100 else
        "Your response is too short. Add more details." if word_count < 20 else
        "Your response is too long. Focus on the key points."
    )

    # Relevance analysis
    relevance_score = compute_similarity(question, response)
    relevance_feedback = (
        "Excellent! Your response aligns very well with the question."
        if relevance_score > 0.8 else
        "Good, but your response could be more specific to the question."
        if relevance_score > 0.6 else
        "Your response lacks alignment with the question. Address the main topic."
    )

    # Emotion analysis
    tone = analyze_emotion(response)
    emotion_feedback = (
        "Your tone is confident and positive."
        if tone in ["confident", "positive"] else
        "Your tone is neutral. Adding enthusiasm might help."
        if tone == "neutral" else
        "Your tone appears negative. Frame your response more positively."
    )

    # Role-specific feedback
    if role == "Software Developer":
        role_feedback = (
            "Ensure your answer demonstrates technical understanding and coding practices."
            if "code" not in response.lower()
            else "Good job mentioning technical concepts! Elaborate with examples."
        )
    elif role == "Data Scientist":
        role_feedback = (
            "Mention specific methods or metrics to strengthen your response."
            if "data" not in response.lower()
            else "Good response! Including more examples would make it stronger."
        )
    elif role == "Product Manager":
        role_feedback = (
            "Highlight team dynamics and leadership skills to enhance your response."
            if "team" not in response.lower()
            else "Excellent! Your answer showcases leadership and team coordination."
        )
    else:
        role_feedback = "Tailor your response to the key skills relevant to the role."

    # Calculate score
    total_score, relevance_score, tone_score, length_score = compute_score(
        relevance_score, tone, word_count
    )

    # Combine all feedback
    feedback = [
        f"Overall Score: {total_score}/10",
        f"Relevance Score: {relevance_score}/4",
        f"Tone Score: {tone_score}/3",
        f"Length Score: {length_score}/3",
        length_feedback,
        relevance_feedback,
        emotion_feedback,
        role_feedback,
    ]

    return "\n".join(feedback)