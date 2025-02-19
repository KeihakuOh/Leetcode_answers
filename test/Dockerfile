# ベースイメージの指定（例: Python 3.9）
FROM python:3.9-slim

# コンテナ内の作業ディレクトリを指定
WORKDIR /app

# ホスト側から requirements.txt をコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# 実行コマンドを pytest に設定
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v"]


# docker build -t pytest-container .
# docker run --rm pytest-container
