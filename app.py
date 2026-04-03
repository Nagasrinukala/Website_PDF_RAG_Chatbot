import gradio as gr
from website_chatbot.scraper import scrape_website
from website_chatbot.chatbot import ask_chatbot, reset_vector_store
from website_chatbot.pdf_reader import read_pdf

website_data = ""
chat_history = []

def scrape(urls, pdf_file):
    global website_data
    website_data = ""
    reset_vector_store()

    print("URLs received:", urls)

    # Handle URLs
    if urls:
        url_list = urls.split(",")
        for url in url_list:
            url = url.strip()
            if url:
                print("Processing URL:", url)
                data = scrape_website(url)
                website_data += f"\nContent from {url}:\n"
                website_data += data + "\n\n"

    # Handle PDF
    if pdf_file is not None:
        print("Reading PDF...")
        pdf_text = read_pdf(pdf_file)
        website_data += "\nContent from PDF:\n"
        website_data += pdf_text + "\n\n"

    print("Total data length:", len(website_data))

    if website_data.strip() == "":
        return "Please enter URLs or upload PDF."

    return f"Data loaded successfully! Length: {len(website_data)}"

    
def chat(message, history):
    global website_data
    global chat_history

    if website_data == "":
        return "Please load website or PDF first."

    history_text = "\n".join(chat_history)
    answer = ask_chatbot(website_data, message, history_text)

    chat_history.append(f"User: {message}")
    chat_history.append(f"Bot: {answer}")

    return answer


