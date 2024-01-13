# 华北平原水旱风险评估
这是该科创项目的资源以及论文仓库。以下是该仓库的目录结构说明。

## 目录结构
* `./scripts`<br>
程序脚本


* `./tex`<br>
$\LaTeX$论文目录


* `./tutorials`<br>
基础的[操作教程](## "教程索引")


* `./docs`<br>

参考文献与相关文档目录

***
## 教程索引

* [命令行教程](tutorials/cmd.md) <br>
* [GitHub使用教程](tutorials/github.md) <br>
* [OpenSSH](tutorials/openssh.md)<br>

***
## 环境要求
* `python>=3.10`
* `pip`
* WSL2来提供`directML`支持

使用`scripts` 中的`Makefile`来构建计算环境。

***
## 数据来源
项目的主要数据均上传至腾讯云cos存储桶。预期数据时间跨度为2000-2015年。


### 数据列表
* [x] DEM（90m）来自[地理空间数据云][1]
* [x] 降雨量 来自[国家青藏高原科学数据中心][3]
* [x] PET 来自[NASA MODIS16A2][9]

* [x] 土地利用 来自[30 m annual land cover and its dynamics in China from 1990 to 2019][8]

* [x] 省级行政区边界 来自来自[中国科学院资源环境科学与数据中心][2]
* [x] 人口密度 来自[worldpop.org][4]
* [x] GDP密度 来自[全球变化科学研究数据出版系统][7]
* [x] 河流分布 来自[全国地理信息资源目录服务系统][6]


[1]:<https://www.gscloud.cn/sources/accessdata/305?pid=302>
[2]:<https://www.resdc.cn/DOI/DOI.aspx?DOIID=122>
[3]:<https://data.tpdc.ac.cn/zh-hans/data/faae7605-a0f2-4d18-b28f-5cee413766a2>
[4]:<https://hub.worldpop.org/geodata/listing?id=76>
[5]:<https://data.tpdc.ac.cn/zh-hans/data/c3a67628-bb4d-4fb3-9bb2-0a2b88bdb6fe>
[6]:<https://www.webmap.cn/commres.do?method=result100W>
[7]:<https://www.geodoi.ac.cn/WebCn/doi.aspx?Id=125>
[8]:<https://zenodo.org/record/4417810#.ZAXdchVBxD8>
[9]:<https://lpdaac.usgs.gov/products/mod16a2v006/>
