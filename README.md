# IntroAI_Project
人工智能导论课程项目作业

## LLM模型api

### 1.获取api
前往[讯飞星火](https://xinghuo.xfyun.cn/sparkapi)创建应用获取https服务接口的apipassword与接口地址

### 2.设置环境变量
```bash
set LLM_PROMPT_API_URL your_url
set LLM_PROMPT_API_PASSWORD your_password
```

## 后端

### 1.创建虚拟环境
```bash
cd backend
python -m venv venv
```
### 2.激活虚拟环境
```bash
venv\Scripts\activate
```

### 3.安装依赖
```bash
pip install -r requirements.txt
```

### 4.运行服务器
```bash
python app.py
```

## 前端

### 1.下载nvm
前往[nvm-windows](https://github.com/coreybutler/nvm-windows/releases)下载

### 2.安装Node.js
```bash
nvm install 20
nvm use 20
```

### 3.安装依赖
```bash
cd frontend
npm install
```

### 4.运行服务器
```bash
npm run dev
```

