import fpdf

def createPdf(questionsAndAnswers):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for question, answer in questionsAndAnswers.items():
        pdf.cell(0, 10, txt=f"Q: {question}", ln=True)  # Print the question
        pdf.multi_cell(0, 10, txt=f"A: {answer}")         # Print the answer

    pdf.output("Simple_Notes_Study_Document.pdf")  # Ensure to add .pdf extension

# Example usage
questions_and_answers = {
    "What is Python?": "Python is a programming language that lets you work quickly and integrate systems more effectively.",
    "What is FPDF?": "FPDF is a PHP class which allows generating PDF files with pure PHP."
}

createPdf(questions_and_answers)
