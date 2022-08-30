拉去最新的代码

python3 -m venv .venv
cd .venv
source ./.venv/bin/activate
activate 
deactivate

安装依赖
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r .\requirements.txt
python -m pip install PyMySQL --upgrade #如果跑不起来

初始化数据库 更新到最新版
cd backend
alembic upgrade head
cd ..
python3 init_data.py