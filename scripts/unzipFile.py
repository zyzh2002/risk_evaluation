import zipfile
import os
import pathlib
from tqdm import tqdm


def unzipFile(file_path, extract_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        file_size = sum((file.file_size for file in zip_ref.infolist()))
        extracted_size = 0
        for file in tqdm(iterable=zip_ref.infolist(), total=len(zip_ref.infolist()), unit='B', unit_scale=True):
            zip_ref.extract(file, path=extract_path)
            extracted_size += file.file_size
            progress = extracted_size / file_size * 100
            tqdm.write(
                f'Extracting: {file.filename}, Progress: {progress:.2f}%')

dataPath = pathlib.Path("./scripts/datas/")

for filePath in dataPath.glob("*/*.zip"):
    extractPath = os.path.dirname(filePath) + "/extracted/"

    if not os.path.exists(extractPath):
        os.makedirs(extractPath)

    unzipFile(filePath, extractPath)

# unzip