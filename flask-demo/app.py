from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# serve the /static/index.html file by default
@app.route('/')
def serve_static_page():
    return app.send_static_file('index.html')

# API endpoint returning JSON
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")

# POST route
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(received=data)


@app.route('/api/notification', methods=['POST'])
def send_notification():
    data = request.get_json()

    # Input validation
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    # Send notification
    try:
        response = requests.post('https://ntfy.sh/flo85', json={'message': message})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Notification failed: {str(e)}'}), 500

    return jsonify({'status': 'Notification sent successfully'}), 200


if __name__ == '__main__':
    app.run(debug=False)

