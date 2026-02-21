from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "messages.txt"

# ===== HELPER FUNCTIONS =====
def load_messages():
    """Load messages from file, return as list of dicts."""
    messages = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():  # skip empty lines
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        msg_id, name, text, timestamp = parts
                        messages.append({
                            "id": int(msg_id),
                            "name": name,
                            "text": text,
                            "timestamp": timestamp
                        })
    return messages

def save_messages(messages):
    """Save list of message dicts to file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for msg in messages:
            f.write(f"{msg['id']}|{msg['name']}|{msg['text']}|{msg['timestamp']}\n")

# ===== ROUTES =====
@app.route("/", methods=["GET", "POST"])
def guestbook():
    messages = load_messages()
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        text = request.form.get("message", "").strip()

        if not name or not text:
            error = "Both name and message are required."
        else:
            # Generate new ID
            next_id = max([m["id"] for m in messages], default=0) + 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            messages.append({"id": next_id, "name": name, "text": text, "timestamp": timestamp})
            save_messages(messages)
            return redirect(url_for("guestbook"))

    return render_template("guestbook.html", messages=messages, error=error, total=len(messages))

@app.route("/delete/<int:msg_id>")
def delete_message(msg_id):
    messages = load_messages()
    messages = [m for m in messages if m["id"] != msg_id]
    save_messages(messages)
    return redirect(url_for("guestbook"))

if __name__ == "__main__":
    app.run(debug=True)
