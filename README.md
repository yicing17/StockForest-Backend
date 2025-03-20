## 開發指引

### 初次配置

- 安裝 uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. 使用 uv 建立環境
```
# 等待確定本專案所需 python 環境再調整
uv venv test
```

2. 啟動環境
```
source test/bin/activate
```

3. 安裝所有套件
```
uv pip install -r requirements.txt
```

### 日常維護

- 啟動環境
```
source test/bin/activate
```

- 安裝新套件
```
uv pip install <package>
```

- 啟動 FastAPI
```
fastapi dev main.py
```