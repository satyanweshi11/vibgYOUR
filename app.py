from flask import Flask, render_template, request, jsonify
import hashlib
import json
import os

app = Flask(__name__)

THEME_FILE = "user_themes.json"  # Store user themes persistently

def text_to_color(text):
    """Generate a color hex code from a given text (hashing)."""
    hash_object = hashlib.sha256(text.encode())
    hex_code = hash_object.hexdigest()[:6]
    return f"#{hex_code}"

def load_theme(username):
    """Loads the user's saved theme colors from JSON file."""
    try:
        if os.path.exists(THEME_FILE) and os.path.getsize(THEME_FILE) > 0:
            with open(THEME_FILE, "r") as file:
                themes = json.load(file)

                if isinstance(themes, str):  # Ensure correct parsing
                    themes = json.loads(themes)

                return themes.get(username, {
                    "font_color": "#FFFFFF",
                    "body_color": "#141E30",
                    "border_color": "#FFFFFF"
                })
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return {"font_color": "#FFFFFF", "body_color": "#141E30", "border_color": "#FFFFFF"}

def save_theme(username, font_color, body_color, border_color):
    """Save the user's theme selection to a JSON file."""
    themes = {}
    if os.path.exists(THEME_FILE) and os.path.getsize(THEME_FILE) > 0:
        try:
            with open(THEME_FILE, "r") as file:
                themes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    themes[username] = {
        "font_color": font_color,
        "body_color": body_color,
        "border_color": border_color
    }

    with open(THEME_FILE, "w") as file:
        json.dump(themes, file, indent=4)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Generate unique color from username + password
        user_color = text_to_color(username + password)

        # Load user theme from saved settings
        user_theme = load_theme(username)

        return render_template('dashboard.html', 
                               username=username, 
                               color=user_color,
                               font_color=user_theme["font_color"],
                               body_color=user_theme["body_color"],
                               border_color=user_theme["border_color"])

    return render_template('index.html')

@app.route('/update-theme', methods=['POST'])
def update_theme():
    """API to update the user's custom theme settings."""
    data = request.json
    username = data.get("username")
    font_color = data.get("fontColor")
    body_color = data.get("bodyColor")
    border_color = data.get("borderColor")

    if not username:
        return jsonify({"status": "error", "message": "Username missing"}), 400

    save_theme(username, font_color, body_color, border_color)
    return jsonify({"status": "success", "message": "Theme updated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
