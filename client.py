import os
from cerebras.cloud.sdk import Cerebras
from openai import OpenAI
import requests
from google import genai
from dotenv import load_dotenv


load_dotenv()


# open router response format:
def ask_ai(prompt):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv("OPEN_ROUTER_API_KEY")}",  # this api key is generated from openrouter.ai
        "Content-Type": "application/json",
    },
    json={   # 🔥 json use karo (data ki jagah)
        "model": "arcee-ai/trinity-large-thinking:free",
        "messages": [
        {
            "role": "user",
            "content": prompt
        }
        ]
    }
    )

    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return "Error:", data



#google gemini response format:

def ask_gemini(prompt):

    client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))      # this api key generated from google cloud console

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text




# hugging face model response format:

def ask_huggingface_llama(prompt):

    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.getenv("HUGGING_FACE_ACCESS_TOKEN"),
    )

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct:novita",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return  completion.choices[0].message.content


# hugging face deepseek response

def huggingface_deepseek(prompt):

    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.getenv("HUGGING_FACE_ACCESS_TOKEN"),
    )

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V4-Pro:novita",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return completion.choices[0].message.content


# this response is generated from groq api:

def ask_groq(prompt):
    groq_api_key = os.getenv("GROQ_API_KEY")   # this api key generated from groq cloud console
    client = OpenAI(
        api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        input=prompt,
        model="openai/gpt-oss-20b",
)
    return response.output_text



# this response is generated from nvidia api:

def ask_nvidia(prompt):

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.getenv("NVIDIA_API_KEY")
    )

    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        top_p=0.95,
        max_tokens=65536,
        extra_body={"chat_template_kwargs": {"enable_thinking": True}, "reasoning_budget": 16384},
        stream=False
    )

    reasoning = getattr(completion.choices[0].message, "reasoning_content", None)
    if reasoning:
        print(reasoning)
    return completion.choices[0].message.content




# this is the response generated from cerebras api:

def ask_cerebras(prompt):
    cerebras_api_key = os.getenv("CEREBRAS_API_KEY")           # this api key is generated from cerebras cloud console

    client = Cerebras(
        api_key=cerebras_api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": prompt,
            }
    ],
        model="qwen-3-235b-a22b-instruct-2507",
    )

    return chat_completion.choices[0].message.content

