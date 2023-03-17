import re

text = "['https://riskevaluate.zyzh20021020.cn/DEM-90/DEM-90.zip', 'https://riskevaluate.zyzh20021020.cn/PRECIP/cn_precip.csv', 'https://riskevaluate.zyzh20021020.cn/TEMP/TEMP.zip', 'https://riskevaluate.zyzh20021020.cn/POPULAR/chn_pd_2000_1km_ASCII_XYZ.zip', 'https://riskevaluate.zyzh20021020.cn/WIND/GGWS-PCNN-wind_speed-197301202112_v330202202p.nc', 'https://riskevaluate.zyzh20021020.cn/RIVER/river.zip', 'https://riskevaluate.zyzh20021020.cn/BOARDER/border_2022.rar', 'https://riskevaluate.zyzh20021020.cn/GDP/GDP.zip', 'https://riskevaluate.zyzh20021020.cn/CLCD/CLCD.zip']"
pattern = r"(?<=zyzh20021020\.cn/)[^/]+"
match = re.search(pattern, text)

if match:
    url = match.group(0)
    print(url)
