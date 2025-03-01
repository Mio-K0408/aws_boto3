import boto3
from secret import const

# バージョン情報格納用
version_list = []
file_name = 'sample4.txt'

# バージョンの確認
client = boto3.client('s3')
client.list_object_versions(Bucket=const.BUKKET_NAME)
# 特定のファイル名の情報を取得
# 特定のフォルダ配下の物にしたい場合はPrefix='folder/'とする
for version in client.list_object_versions(Bucket=const.BUKKET_NAME, Prefix=file_name)['Versions']:
    version_list.append(version['VersionId'])
    print(version['Key'],version['VersionId'], version['LastModified'].strftime("%Y/%m/%d %H:%M:%S"))

# 署名付きURLの生成
# Paramsの中で指定することで条件を絞って署名付きURLの発行が可能
# 今回はファイル名とそのファイルのバージョンIDを渡すことで、過去のバージョンのURLを発行している
s3 = boto3.client('s3')
for version in version_list:
    presigned_url = s3.generate_presigned_url(
        ClientMethod = 'get_object',
        Params = {'Bucket' : const.BUKKET_NAME, 'Key' : file_name, 'VersionId':version},
        ExpiresIn = 300,
        HttpMethod = 'GET')
    print(presigned_url)