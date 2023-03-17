import urllib.request
import os


def download_file_with_proxy(url, file_path, proxy=None):
    """
    使用代理服务器下载文件
    :param url: 下载文件的URL
    :param file_path: 下载文件保存的路径
    :param proxy: 代理服务器地址
    """
    proxy_support = urllib.request.ProxyHandler(
        {'http': proxy, 'https': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    file_size = int(response.getheader('Content-Length'))
    print(
        f'Downloading: {os.path.basename(file_path)} ({file_size/1024:.1f} KB)')

    with open(file_path, 'wb') as f:
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = response.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = f"{file_size_dl/1024:.1f} KB / {file_size/1024:.1f} KB [{file_size_dl/file_size*100:.2f}%]"
            print(status, end='\r')

    print('\nDone.')

proxy="http://127.0.0.1:10809"


def download_file(url, file_path):
    """
    下载文件
    :param url: 下载文件的URL
    :param file_path: 下载文件保存的路径
    """
    urllib.request.urlretrieve(url, file_path)

exeCmd=""

for i in range(2000,2016):
    for j in range(1,13):
        url = "https://zenodo.org/record/5111989/files/Temp_pred_%d_%d_Tmean.zip?download=1" % (i,j)
#        exeCmd += "./fdm.exe " + url + "\n"
        print(url)

#print(exeCmd)
#    download_file_with_proxy(url, file_path, proxy)
#    download_file(url, file_path)

