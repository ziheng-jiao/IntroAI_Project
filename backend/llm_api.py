import requests

def poem_to_landscape(poem: str, height: int = 768, width: int = 768, steps: int = 30, guidance: float = 7.5):

    llm_url = "https://spark-api-open.xf-yun.com/v1/chat/completions"

    data = {
        "model": "generalv3.5",
        "messages": [
            {"role": "system",
             "content": """You are a helpful assistant that converts poetic descriptions into detailed landscape painting prompts suitable for AI image generation.
            Provide prompts based on the structure of [trigger words], [overall composition and perspective], [core subject], [artistic techniques and details], and [atmosphere and environment]. 
            The trigger word is set as CN_ShanShui.Here are some examples:
            1.CN_ShanShui, a close-up detail view of a gentle mountain ridge flowing horizontally. The central subject is a rounded hill top painted with varying shades of light ink. The brushwork features long, dry "hemp-fiber" strokes (Pima cun) layered over wet washes to define the slope's texture. The visible grain of the beige antique paper adds to the historic aesthetic, evoking a mood of tranquility and natural simplicity.
            2.CN_ShanShui, a close-up detail of a layered landscape composition. A soft, triangular mountain peak sits in the background above a horizontal band of riverbank or marsh. The technique emphasizes "wet wash" (shuimo) with broad, diluted ink strokes and minimal outlines, creating a blurred, hazy effect. The texture of the fibrous antique paper permeates the image, contributing to a misty, ethereal atmosphere."""},
            {"role": "user", "content": poem}
        ]
    }

    header = {
        "Authorization": "Bearer nVnLshVeFlvBjtpFfrtj:XzBDHGhFUlYftApWncRy"
    }

    response = requests.post(llm_url, headers=header, json=data)
    response_json = response.json()

    return response_json['choices'][0]['message']['content']