from bs4 import BeautifulSoup
import re
import base64
from urllib.parse import urljoin

async def extract_quiz_info(html, current_url):
    """Extract quiz instructions, files, and submit URL from page"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get all text content
    question_text = soup.get_text(separator='\n', strip=True)
    
    # Find submit URL (look in script tags and text)
    submit_url = None
    
    # Method 1: Look for base64 encoded instructions (like in project description)
    for script in soup.find_all('script'):
        if script.string and 'atob' in script.string:
            # Extract base64 content
            base64_matches = re.findall(r'atob\([\'"]([A-Za-z0-9+/=]+)[\'"]\)', script.string)
            for base64_content in base64_matches:
                try:
                    decoded = base64.b64decode(base64_content).decode('utf-8')
                    # Look for submit URL in decoded content
                    url_matches = re.findall(r'https?://[^\s"\']+', decoded)
                    for url in url_matches:
                        if 'submit' in url:
                            submit_url = url
                            break
                except:
                    pass
    
    # Method 2: Look in script tags
    if not submit_url:
        for script in soup.find_all('script'):
            if script.string:
                script_text = script.string
                # Look for submit URLs in JavaScript
                url_matches = re.findall(r'https?://[^\s"\']+', script_text)
                for url in url_matches:
                    if 'submit' in url:
                        submit_url = url
                        break
    
    # Method 3: Look in entire page text
    if not submit_url:
        url_matches = re.findall(r'https?://[^\s]+', html)
        for url in url_matches:
            if 'submit' in url:
                submit_url = url
                break
    
    # Clean URL - remove HTML tags if any
    if submit_url:
        submit_url = re.sub(r'<[^>]+>', '', submit_url)
    
    # Find all downloadable files
    file_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Make absolute URL
        absolute_url = urljoin(current_url, href)
        if any(absolute_url.endswith(ext) for ext in ['.pdf', '.csv', '.xlsx', '.json', '.txt']):
            file_links.append(absolute_url)
    
    return {
        "question_text": question_text,
        "file_links": file_links,
        "submit_url": submit_url,
        "full_html": html
    }