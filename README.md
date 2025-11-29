```markdown
# TDS Sep 2025 – LLM Analysis Quiz Solver

A FastAPI-based automated quiz solver that can handle data sourcing, preparation, analysis, and visualization tasks using headless browser automation.

## 🚀 Features

- **Secure API Endpoint** - Verifies email and secret before processing
- **Headless Browser Automation** - Uses Playwright to handle JavaScript-rendered pages
- **Multi-format Support** - Parses PDF, CSV, Excel, and web content
- **Data Analysis** - Performs calculations, aggregations, and transformations
- **Visualization** - Generates charts and plots when required
- **Chain Quizzes** - Automatically follows quiz sequences within 3-minute time limit

## 📁 Project Structure

```
tds-llm-analysis-quiz/
│
├── app/
│   ├── main.py              # FastAPI server and endpoint handler
│   ├── solver.py            # Main quiz solving logic
│   ├── browser.py           # Headless browser automation
│   ├── submit.py            # Answer submission handler
│   └── utils/
│       ├── parser.py        # HTML/JavaScript content parsing
│       ├── analysis.py      # Data analysis and computation
│
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── LICENSE               # MIT License
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/tds-llm-analysis-quiz.git
   cd tds-llm-analysis-quiz
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## 🚀 Quick Start

1. **Set environment variable**
   ```bash
   export TDS_SECRET="your-secret-here"
   ```

2. **Run the server**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

3. **Test the endpoint**
   ```bash
   curl -X POST http://localhost:8000/ \
     -H "Content-Type: application/json" \
     -d '{
       "email": "your-email@example.com",
       "secret": "your-secret-here",
       "url": "https://example.com/quiz-123"
     }'
   ```

## 📡 API Endpoint

**POST** `http://localhost:8000/`

**Request Body:**
```json
{
  "email": "string",
  "secret": "string", 
  "url": "string"
}
```

**Response:**
```json
{
  "final_status": "completed",
  "solved_quizzes": 3,
  "results": [
    {
      "quiz_url": "https://example.com/quiz-123",
      "answer": 42,
      "result": {
        "correct": true,
        "url": "https://example.com/quiz-456"
      }
    }
  ]
}
```

## 🎯 Supported Quiz Types

- **Web Scraping** - Extract data from JavaScript-rendered pages
- **File Processing** - Parse PDF, CSV, Excel files
- **Data Analysis** - Sum, average, filter, aggregate data
- **API Integration** - Fetch data from REST APIs
- **Visualization** - Generate charts and plots
- **Text Processing** - Clean and transform text data

## 🔧 Configuration

### Environment Variables
- `TDS_SECRET` - Your secret key for API authentication

### Time Limits
- **3 minutes** total for entire quiz chain
- **30 seconds** per individual request
- Automatic timeout handling

## 🐳 Docker Deployment

1. **Build the image**
   ```bash
   docker build -t tds-quiz-solver .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 -e TDS_SECRET="your-secret" tds-quiz-solver
   ```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Email: your-email@example.com
```

**Key improvements made:**
- ✅ Fixed formatting and structure
- ✅ Added proper installation instructions
- ✅ Added API documentation with examples
- ✅ Added features list
- ✅ Added configuration section
- ✅ Added Docker deployment instructions
- ✅ Added testing section
- ✅ Added license and contributing sections

**Now save this as `README.md` in your project root and push to GitHub!**