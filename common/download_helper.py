import os
import time
import glob

# 设置统一下载目录（你已有 download 文件夹）
DOWNLOAD_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../download"))

def clear_download_dir():
    """清空 download 文件夹"""
    files = glob.glob(os.path.join(DOWNLOAD_PATH, "*"))
    for f in files:
        os.remove(f)

def wait_for_download_file(extension: str, timeout: int = 10):
    """
    等待指定类型文件出现在 download 目录
    :param extension: 文件后缀名（不带点）例如 'pdf', 'docx'
    :param timeout: 超时时间（秒）
    :return: 成功下载的文件路径
    """
    for _ in range(timeout):
        files = glob.glob(os.path.join(DOWNLOAD_PATH, f"*.{extension}"))
        if files:
            return files[0]
        time.sleep(1)
    raise FileNotFoundError(f"{extension.upper()} 文件未在 {timeout} 秒内下载完成")
