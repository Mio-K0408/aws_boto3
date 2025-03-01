import boto3
from secret import const

# S3にアクセスし、バケットを取得
s3_resource = boto3.resource("s3")
bucket = s3_resource.Bucket(const.BUKKET_NAME)

# objects.allを使えば1000件以上も問題なく一括取得可能
for object in bucket.objects.all():
    print(object.key)
    
# 署名付きURLの発行
file_count = 1000 
# S3クライアント作成
s3 = boto3.client("s3")
for i in range(1, file_count + 1):
    file_name = f"test_{i:04d}.txt"
    presigned_url = s3.generate_presigned_url(
    ClientMethod = 'get_object',
    Params = {'Bucket' : const.BUKKET_NAME, 'Key' : file_name},
    ExpiresIn = 300,
    HttpMethod = 'GET')
    print(presigned_url)


# 署名付きURLを1000件発行しても処理速度は2秒程度
