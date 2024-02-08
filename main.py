import gradio as gr
import pyperclip
from convertpdf import convert_to_pdf
from padoc import generate_pa_document
from apidoc import generate_api_documents
from javacode import generate_java_code

def generate_documents(category, project_title=None, date=None, purpose=None, objectives=None, api_parameter=None):
    if category == "P&A Document":
        return f"Generated P&A Document based on the provided idea or requirements:\n"+generate_pa_document(project_title, date, purpose, objectives)
    elif category == "API Documents":
        return f"Generated API Documents based on the provided user stories:\n"+generate_api_documents(api_parameter)
    elif category == "Java Spring Boot Code":
        return f"Generated Java Spring Boot Code based on user stories and API documents:\n"+generate_java_code()
    elif category == "All 3":
        pa_doc = generate_pa_document(project_title, date, purpose, objectives)
        api_doc = generate_api_documents(api_parameter)
        java_code = generate_java_code()
        
    else:
        return "Please select a valid category."

def update_visibility(category):
    print(str(category).casefold())
    
    if str(category).casefold() == "p&a document":
        
        project_title.visible = True
        print(project_title.visible)
        date.visible = True
        purpose.visible = True
        objectives.visible = True
        api_parameter.visible = False
        
    
    elif str(category).casefold() == "api documents":
        project_title.visible = False
        date.visible = False
        purpose.visible = False
        objectives.visible = False
        api_parameter.visible = True
        
    elif str(category).casefold() == "java spring boot code":
        project_title.visible = False
        date.visible = False
        purpose.visible = False
        objectives.visible = False
        api_parameter.visible = False

    return project_title.visible,date.visible,purpose.visible,objectives.visible

def launch_pdf_generation(content_category_tuple):
    content, category = content_category_tuple
    if content is not None:
        convert_to_pdf(category, content)


    


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=25):
            title = gr.HTML("""
                <div style="background-color: #FFCCCB; padding: 10px; text-align: center; border-radius: 10px;">
                    <strong style="font-size: 24px;">Category</strong>
                </div>
            """)
            category = gr.Radio(choices=["P&A Document", "API Documents", "Java Spring Boot Code", "All 3"],  label="Category")
            project_title = gr.Textbox(label="Project Title",visible = False )
            print(project_title.visible)
            date = gr.Textbox(label="Date",visible = False )
            purpose = gr.Textbox(label="Purpose",visible = False)
            objectives = gr.Textbox(label="Objectives",visible = False)
            api_parameter = gr.Textbox(label="API Parameter",visible = False)
            

            category.change(fn=update_visibility, inputs=[category])
            print(f"category:{category}")
        with gr.Column(scale=75):
            title = gr.HTML("""
                <div style="background-color: #FFCCCB; padding: 10px; text-align: center; border-radius: 10px;">
                    <strong style="font-size: 24px;">OneVerse CodeGen App</strong>
                </div>
            """)
            output = gr.TextArea(lines=10, label="Output",show_copy_button=True)
            button = gr.Button("Generate").click(
                    fn=generate_documents,
                    inputs=[category, project_title, date, purpose, objectives, api_parameter],
                    outputs=[output]
                )
            # copy_button = gr.Button("Copy").click(fn=copy_to_clipboard, inputs=[output])
            pdf_button = gr.Button("Convert to PDF").click(fn=convert_to_pdf, inputs=[category,output])
            file_output = gr.File()
            

demo.launch()





