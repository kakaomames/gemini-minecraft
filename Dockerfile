# より安定したAmazonのOpenJDKイメージを使用
FROM amazoncorretto:21-al2023-headless

# Python3のインストール（Amazon Linuxベースなのでyum/dnfを使用）
RUN dnf update -y && dnf install -y python3 python3-pip

WORKDIR /app

# 全ファイルをコピー
COPY . .

# 依存関係のインストール（requirements.txtがある場合）
RUN pip3 install -r requirements.txt || echo "requirements.txt not found, skipping"

# Renderのポート開放
EXPOSE 8080

# 起動コマンド
CMD ["python3", "main.py"]
