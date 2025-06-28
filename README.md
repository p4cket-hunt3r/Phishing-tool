# Phishing Link Generator - Educational Cybersecurity Tool

---

## 📌 About This Tool:

This is a **Python-based phishing simulation tool** built using Flask.  
It allows ethical hackers, students, and cybersecurity learners to **simulate phishing attacks for educational and awareness purposes**.

### ✅ Features:

- Generates fake login pages for popular platforms (Facebook, Instagram, Twitter)
- Captures username and password entered by the victim
- Displays captured data live in the terminal
- Saves all captured credentials to a file (`captured_data.txt`)
- Platform selection menu for easy targeting
- No external HTML files (everything in one Python file)
- Can run on Termux, Linux, and Windows

---

## 📋 Requirements:

| Requirement | Details |
|---|---|
| Python Version | Python 3.x |
| Python Packages | Flask |
| OS Support | Termux (Android), Linux (Ubuntu/Kali/Debian), Windows (CMD/PowerShell) |

---

## ⚙️ Installation Instructions:

---

### ✅ Termux (Android):

```
pkg update && pkg upgrade
pkg install python
pip install flask

```
---

✅ Linux (Ubuntu / Kali / Debian):
```
sudo apt update && sudo apt install python3 python3-pip
pip3 install flask

```
---

✅ Windows:

1. Download and install Python 3.x from:
https://www.python.org/downloads/


2. Open CMD or PowerShell:


```
pip install flask
```

---

🚀 How to Run the Tool:
```
python phishing_link_generator.py
```
✅ After running:

A platform selection menu will appear (Facebook / Instagram / Twitter)

Choose the desired target platform

The tool will generate a local URL like:


http://127.0.0.1:5000/facebook/login.php

✅ Open this URL on your browser (on the same device).

When a victim submits credentials:

Username and Password will appear live in your terminal

Also saved inside: captured_data.txt



---

✅ Important Notes:

This tool runs on localhost (127.0.0.1) for ethical testing only.

For external/public testing, you'd need port forwarding (like Ngrok) or DNS spoofing, which is beyond the scope of this README.



---

⚠️ Legal Disclaimer:

This tool is intended strictly for educational purposes, cybersecurity awareness, and ethical hacking practice only.

By using this tool, you agree to the following:

✅ You will only use this tool in authorized environments (your own devices, labs, or with written permission).

✅ You will NOT use this for illegal phishing, harassment, or real-world cybercrime.

✅ The author ("p4cket-hunt3r") is NOT responsible for any misuse, data loss, or legal issues arising from improper use.




---

✅ License:

MIT License – 2025 – p4cket-hunt3r
Free to use, modify, and distribute.
You must give credit to the author (p4cket-hunt3r).
No warranty. No liability.


---

✅ Stay Ethical. Stay Legal.
✅ For Cybersecurity Learning Only.

---


👤 Author:




username:```p4cket-hunt3r```
