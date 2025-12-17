\# Shopify AI Assignment



This project demonstrates a simple integration between:

\- A Ruby on Rails API backend

\- A Python FastAPI AI service



The Rails API sends text to the Python service and returns the AI-processed result.



---



\## Tech Stack



\- Ruby on Rails 8 (API mode)

\- Ruby 3.x

\- Python 3.12

\- FastAPI

\- Uvicorn



---



\## Project Structure



shopify-ai-assignment/

├── rails\_api/

├── ai\_service/

└── screenshots/



---



\## How to Run



\### Start Python AI Service



cd ai\_service

venv\\Scripts\\activate

uvicorn main:app --reload --port 8000



Python runs at:

http://127.0.0.1:8000



---



\### Start Rails API



cd rails\_api

rails s



Rails runs at:

http://127.0.0.1:3000



---



\### Test API Integration



curl -X POST http://127.0.0.1:3000/analyze ^

-H "Content-Type: application/json" ^

-d "{\\"text\\":\\"hello shopify ai\\"}"



Expected Response:



{

&nbsp; "original\_text": "hello shopify ai",

&nbsp; "ai\_result": "HELLO SHOPIFY AI"

}



---



\## Screenshots



\- screenshots/python\_server.png

\- screenshots/rails\_server.png

\- screenshots/curl\_success.png



