import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_sentiment_plot(sentiment_scores):
       plt.figure(figsize=(10, 6))
       plt.hist(sentiment_scores, bins=20, color='skyblue', edgecolor='black')
       plt.title('Sentiment Score Distribution')
       plt.xlabel('Sentiment Score')
       plt.ylabel('Frequency')

       buffer = BytesIO()
       plt.savefig(buffer, format='png')
       buffer.seek(0)
       plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
       plt.close()
       return plot_data