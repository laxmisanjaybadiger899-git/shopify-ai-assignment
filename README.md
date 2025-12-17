# Shopify AI Assignment

This project demonstrates a simple integration between:
- A Ruby on Rails API backend
- A Python FastAPI AI service

The Rails API sends text to the Python service and returns the AI-processed response.



## Tech Stack

- Ruby on Rails 8 (API mode)
- Ruby 3.x
- Python 3.12
- FastAPI
- Uvicorn



## Project Structure
## Project Structure



shopify-ai-assignment/
├── rails_api/        # Rails backend
├── ai_service/       # Python FastAPI service
└── screenshots/      # Screenshots of running services and API test



## How to Run the Project

### 1. Start Python AI Service

cd ai_service  
venv\Scripts\activate  
uvicorn main:app --reload --port 8000  

Python service runs at:
http://127.0.0.1:8000



### 2. Start Rails API Server

cd rails_api  
rails s  

Rails server runs at:
http://127.0.0.1:3000



### 3. Test the Integration

curl -X POST http://127.0.0.1:3000/analyze ^
-H "Content-Type: application/json" ^
-d "{\"text\":\"hello shopify ai\"}"

Expected Response:

{
  "original_text": "hello shopify ai",
  "ai_result": "HELLO SHOPIFY AI"
}



## Screenshots Included

- rails_server.png
- python_server.png
- curl_success.png