css = """
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

body {
    background-image: url("/file=assets/background.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Syne', sans-serif !important;
}

/* ── Main container ── */
.gradio-container {
    background: linear-gradient(160deg, #09060f 0%, #0d0818 40%, #0a0612 100%) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    color: #ede9fe !important;
    border-radius: 22px !important;
    border: 1px solid rgba(167,139,250,0.2) !important;
    padding: 0 !important;
    box-shadow: 0 0 100px rgba(139,92,246,0.07), 0 0 0 1px rgba(255,255,255,0.03) !important;
    overflow: hidden !important;
    position: relative !important;
}

/* ── Ambient aurora glow orbs ── */
.gradio-container::before {
    content: '';
    position: absolute;
    top: -150px; left: 30%;
    width: 400px; height: 300px; border-radius: 50%;
    background: radial-gradient(ellipse, rgba(139,92,246,0.09) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
}

.gradio-container::after {
    content: '';
    position: absolute;
    top: -100px; right: 10%;
    width: 250px; height: 250px; border-radius: 50%;
    background: radial-gradient(ellipse, rgba(236,72,153,0.06) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
}

/* ── Title / Header ── */
.prose h1, .md h1, h1 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    font-size: 26px !important;
    background: linear-gradient(90deg, #c084fc, #f472b6) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    text-align: center !important;
    padding: 18px 0 14px !important;
    border-bottom: 1px solid rgba(139,92,246,0.15) !important;
    letter-spacing: 0.3px !important;
}

/* ── Blocks / panels ── */
.block, .gr-block, .gap, .contain, .form {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

.gradio-container > .wrap,
.gradio-container > .wrap > .gap > .block {
    background: rgba(7,5,15,0.6) !important;
    border: 1px solid rgba(139,92,246,0.15) !important;
    border-radius: 16px !important;
    padding: 16px !important;
}

/* ── Inputs & Textareas ── */
input[type="text"], input[type="email"],
textarea, .scroll-hide {
    background: rgba(7,5,15,0.85) !important;
    border: 1px solid rgba(139,92,246,0.22) !important;
    border-radius: 11px !important;
    color: #ddd6fe !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 14px !important;
    caret-color: #a855f7 !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    box-shadow: none !important;
}

input[type="text"]:focus, textarea:focus {
    border-color: rgba(168,85,247,0.55) !important;
    box-shadow: 0 0 0 3px rgba(168,85,247,0.1) !important;
    outline: none !important;
}

input::placeholder, textarea::placeholder {
    color: #3b0764 !important;
}

/* ── File upload zone ── */
.upload-container, [data-testid="block-upload-area"],
.svelte-uploadzone, .drop-col {
    background: rgba(7,5,15,0.6) !important;
    border: 1.5px dashed rgba(139,92,246,0.25) !important;
    border-radius: 13px !important;
    transition: border-color 0.2s, background 0.2s !important;
}

.upload-container:hover, [data-testid="block-upload-area"]:hover {
    border-color: rgba(168,85,247,0.5) !important;
    background: rgba(139,92,246,0.05) !important;
}

.upload-container p, .drop-col p, .file-name {
    color: #6d28d9 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
}

/* ── Primary button (Load Data) ── */
button.primary, .gr-button-primary,
button[variant="primary"], .green-btn {
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #db2777 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 13px !important;
    height: 46px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 24px rgba(124,58,237,0.4) !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
}

button.primary:hover, .green-btn:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(124,58,237,0.55) !important;
}

/* ── Secondary buttons ── */
button.secondary, .gr-button-secondary,
button[variant="secondary"] {
    background: rgba(139,92,246,0.08) !important;
    color: #c084fc !important;
    border: 1px solid rgba(139,92,246,0.25) !important;
    border-radius: 12px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    transition: background 0.15s !important;
}

button.secondary:hover {
    background: rgba(139,92,246,0.16) !important;
}

/* ── Status textbox ── */
.status-box, [data-testid="textbox"] .scroll-hide {
    background: rgba(7,5,15,0.85) !important;
    border-left: 3px solid #a855f7 !important;
    border-top: 1px solid rgba(139,92,246,0.15) !important;
    border-right: 1px solid rgba(139,92,246,0.15) !important;
    border-bottom: 1px solid rgba(139,92,246,0.15) !important;
    border-radius: 0 10px 10px 0 !important;
    color: #a855f7 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
}

/* ── Chatbot window ── */
.chatbot, [data-testid="chatbot"] {
    background: rgba(7,5,15,0.65) !important;
    border: 1px solid rgba(139,92,246,0.13) !important;
    border-radius: 16px !important;
}

/* ── Chat bubbles ── */
[data-testid="bot"] {
    background: rgba(139,92,246,0.09) !important;
    border: 1px solid rgba(139,92,246,0.2) !important;
    border-radius: 4px 14px 14px 14px !important;
    color: #ddd6fe !important;
    font-family: 'Syne', sans-serif !important;
}

[data-testid="user"] {
    background: linear-gradient(135deg, rgba(124,58,237,0.22), rgba(219,39,119,0.18)) !important;
    border: 1px solid rgba(167,139,250,0.25) !important;
    border-radius: 14px 4px 14px 14px !important;
    color: #f5d0fe !important;
    font-family: 'Syne', sans-serif !important;
}

/* ── Chat send button ── */
button[aria-label="Submit"], .submit-btn {
    background: linear-gradient(135deg, #7c3aed, #db2777) !important;
    border-radius: 11px !important;
    border: none !important;
    color: #fff !important;
    box-shadow: 0 4px 16px rgba(124,58,237,0.4) !important;
    transition: transform 0.15s !important;
}

button[aria-label="Submit"]:hover {
    transform: scale(1.08) !important;
}

/* ── Labels ── */
label span, .gr-label, span.svelte-1b6s6s {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 9px !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    background: linear-gradient(90deg, #a855f7, #ec4899) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: rgba(7,5,15,0.5); border-radius: 8px; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #7c3aed, #db2777); border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: #a855f7; }

/* ── Footer ── */
.footer, .footer-wrap {
    text-align: center !important;
    color: #3b0764 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 9px !important;
    letter-spacing: 1.5px !important;
    border-top: 1px solid rgba(139,92,246,0.1) !important;
    padding: 10px !important;
}

.footer a { color: #6d28d9 !important; }
"""

with gr.Blocks(css=css) as demo:

    gr.Markdown("# 🌐 Website + PDF RAG Chatbot")

    with gr.Row():
        with gr.Column(scale=1):
            url = gr.Textbox(label="Website URLs (comma separated)")
            pdf_file = gr.File(label="Upload PDF")
            scrape_btn = gr.Button("Load Data")
            scrape_output = gr.Textbox(label="Status")

        with gr.Column(scale=2):
            chatbot_ui = gr.ChatInterface(chat)

    scrape_btn.click(scrape, inputs=[url, pdf_file], outputs=scrape_output)

demo.launch()