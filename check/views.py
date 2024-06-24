import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Use the loaded API key
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "kamu adalah orang yang bisa melihat kepribadian diri seseorang dengan nama, analisislah kepribadian dari nama yang diberikan"},
                {"role": "user", "content": f"analisis kepribadianku. namaku {name}. jawablah dengan 1 paragraf deskripsi dengan singkat padat dan jelas dalam bahasa indonesia."}
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
        )
        
        # Ambil konten pesan dari respons
        response_content = chat_completion.choices[0].message.content
        return render(request, "check/index.html", {"response_data": response_content})
    else:
        return render(request, "check/index.html", {"response_data": None})
