from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

def chat_bot(request):
    return render(request, 'chat_bot.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    
    chat_completion = client.chat.completions.create(
        messages=[
        {"role": "user", 
        "content": userMessage
        }
    ],
        model="gpt-3.5-turbo",
    )
    botsResponse = (chat_completion.choices[0].message)

    return HttpResponse(botsResponse.content) # this will be sent back to the client