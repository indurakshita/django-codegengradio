from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_to_pdf(path,content):
    
    lines = content.strip().split("\n")  
    file_name = path + ".pdf"
    print(file_name)
   
    pdf_canvas = canvas.Canvas(file_name, pagesize=letter)
    y = 700
    pdf_canvas.setFont("Helvetica", 12)
    for line in lines:
        pdf_canvas.drawString(100, y, line)
        y -= 20 
    pdf_canvas.save()
    
    return file_name


# def convert_to_pdf(path, content, category):
#     lines = content.strip().split("\n")
    
#     # Determine file name based on category
#     if category == "P&A Document":
#         file_name = os.path.join(path, "pa_document.pdf")
#     elif category == "API Documents":
#         file_name = os.path.join(path, "api_documents.pdf")
#     elif category == "Java Spring Boot Code":
#         file_name = os.path.join(path, "java_code.pdf")
#     elif category == "All 3":
#         file_name = os.path.join(path, "all_documents.pdf")
#     else:
#         raise ValueError("Invalid category provided")
   
#     # Create PDF
#     pdf_canvas = canvas.Canvas(file_name, pagesize=letter)
#     y = 700
#     pdf_canvas.setFont("Helvetica", 12)
#     for line in lines:
#         pdf_canvas.drawString(100, y, line)
#         y -= 20 
#     pdf_canvas.save()
    
#     return file_name