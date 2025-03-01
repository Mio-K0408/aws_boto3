import boto3
import os
from secret import const

# 設定
local_folder = const.UPLOAD_DIR2        # ローカルで作成するフォルダ名
file_count = 1000                  # 作成するファイル数

# S3クライアント作成
s3 = boto3.client("s3")

# ローカルフォルダ作成（なければ作る）
os.makedirs(local_folder, exist_ok=True)

# 1000件のテキストファイルを作成してS3にアップロード
for i in range(1, file_count + 1):
    file_name = f"test_{i:04d}.txt"  # 例: test_0001.txt, test_0002.txt, ...
    local_path = os.path.join(local_folder, file_name)

    # ファイル作成
    with open(local_path, "w") as f:
        f.write(f"Dummy content for file {i}")

    # S3にアップロード
    s3.upload_file(local_path, const.BUKKET_NAME, file_name)

    # 進捗表示
    if i % 100 == 0:
        print(f"Uploaded {i} files...")

print("1000件のファイルをS3にアップロード完了！")