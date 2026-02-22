import boto3

def get_bedrock_client():
    session = boto3.Session(profile_name="sandbox")
    bedrock = session.client("bedrock-runtime")
    return bedrock

def invoke_bedrock(bedrock, input):
    response = bedrock.converse(
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

def main(input):
    bedrock = get_bedrock_client()
    response_text = invoke_bedrock(bedrock, input)
    print(response_text)
    return

main("Langfuseって何？")
