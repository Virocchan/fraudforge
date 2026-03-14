from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        api_key = request.headers.get('X-API-Key', '')

        if not api_key:
            return jsonify({'error': 'Missing API key'}), 401

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=data.get('messages', []),
            temperature=0.2,
            max_tokens=2048
        )

        return jsonify({
            'choices': [{
                'message': {
                    'content': response.choices[0].message.content
                }
            }]
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("✅ FraudForge proxy running at http://localhost:8181")
    app.run(port=8181, debug=False)
