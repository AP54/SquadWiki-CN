import os

def lowercase_filenames(path):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            if any(c.isupper() for c in name):
                newname = name.lower()
                os.rename(os.path.join(root, name), os.path.join(root, newname))

if __name__ == '__main__':
    path = input("请输入文件夹路径：")
    lowercase_filenames(path)