from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)


def ask_question(access_token, question):
    """
    向文心一言4.0发送问题，并获取回答。
    """
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token={access_token}"
    payload = {
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def get_access_token():
    """
    使用 API Key 和 Secret Key 获取access_token。
    """
    client_id = "pyIhsEGGlEdQK5Itx7vSHUOi"
    client_secret = "mltXg83hGyqxZMbYemXW1HPVwTEe16tq"
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers)
    return response.json().get("access_token")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask_question', methods=['POST'])
def handle_question():
    data = request.json
    question = data.get('question')
    access_token = get_access_token()
    response = ask_question(access_token, question)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
