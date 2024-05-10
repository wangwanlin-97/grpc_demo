# 运行环境
python 3.10.0

# 编译proto文件
python -m grpc_tools.protoc -I. --python_out=src --grpc_python_out=src proto/**