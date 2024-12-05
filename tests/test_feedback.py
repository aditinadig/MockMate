import unittest
from app.feedback import evaluate_response

class TestFeedback(unittest.TestCase):
    def test_relevance(self):
        feedback = evaluate_response(
            role="Software Developer",
            question="What is polymorphism?",
            response="Polymorphism allows objects to be treated as instances of their parent class."
        )
        self.assertIn("Your response aligns well with the question", feedback)

    def test_emotion(self):
        feedback = evaluate_response(
            role="Product Manager",
            question="How do you resolve conflicts?",
            response="I always try to remain calm and mediate discussions."
        )
        self.assertIn("Emotion detected: calm", feedback)  # Adjust based on expected model output

if __name__ == "__main__":
    unittest.main()