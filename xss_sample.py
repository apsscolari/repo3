from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    # Rendering user input directly in the response without sanitizing
    html = f"<h1>Hello, {name}!</h1>"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
