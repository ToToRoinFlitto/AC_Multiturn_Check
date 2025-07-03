# ========================================
# Author: Soohyun Lee
# Date: 2025-06-02
# ========================================


import openai
import os
from dotenv import load_dotenv

load_dotenv()  # .env에서 환경변수 불러오기
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_chat_completion(system_prompt: str, user_prompt: str, model="gpt-4o"):
    response = openai.ChatCompletion.create(
        
        model=model,
        
        messages=[
            
            {"role": "system", 
             "content": system_prompt},
            
            {"role": "user", 
             "content": user_prompt}
            
        ],
        
        temperature=0
    )
    
    return response["choices"][0]["message"]["content"]
