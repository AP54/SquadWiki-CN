import os

def remove_substring(path, substring):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            new_name = name.replace(substring, '')
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))

if __name__ == '__main__':
    path = input("请输入路径：")
    substring = input("请输入要删除的子字符串：")
    remove_substring(path, substring)
