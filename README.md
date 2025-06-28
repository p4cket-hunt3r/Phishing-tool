# Phishing Link Generator (Python Flask)

## ❗ DISCLAIMER:

This tool is **for educational purposes only** (cybersecurity training, ethical hacking labs, college projects, or personal awareness demos).  
**Do not use for illegal activities or real-world phishing attacks.**  
Unauthorized phishing is a criminal offense under cybercrime laws.

---

## 📌 Project Description:

A simple single-file Python Flask app that creates fake social media login pages (Facebook, Instagram, Twitter).  
When someone enters login details, the **username and password will appear live on your terminal** and also saved in a text file (`captured_data.txt`).

---

## ✅ Supported Operating Systems:

| OS | Supported |
|---|---|
| **Termux (Android)** | ✅ |
| **Linux (Ubuntu, Kali, Debian, etc.)** | ✅ |
| **Windows (CMD / PowerShell)** | ✅ |

---

## ✅ Tool Features:

- Single Python file (No external HTML/PHP needed)
- Fake login pages for:  
  ✅ Facebook  
  ✅ Instagram  
  ✅ Twitter
- Captures victim's username and password
- Shows captured data **live in your terminal**
- Saves captured data in a text file
- Auto-install Flask if not already installed
- Runs fully on localhost (127.0.0.1:5000)

---

## ✅ Installation and Running Guide:

---

### 🖥️ For Termux (Android):

```
pkg update && pkg upgrade
pkg install python
pip install flask
python phishing_link_generator.py

Then open your browser and go to:
http://127.0.0.1:5000/

```
---

🐧 For Linux (Ubuntu/Kali/Debian):
```
sudo apt update && sudo apt install python3 python3-pip
pip3 install flask
python3 phishing_link_generator.py

Access in browser:
http://127.0.0.1:5000/

```
---

🪟 For Windows (CMD or PowerShell):

1. Install Python from https://www.python.org/downloads/


2. Open CMD or PowerShell:


```
pip install flask
python phishing_link_generator.py

Access via browser:
http://127.0.0.1:5000/

```
---

✅ How to Use:

1. Run the Python script:


```
python phishing_generator.py
```
2. Terminal will show:



[+] Phishing server running at http://127.0.0.1:5000

3. Open browser and test:



Fake Page	URL

Home Menu	http://127.0.0.1:5000/
Facebook	http://127.0.0.1:5000/facebook
Instagram	http://127.0.0.1:5000/instagram
Twitter	http://127.0.0.1:5000/twitter


4. When someone enters username and password and clicks login:



✅ You will instantly see this in your Terminal:

[+] Captured Login:
Facebook - Username: victim_user | Password: victim_pass

✅ It will also save to:

captured_data.txt


---

✅ Optional: Exposing Public Link (Ngrok)

If you want to demo over internet (for testing only):

./ngrok http 5000

Ngrok will give a public URL like:
https://abc123.ngrok.io/facebook

✅ Do not send public links to real people. Test only on yourself.


---

✅ Project Folder Structure:

phishing_link_generator/
├── phishing_generator.py
├── captured_data.txt
└── README.md


---

✅ Extra Features (Optional to Add):

IP address capture

Timestamp logging

More fake sites (Gmail, Snapchat, etc.)



---

✅ Author:
```
p4cket-hunt3r 
```

---


# ⚠️ Legal Disclaimer:

This project is developed **strictly for educational purposes, cybersecurity awareness, and ethical hacking training only**.  
It is intended for:

- Cybersecurity students  
- Ethical hacking labs  
- Penetration testing practice environments  
- Academic research and demonstration  

**By using this tool, you agree to the following conditions:**

1. You will **NOT use this tool for any illegal activities**, unauthorized testing, or real-world phishing attacks.
2. You will **only use this tool on systems you own or have explicit written permission to test**.
3. The creator (p4cket-hunt3r), contributors, and any distributing platforms (GitHub, etc.) are **not responsible for any misuse or damage caused** by this tool.



✅ **Always practice ethical hacking responsibly.**
