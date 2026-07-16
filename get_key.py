import os

def get_api_key():
    """从配置文件或环境变量中获取API密钥"""
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 尝试从.env文件中读取
    config_file_path = os.path.join(script_dir, '.env')
    
    try:
        if os.path.exists(config_file_path):
            with open(config_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            if key.strip() == 'MODELSCOPE_API_KEY':
                                api_key = value.strip()
                                if api_key:
                                    return api_key
            print(f"警告: 配置文件 {config_file_path} 中未找到MODELSCOPE_API_KEY，将尝试从环境变量读取")
        else:
            print(f"警告: 配置文件 {config_file_path} 不存在，将尝试从环境变量读取")
    except Exception as e:
        print(f"错误: 读取配置文件 {config_file_path} 时发生未知错误: {e}")
    
    # 如果配置文件中没有找到，则从环境变量中读取
    api_key = os.getenv("myKEY")
    if api_key and api_key.strip():
        return api_key.strip()
    
    # 如果都找不到，返回None
    return None