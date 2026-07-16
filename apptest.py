import gradio as gr

def greet(name):
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("# 最简单的 Gradio 应用")
    name = gr.Textbox(label="输入名字")
    output = gr.Textbox(label="输出")
    gr.Button("问候").click(fn=greet, inputs=name, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)
