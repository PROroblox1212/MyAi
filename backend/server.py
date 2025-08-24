from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ai_model import ask_ai
from web_search import search_web

app = FastAPI()

# Autoriser le frontend à parler au backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    
    # IA réfléchit
    response = ask_ai(user_input)
    
    # Si l’IA a besoin d’infos du web
    if "[SEARCH]" in response:
        query = response.replace("[SEARCH]", "").strip()
        web_data = search_web(query)
        response = ask_ai(f"Infos trouvées sur le web: {web_data}. Réponds à la question : {user_input}")
    
    return {"reply": response}
