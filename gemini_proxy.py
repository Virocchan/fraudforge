from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        api_key = request.headers.get('X-API-Key', '')

        if not api_key:
            return jsonify({'error': 'Missing API key'}), 401

        client = genai.Client(api_key=api_key)
        prompt = data.get('messages', [{}])[-1].get('content', '')

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )

        return jsonify({
            'choices': [{
                'message': {
                    'content': response.text
                }
            }]
        })

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("✅ FraudForge proxy running at http://localhost:8181")
    app.run(port=8181, debug=False)
