import boto3
from langfuse.decorators import observe
from langfuse import Langfuse # 追加

def get_client():
    session = boto3.Session(profile_name="sandbox")
    client = session.client("bedrock-runtime")
    return client

# 追加
def get_prompt(word):
    langfuse = Langfuse()
    prompt = langfuse.get_prompt("test")
    compiled_prompt = prompt.compile(name=word)
    return compiled_prompt

@observe()
def invoke_bedrock(client, input):
    response = client.converse(
        modelId="anthropic.claude-3-5-sonnet-20241022-v2:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": input}]
            }
        ]
    )
    response_text = response["output"]["message"]["content"][0]["text"]
    return response_text

@observe()
def main(word):
    client = get_client()
    input = get_prompt(word) # 追加
    response_text = invoke_bedrock(client, input)
    print(response_text)
    return

main("かぐたん")
