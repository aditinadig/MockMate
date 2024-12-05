import gradio as gr
from app.feedback import evaluate_response
from app.question_bank import generate_question

def start_app():
    with gr.Blocks() as app:
        gr.Markdown("# MockMate: AI-Powered Job Interview Coach")

        with gr.Row():
            role = gr.Dropdown(["Software Developer", "Data Scientist", "Product Manager"], 
                               label="Select Role", value="Software Developer")
            question = gr.Textbox(label="Generated Question", interactive=False)

        generate_btn = gr.Button("Generate Question")
        generate_btn.click(generate_question, inputs=[role], outputs=[question])

        response = gr.Textbox(label="Your Response", placeholder="Type your answer...")
        feedback = gr.Textbox(label="Feedback", interactive=False)

        feedback_btn = gr.Button("Get Feedback")
        feedback_btn.click(evaluate_response, inputs=[role, question, response], outputs=[feedback])

        app.launch()