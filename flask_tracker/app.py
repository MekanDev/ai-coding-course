from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "data.json"

# ===== Helper Functions =====
def load_items():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_items(items):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4)

# ===== Routes =====
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"success": False, "error": "Missing title"}), 400

    items = load_items()
    next_id = max([item["id"] for item in items], default=0) + 1
    item = {
        "id": next_id,
        "title": data["title"],
        "genre": data.get("genre", ""),
        "rating": data.get("rating", ""),
        "notes": data.get("notes", ""),
        "status": "want to watch/read",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    items.append(item)
    save_items(items)
    return jsonify({"success": True, "item": item})

@app.route('/api/items')
def get_items():
    return jsonify({"items": load_items()})

@app.route('/api/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = load_items()
    items = [item for item in items if item["id"] != item_id]
    save_items(items)
    return jsonify({"success": True})

@app.route('/api/toggle/<int:item_id>', methods=['POST'])
def toggle_status(item_id):
    items = load_items()
    for item in items:
        if item["id"] == item_id:
            item["status"] = "completed" if item["status"] == "want to watch/read" else "want to watch/read"
    save_items(items)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
