from django.shortcuts import render, redirect
from .forms import TextEntryForm
from .sentiment_model import analyze_sentiment
from .models import TextEntry

def analyze(request):
       if request.method == 'POST':
           form = TextEntryForm(request.POST)
           if form.is_valid():
               text_entry = form.save(commit=False)
               text_entry.sentiment_score = analyze_sentiment(text_entry.text)
               text_entry.save()
               return redirect('result', pk=text_entry.pk)
       else:
           form = TextEntryForm()
       return render(request, 'analyze.html', {'form': form})

from .visualization import generate_sentiment_plot

def result(request, pk):
       text_entry = TextEntry.objects.get(pk=pk)
       sentiment_scores = TextEntry.objects.values_list('sentiment_score', flat=True)
       plot_data = generate_sentiment_plot(sentiment_scores)
       return render(request, 'result.html', {'text_entry': text_entry, 'plot_data': plot_data})

