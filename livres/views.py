from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Livre
from .forms import LivreForm
import requests

# Create your views here.

def livre_list(request):
    livres = Livre.objects.all()
    return render(request, 'livres/livre_list.html', {'livres': livres})

def livre_add(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livre_list')
    else:
        form = LivreForm()
    return render(request, 'livres/livre_form.html', {'form': form})

def livre_edit(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('livre_list')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'livres/livre_form.html', {'form': form})

def livre_delete(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        livre.delete()
        return redirect('livre_list')
    return render(request, 'livres/livre_confirm_delete.html', {'livre': livre})

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = generate_chatbot_response(user_message)
        return JsonResponse({'response': response})
    return render(request, 'livres/chatbot.html')

def generate_chatbot_response(message):
    # Query DB based on message
    livres = Livre.objects.all()
    context = "\n".join([f"ID: {l.id_livre}, Title: {l.titre}, Author: {l.auteur}, Status: {l.statut}, Quantity: {l.quantite_disponible}" for l in livres])
    
    prompt = f"""
You are a library chatbot. Answer questions about books using the following data from the database:

{context}

User question: {message}

Provide a helpful response in French, using the data above. If the question is about availability, check the status and quantity.
For recommendations, suggest based on category or author.
"""
    
    # Call Ollama
    try:
        response = requests.post('http://localhost:11434/api/generate', json={
            'model': 'mistral',
            'prompt': prompt,
            'stream': False
        })
        if response.status_code == 200:
            return response.json()['response']
        else:
            return "Désolé, je ne peux pas répondre pour le moment."
    except:
        return "Erreur de connexion à l'IA."
