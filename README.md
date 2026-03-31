# Azure Web App Python Demo

这是一个可直接上传到 GitHub 并部署到 Azure Web App 的最小 Flask 示例。

## 文件说明
- `app.py`：应用入口
- `requirements.txt`：Python 依赖
- `startup.txt`：建议在 Azure Web App 的启动命令中填写的内容

## 本地运行
```bash
python -m venv .venv
source .venv/bin/activate   # Windows 用 .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Azure Web App 配置建议
运行时：Python  
启动命令：
```bash
gunicorn --bind=0.0.0.0:$PORT app:app
```

## 可用于验证日志的路径
- `/`：首页
- `/health`：正常 200
- `/echo?name=test`：正常 200 并记录日志
- `/error`：主动返回 500，便于验证告警和日志采集
- `/notfound`：访问不存在路径，可制造 404

## 部署到 GitHub 后
把这几个文件放到仓库根目录即可，然后在 Azure Web App 的部署中心选择 GitHub 仓库和分支。
