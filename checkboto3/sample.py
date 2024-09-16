import boto3
from secret import const

# S3にアクセスし、バケットを取得
s3_resource = boto3.resource("s3")
print("Hello, Amazon S3! Let's list your buckets:")
for bucket in s3_resource.buckets.all():
    print(f"\t{bucket.name}")

# バケット内のすべてのオブジェクトを取得
bucket = s3_resource.Bucket(const.BUKKET_NAME)
for object in bucket.objects.all():
    print(object)

# ファイルをダウンロードする
s3_resource.Object(const.BUKKET_NAME, 'sample1.txt').download_file(const.DOWNLOAD_DIR)

# ファイルをアップロードする
s3_resource.Object(const.BUKKET_NAME, 'sample4.txt').upload_file(const.UPLOAD_DIR)

# 署名付きURLの生成
s3 = boto3.client('s3')
presigned_url = s3.generate_presigned_url(
    ClientMethod = 'get_object',
    Params = {'Bucket' : const.BUKKET_NAME, 'Key' : 'sample4.txt'},
    ExpiresIn = 300,
    HttpMethod = 'GET')
print(presigned_url)

# バージョンの確認
client = boto3.client('s3')
client.list_object_versions(Bucket=const.BUKKET_NAME)
for version in client.list_object_versions(Bucket=const.BUKKET_NAME)['Versions']:
    print(version['Key'],version['VersionId'], version['LastModified'].strftime("%Y/%m/%d %H:%M:%S"))