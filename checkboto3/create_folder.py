import boto3
from secret import const

# S3にアクセスし、バケットを取得
client = boto3.client('s3')

# バケットから情報を取得
result = client.list_objects(Bucket=const.BUKKET_NAME, Prefix=const.CREATE_DIR)

# 作成したいフォルダパスが存在しない場合Trueになる
# フォルダパスが既に存在する場合は"Contents"というキーが存在する
if not "Contents" in result:
    client.put_object(Bucket=const.BUKKET_NAME, Key=const.CREATE_DIR)