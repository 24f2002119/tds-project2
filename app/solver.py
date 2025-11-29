import time
import requests
from app.browser import load_quiz_page
from app.utils.parser import extract_quiz_info
from app.utils.analysis import compute_answer
from app.submit import submit_answer

async def solve_quiz(email, secret, start_url, start_time):
    current_url = start_url
    results = []
    
    while current_url and (time.time() - start_time < 170):  # 3 minutes limit
        print(f"Solving quiz: {current_url}")
        
        # Load quiz page
        page_html = await load_quiz_page(current_url)
        
        # Extract quiz information
        quiz_info = await extract_quiz_info(page_html, current_url)
        
        # Compute answer
        answer = await compute_answer(quiz_info)
        
        # Submit answer
        submission_result = await submit_answer(
            email=email,
            secret=secret,
            quiz_url=current_url,
            answer=answer,
            submit_url=quiz_info.get("submit_url")
        )
        
        results.append({
            "quiz_url": current_url,
            "answer": answer,
            "result": submission_result
        })
        
        # Check if we got next URL
        if submission_result.get("correct") and submission_result.get("url"):
            current_url = submission_result["url"]
            print(f"Moving to next quiz: {current_url}")
        else:
            current_url = None
    
    return {
        "final_status": "completed",
        "solved_quizzes": len(results),
        "results": results
    }