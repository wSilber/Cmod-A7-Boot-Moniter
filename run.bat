set FLASK_APP=main.py
cmd /c "pip install -r requirements.txt"
start cmd /k "python -m flask run"
start chrome.exe -new-tab "127.0.0.1:5000"