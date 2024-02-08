def generate_pa_document(project_title, date, purpose, objectives):
    document = ''
    if project_title is not None and date is not None and purpose is not None and objectives is not None:
        document += f"Project Title: {project_title}\n"
        document += f"Date: {date}\n"
        document += f"Purpose: {purpose}\n"
        document += f"Objectives: {objectives}\n"
    else:
        document += "Some fields are missing. Please provide all required information."
    return document


# import requests

# def generate_pa_document(project_title, date, purpose, objectives):
#     # Construct the request payload
#     payload = {
#         "project_title": project_title,
#         "date": date,
#         "purpose": purpose,
#         "objectives": objectives
#     }
    
#     # Make a POST request to the API endpoint
#     api_url = "https://example.com/generate_pa_document"  # Replace with your API endpoint
#     response = requests.post(api_url, json=payload)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         return response.text
#     else:
        # return f"Error: Failed to generate P&A document. Status code: {response.status_code}"
