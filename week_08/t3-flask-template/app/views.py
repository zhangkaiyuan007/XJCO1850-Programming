import os
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from flask import render_template, request, redirect, url_for
from app import app

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    graph_url = None
    table_html = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            df = pd.read_csv(file_path)
            
            product_counts = df['Product'].value_counts()
            
            plt.figure(figsize=(10, 6))
            product_counts.plot(kind='bar', color='teal')
            plt.title('Most Popular Items')
            plt.xlabel('Product')
            plt.ylabel('Frequency')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            graph_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
            
            table_html = df.to_html(classes='table table-hover table-bordered', index=False)
            
    return render_template('home.html', graph_url=graph_url, table_html=table_html)