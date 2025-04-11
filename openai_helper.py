import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_CHATGPT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHATGPT_DEPLOYMENT")
AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

def generate_prompt(user_input, map_nodes):
    system_prompt = "你是一個地圖導引助手。根據使用者輸入的內容，從下列節點資訊中，找出一個最合適的目的地，只回傳那一筆節點的 JSON："

    nodes_info = "\n".join(
        [
            f"{node['nodeID']}: {node['nodeName']} - {node['description']}"
            for node in map_nodes
        ]
    )

    final_prompt = f"""{system_prompt}

地圖節點：
{nodes_info}

使用者輸入：
「{user_input}」

請回傳一筆最適合的節點資料（JSON 格式），例如：
{{"nodeID": 0, "nodeName": "Corridor", "description": ""}}"""

    return final_prompt

def get_destination_node(user_input, map_nodes):
    prompt = generate_prompt(user_input, map_nodes)
    response = client.chat.completions.create(
        model=AZURE_OPENAI_CHATGPT_DEPLOYMENT,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "你是一個地圖導引助手，請根據使用者輸入選出最合適的節點"},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        top_p=1,
        max_tokens=200,
    )

    return json.loads(response.choices[0].message.content)
