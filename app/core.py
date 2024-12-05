from app.feedback import evaluate_response
from app.question_bank import generate_question
import gradio as gr

def start_app():
    with gr.Blocks() as app:
        gr.Markdown("# MockMate: AI-Powered Job Interview Coach")
        gr.Markdown("Get dynamic questions and actionable feedback on your responses.")

        # Store the initial question
        role = gr.Dropdown(["Software Developer", "Data Scientist", "Product Manager"],
                           label="Select Job Role", value="Software Developer")
        question = gr.Textbox(label="Generated Question", value="Generating your first question...", interactive=False)

        # Generate the initial question when the app loads
        def initialize_question(role):
            return generate_question(role)

        # Generate a new question
        def next_question(role):
            return generate_question(role)

        # Input for user's response
        response = gr.Textbox(label="Your Response", placeholder="Type your answer here...", lines=5)
        feedback = gr.Textbox(label="Feedback", interactive=False, lines=5)

        # Submit response and get feedback
        def submit_response(role, question, response):
            feedback_text = evaluate_response(role, question, response)
            new_question = generate_question(role)  # Prepare next question for multi-rounds
            return feedback_text, new_question

        # Buttons for interaction
        submit_btn = gr.Button("Submit Response")
        next_btn = gr.Button("Next Question")

        # Link buttons to their respective functions
        submit_btn.click(submit_response, inputs=[role, question, response], outputs=[feedback, question])
        next_btn.click(next_question, inputs=[role], outputs=[question])

        # Initialize the first question
        question.value = initialize_question(role.value)

        app.launch()