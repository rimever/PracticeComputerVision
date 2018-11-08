import os
def get_imlist(path):
    """pathに指定されたディレクトリの全てのjpgファイル名のリストを返す"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]