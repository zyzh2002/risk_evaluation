import urllib.request


def download_file_with_proxy(url, file_path, proxy):
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
    urllib.request.urlretrieve(url, file_path)


proxy="http://127.0.0.1:10809"


def download_file(url, file_path):
    """
    下载文件
    :param url: 下载文件的URL
    :param file_path: 下载文件保存的路径
    """
    urllib.request.urlretrieve(url, file_path)

for i in range(2000,2016):
    url = "https://zenodo.org/record/4417810/files/CLCD_v01_"+str(i)+".tif?download=1"
    file_path = "./down/CLCD_v01_"+str(i)+".tif"
#    download_file_with_proxy(url, file_path, proxy)
    download_file(url, file_path)