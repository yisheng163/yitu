import gradio as gr
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://developer.amd.com.cn/radeon/api/v1/chat/completions"
API_KEY = os.getenv("AMD_API_KEY")
MODEL = "Qwen3.6-35B-A3B"

if not API_KEY:
    raise ValueError("AMD_API_KEY 未配置，请在 .env 文件中设置 AMD_API_KEY，或在系统环境变量中配置。")

def chat(message, history):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = []
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})
    
    data = {
        "model": MODEL,
        "messages": messages
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="简易聊天") as demo:
    gr.Markdown("# 💬 简易聊天")
    gr.Markdown("基于 AMD Radeon API 的对话应用")
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.ChatInterface(
                fn=chat,
                title="",
                description="输入消息开始对话"
            )
        with gr.Column(scale=1):
            gr.Markdown("### 📦 模型信息")
            gr.Markdown(f"**模型**: {MODEL}")
            gr.Markdown("**API**: AMD Radeon")
            gr.Markdown("---")
            gr.Markdown("### 📝 使用说明")
            gr.Markdown("1. 在左侧输入框输入消息")
            gr.Markdown("2. 按 Enter 发送")
            gr.Markdown("3. 支持多轮对话")

demo.launch(server_name="0.0.0.0", server_port=7860)
