from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

@app.route('/processar', methods=['POST'])
def processar_arquivo():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400

    try:
        if file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return jsonify({"error": "Formato de arquivo não suportado"}), 400
        
        # Média
        df['media'] = df[['nota_1', 'nota_2']].mean(axis=1)
        
        print(jsonify(df.to_dict(orient='records')))

        # Retorna JSON
        return jsonify(df.to_dict(orient='records')) 
    
    except Exception as e:
        return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
