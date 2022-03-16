import boto3

def lambda_handler(event, context):
    # Trigger S3-bucket
    s3 = boto3.client("s3")
    if event:
        print(event)
        file_obj = event['Records'][0]
        filename = str(file_obj["s3"]["object"]["key"])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket = "source-bucket00", Key = filename)
        print("File Obj: ", fileObj)
        file_content = fileObj["Body"].read().decode('utf-8')
        print(file_content)
        print()
    return "Thanks"