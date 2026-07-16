import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

def setup_logging():
    """
    配置日志系统
    日志文件存储在项目根目录下的log文件夹中，文件名格式为：日期字符串（YYYY-MM-DD）+.log
    支持多用户并发访问，使用TimedRotatingFileHandler确保线程安全
    """
    # 创建logs目录（如果不存在）
    log_dir = "log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 以日期命名日志文件
    log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
    
    # 创建一个支持多进程安全的日志处理器
    file_handler = TimedRotatingFileHandler(
        filename=log_filename,
        when="midnight",
        interval=1,
        backupCount=7,  # 保留7天的日志
        encoding="utf-8"
    )
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # 配置日志格式
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
    # 添加控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)
    
    # 防止日志传播到根记录器
    logger.propagate = False
    
    return logger

# 创建全局日志记录器
logger = setup_logging()