## Lưu ý dành cho Dev

## 1. Luôn cài từ source:

```bash
git clone -b main https://github.com/quanda1102/agentscope.git
cd agentscope
```

Nếu dùng uv, đừng dùng uv sync hay uv run vì dependency conflict sẽ xảy ra

```bash
uv venv
source .venv/bin/activate
pip install -e .
python example.py 
```





