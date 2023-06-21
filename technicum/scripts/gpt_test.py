import openai
import os


def get_gpt_answer(question: str) -> str:
    'Принимает вопрос - возвращает ответ от ChatGpt'
    os.environ['http_proxy'] = 'https://172.67.177.230:80'
    openai.api_key = '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'
    messages3 = [{"role": "user",
                "content": f"Подбери код ТНВЭД, код ОКПД2 для продукции: {question}. Сертификации по каким техническим регламентам таможенного союза подлежит {question}?"
                }
    ]
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                            temperature=0.5,
                                            max_tokens=1000,
                                            messages=messages3,
                                            )
    return response["choices"][0]["message"]["content"]
