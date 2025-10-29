from flask import Flask , render_template , request
app = Flask(__name__)
@app.route("/")
def index():
     return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def genarete():
    message = "Initial Text"
    if request.method == 'POST':
        if 'change_text_btn' in request.form:
            message = "Text Changed by Button!"
    return render_template('index.html', message=message)

if __name__ == "__main__": 
     app.run(debug=True, port=3003)