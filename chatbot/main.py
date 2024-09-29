from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os
import fpdf

template =  """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Please respond in 1-2 sentences

Answer:
"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain  = prompt | model

#all answers to this should be concise. 1-2 sentences. they should allow for review. Feed this prompt to the ai with minimal tokens/instructions.
#take in user questions to a list, and print ai output. also store this output to a list. actually, skip the list alltogether. use a dict.

#'why is coding hard" --> coding is hard becuase there is some stupid little kid across the world who is better than you

#keep this stored. Maybe don't display ai, responses, as it takes a while

def handle_conversation():
    context = ""
    #user_dict = {}
    questionsAndAnswers = {}
    print("Welcome to Simple Notes  --- Developed by Nicholas Corcoran and Rachel Gaff\n")
    input("Please enter the block of text that you would like to study:")
    
    os.system('cls') #clear screen
    print("""
Please skim through your text and write down any questions that you may have
These should be specific enough to jog your memory, but simple enough to understand
          
Example: "What year was Hack UMBC first held in?" --- Specific, but simple
          """)
    while True:
        user_input = input("Ask a question about the text. Type 'exit' when you're done\n")
        
        if user_input.lower() == "exit":
            break
        user_input = user_input.replace('\n',' ')
        result = chain.invoke({"context": context, "question": user_input})
        questionsAndAnswers[user_input] = result
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"
        #user_dict[user_input] = result
    for question, answer in questionsAndAnswers.items():
        print(f"{question} --> {answer}")

    return questionsAndAnswers

def createPdf(questionsAndAnswers):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=8)
    pdf.cell(0, 10, txt="Made with SimpleNotes", ln=True)
    pdf.set_font("Arial", size=12)
    name = input("What is your name? \n")
    class_ = input("What class is this for?\n")
    date = input("What is today's date\n")
    topic = input("What topic are you studying?\n")
    pdf.cell(0, 10, txt=f"Name: {name}          Class: {class_}          {date}", ln=True)
    pdf.set_font("Arial", size=16)
    pdf.cell(0, 10, txt=topic, ln=True)

    for question, answer in questionsAndAnswers.items():
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt=f"Q: {question}", ln=True)  # Print the question
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, txt=f"A: {answer}")         # Print the answer

    pdf.output("Simple_Notes_Study_Document.pdf")  # Ensure to add .pdf extension



if __name__ == "__main__":
    createPdf(handle_conversation())