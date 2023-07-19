import boto3
client = boto3.client(
    's3',
    aws_access_key_id='AKIAXC4GMJFXHUM27OUE',
    aws_secret_access_key='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',
)

a = client.list_objects(
    Bucket = 'bucket-amar-001'
)
l = []
for i in a['Contents']:
    l.append(i['Key'])

b = len(l)
if b == 0:
    print('no data inside')
else:
    print(l)

