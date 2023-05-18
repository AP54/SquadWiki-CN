import os
import re

def convert_links_to_lowercase(folder_path):
    # 遍历文件夹及子文件夹下的所有 Markdown 文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换链接和图片指向的 URL 中的大写字母为小写字母
                converted_content = re.sub(r'\[(.*?)\]\((.*?)\)', lambda match: f"[{match.group(1)}]({match.group(2).lower()})", content, flags=re.IGNORECASE)
                converted_content = re.sub(r'!\[(.*?)\]\((.*?)\)', lambda match: f"![{match.group(1)}]({match.group(2).lower()})", converted_content, flags=re.IGNORECASE)

                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(converted_content)

# 示例使用
folder_path = './docs'  # 替换为实际的文件夹路径
convert_links_to_lowercase(folder_path)
