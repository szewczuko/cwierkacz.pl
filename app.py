from flask import Flask, redirect

app = Flask("ćwierkacz.pl")

@app.route('/')
def main_page():
    return redirect("https://twitter.com", code=302)

@app.route('/<path:url>')
def redirect_to_example(url):
    return redirect(f'http://twitter.com/{url}', code=302)

if __name__ == '__main__':
    app.run(port=1337)