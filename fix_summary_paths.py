#!/usr/bin/env python3
"""
批量修改 SUMMARY.md 文件中的路径为根路径格式
将 ./README.md 改为 /目录名/README.md
将 ./docs/xxx.md 改为 /目录名/docs/xxx.md
"""

import os
import re

def fix_summary_file(filepath):
    """修改单个 SUMMARY.md 文件的路径"""
    # 获取目录名
    dir_path = os.path.dirname(filepath)
    dir_name = os.path.basename(dir_path)
    
    # 跳过根目录的 SUMMARY.md
    if not dir_name or dir_name.endswith('gitbook'):
        print(f"跳过根目录: {filepath}")
        return False
    
    # 读取文件内容
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取失败: {filepath}, 错误: {e}")
        return False
    
    # 替换路径
    # 将 ./README.md 替换为 /目录名/README.md
    # 将 ./docs/xxx.md 替换为 /目录名/docs/xxx.md
    new_content = re.sub(r'\]\(\./', f'](/{dir_name}/', content)
    
    if new_content == content:
        print(f"无需修改: {filepath}")
        return False
    
    # 写回文件
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"已修改: {filepath}")
        return True
    except Exception as e:
        print(f"写入失败: {filepath}, 错误: {e}")
        return False

def main():
    """主函数"""
    base_dir = '/Users/liuyutong/learning_secrets/gitbook'
    
    # 查找所有 SUMMARY.md 文件
    count = 0
    for root, dirs, files in os.walk(base_dir):
        # 跳过 .git 目录
        if '.git' in root:
            continue
        
        if 'SUMMARY.md' in files:
            filepath = os.path.join(root, 'SUMMARY.md')
            if fix_summary_file(filepath):
                count += 1
    
    print(f"\n总计修改了 {count} 个文件")

if __name__ == '__main__':
    main()