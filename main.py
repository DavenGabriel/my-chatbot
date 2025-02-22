from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Konfigurasi API Key untuk Google Gemini
api_key = "AIzaSyAwCz9qh2d8geT2y_I3H5Lcy5Z0Yp66-Io"
genai.configure(api_key=api_key)

# Konfigurasi model Gemini
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Instruksi sistem untuk chatbot
system_instruction = (
    "You are an elementary teacher. Your task is to help students do their homework step by step. "
    "Instead of giving the real answer, provide study materials like PDFs or links to websites so they can learn. "
    "Use simple words appropriate for their age, make it fun with humor, and ask guiding questions to improve their learning experience."
)

# Membuat model generatif dengan instruksi sistem
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=system_instruction,
)

# Membuka sesi percakapan dengan chatbot
chat_session = model.start_chat(history=[])

# Membuat aplikasi Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gemini-api", methods=["POST"])
def gemini_api():
    user_input = request.form['data']  # Ambil input dari user
    
    # Kirim input ke chatbot
    response = chat_session.send_message(user_input)

    if response and response.text:
        return jsonify({"msg": "Success", "bot_reply": response.text})
    else:
        return jsonify({"msg": "Failed", "bot_reply": "I couldn't generate a response."})

# Jalankan aplikasi Flask
if __name__ == "__main__":
    app.run()
