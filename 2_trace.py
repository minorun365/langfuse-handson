import boto3
from langfuse.decorators import observe # 追加

def get_client():
    session = boto3.Session(profile_name="sandbox")
    client = session.client("bedrock-runtime")
    return client

@observe() # 追加
def invoke_bedrock(client, input):
    response = client.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": input}]
            }
        ]
    )
    response_text = response["output"]["message"]["content"][0]["text"]
    return response_text

@observe() # 追加
def main(input):
    client = get_client()
    response_text = invoke_bedrock(client, input)
    print(response_text)
    return

main("Langfuseって何？")
