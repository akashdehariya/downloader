from flask import Flask, request, send_file
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "डाउनलोडिंग वेबसाइट लाइव है!"

@app.route('/download')
def download():
    url = request.args.get("url")
    if not url:
        return "URL नहीं मिला!", 400

    filename = url.split("/")[-1]
    response = requests.get(url, stream=True)
    
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
