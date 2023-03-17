import re
import requests
import os


def downloadFile(url, download_dir):
    def print_progress(current, total):
        progress = current / total * 100
        print(f"\rDownloading... {progress:.2f}%", end='', flush=True)
    # 获取文件名
    file_name = os.path.basename(url)

    # 组合文件保存路径
    file_path = os.path.join(download_dir, file_name)

    # 发起请求获取文件大小
    response = requests.head(url)
    size = int(response.headers.get('Content-Length', 0))

    # 判断文件是否已经存在，如果存在则询问是否覆盖
    if os.path.isfile(file_path):
        overwrite = input(
            f"The file '{file_path}' already exists, do you want to overwrite it? [y/n] ")
        if overwrite.lower() != 'y':
            return

    # 下载文件并保存
    response = requests.get(url, stream=True)
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
            print_progress(f.tell(), size)
    print(" Download completed.")




urlAndPath=[]
pattern = r"\[?[a-zA-Z]\]?:<(.*?)>"


with open("README.md", "r",encoding="utf-8") as f:

    for line in f:
        mdFile = line
        i = re.search(pattern, mdFile)

        if i:
            urlStr = str(i.group(1))

            pathPattern = r"(?<=zyzh20021020\.cn/)[^/]+"
            pathName = re.search(pathPattern, urlStr).group(0)

            urlAndPath.append([urlStr, pathName])



for i in urlAndPath:
    downloadPath = "./scripts/datas/"+i[1]
    if not os.path.exists(downloadPath):
        os.mkdir("./scripts/datas/"+i[1])

    downloadFile(i[0],downloadPath)
    print("Downloaded "+i[1])
