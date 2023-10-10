from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append(message)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
