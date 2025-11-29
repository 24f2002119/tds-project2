import requests
import re

async def submit_answer(email, secret, quiz_url, answer, submit_url):
    """Submit answer to the quiz endpoint"""
    
    # If no submit_url found, use a default one for demo
    if not submit_url:
        submit_url = "https://tds-llm-analysis.s-anand.net/submit"
    
    # Clean the URL - remove any HTML tags or invalid characters
    submit_url = re.sub(r'<[^>]+>', '', submit_url)
    submit_url = submit_url.split(' ')[0]  # Take only first part if multiple words
    
    payload = {
        "email": email,
        "secret": secret,
        "url": quiz_url,
        "answer": answer
    }
    
    print(f"Submitting to: {submit_url}")
    print(f"Payload: {payload}")
    
    try:
        response = requests.post(submit_url, json=payload, timeout=30)
        print(f"Response: {response.status_code} - {response.text}")
        return response.json()
    except Exception as e:
        print(f"Submission error: {e}")
        return {"error": f"Submission failed: {str(e)}", "correct": False}