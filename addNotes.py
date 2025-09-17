# TODO:将一个目录下的子目录中的文件拷贝到当前目录对应的子目录中

import os
import shutil

def copy_notes_from_subdirs(source_dir, target_dir=".", notes_dir_name="笔记"):
    """
    将源目录下的子目录中名为'笔记'的文件夹下的所有内容拷贝到当前目录对应的子目录中
    
    Args:
        source_dir (str): 源目录路径
        target_dir (str): 目标目录路径，默认为当前目录
        notes_dir_name (str): 笔记文件夹名称，默认为"笔记"
    """
    # 确保源目录存在
    if not os.path.exists(source_dir):
        print(f"源目录 {source_dir} 不存在")
        return
    
    if not os.path.isdir(source_dir):
        print(f"源路径 {source_dir} 不是一个目录")
        return
    
    # 遍历源目录下的所有子目录
    for item in os.listdir(source_dir):
        source_subdir = os.path.join(source_dir, item)
        
        # 只处理目录
        if os.path.isdir(source_subdir):
            # 构造源笔记目录路径
            source_notes_dir = os.path.join(source_subdir, notes_dir_name)
            
            # 检查笔记目录是否存在
            if os.path.exists(source_notes_dir) and os.path.isdir(source_notes_dir):
                # 在目标目录中创建对应的子目录
                target_subdir = os.path.join(target_dir, item)
                
                # 如果目标子目录不存在，则创建
                if not os.path.exists(target_subdir):
                    os.makedirs(target_subdir)
                    print(f"创建目录: {target_subdir}")
                
                # 拷贝笔记目录下的所有内容（包括文件和文件夹）
                for file_item in os.listdir(source_notes_dir):
                    source_path = os.path.join(source_notes_dir, file_item)
                    target_path = os.path.join(target_subdir, file_item)
                    
                    # 拷贝文件或文件夹
                    if os.path.isfile(source_path):
                        shutil.copy2(source_path, target_path)
                        print(f"拷贝文件: {source_path} -> {target_path}")
                    elif os.path.isdir(source_path):
                        shutil.copytree(source_path, target_path)
                        print(f"拷贝文件夹: {source_path} -> {target_path}")
            else:
                print(f"在 {source_subdir} 中未找到 {notes_dir_name} 目录")

# 示例用法
if __name__ == "__main__":
    # 将指定目录下的子目录中笔记文件夹下的内容拷贝到当前目录对应的子目录中
    copy_notes_from_subdirs("D:\ADevPlan\Java入门到起飞学习资料\资料")