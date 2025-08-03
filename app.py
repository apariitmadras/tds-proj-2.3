from flask import Flask, request, jsonify
import json
import re
import base64
import io
import os
from dotenv import load_dotenv
from data_analyzer import DataAnalyzer

load_dotenv()

app = Flask(__name__)
analyzer = DataAnalyzer()

@app.route('/api/', methods=['POST'])
def analyze_data():
    try:
        # Get the question from the request
        if 'file' in request.files:
            file = request.files['file']
            question = file.read().decode('utf-8')
        else:
            question = request.get_data(as_text=True)
        
        # Process the question
        result = analyzer.process_question(question)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)