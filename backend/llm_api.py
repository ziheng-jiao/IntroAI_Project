import gradio as gr
import requests

def poem_to_landscape(poem: str, height: int = 768, width: int = 768, steps: int = 30, guidance: float = 7.5):

    llm_url = "https://spark-api-open.xf-yun.com/v1/chat/completions"

    data = {
        "model": "generalv3.5",
        "messages": [
            {"role": "system",
             "content": "你是一位精通意境描绘的AI画师，请将诗词意境转化为生成中国山水画的提示词（prompt），用英文输出，简洁明了，包含光线、情感与景物要素。"},
            {"role": "user", "content": poem}
        ]
    }

    header = {
        "Authorization": "Bearer nVnLshVeFlvBjtpFfrtj:XzBDHGhFUlYftApWncRy"
    }

    response = requests.post(llm_url, headers=header, json=data)
    response_json = response.json()

    return None, response_json['choices'][0]['message']['content']


title = "本地诗意山水画生成器"
description = """输入一首古诗词，系统将理解诗意并生成对应的中国山水画。"""
examples = [
    ["白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"],
    ["孤舟蓑笠翁，独钓寒江雪。"],
    ["明月松间照，清泉石上流。"]
]

demo = gr.Interface(
    fn=poem_to_landscape,
    inputs=[
        gr.Textbox(lines=3, label="请输入诗词"),
        gr.Slider(minimum=256, maximum=1024, step=128, label="图片高 (px)", value=768),
        gr.Slider(minimum=256, maximum=1024, step=128, label="图片宽 (px)", value=768),
        gr.Slider(minimum=5, maximum=100, step=5, label="采样步数", value=30),
        gr.Slider(minimum=1.0, maximum=15.0, step=0.5, label="guidance scale", value=7.5)
    ],
    outputs=[
        gr.Image(label="生成的山水画"),
        gr.Textbox(label="生成的提示词")
    ],
    title=title,
    description=description,
    examples=examples,
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share = True)