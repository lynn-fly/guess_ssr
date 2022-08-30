拉去最新的代码

python3 -m venv .venv
cd .venv
source ./.venv/bin/activate
activate 
deactivate

安装依赖


sudo apt-get install libpq-dev
sudo apt-get install gcc
sudo apt-get install python3.8-dev
sudo apt install python3-wheel
sudo apt install python3.8-venv

pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r .\requirements.txt
python -m pip install PyMySQL --upgrade #如果跑不起来

初始化数据库 更新到最新版
cd backend
alembic upgrade head
cd ..
python3 init_data.py


nohup uvicorn --app-dir backend main:app --reload > log.txt 2>&1 &