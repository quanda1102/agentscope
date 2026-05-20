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

## 2. Nếu cần Pull code mới từ Repo gốc
```bash
# Chạy lần đầu ở local machine
git remote add upstream https://github.com/agentscope-ai/agentscope.git

git fetch upstream
git checkout <your_branch>

# Kéo code thẳng từ remote về branch
git merge upstream/main
```



