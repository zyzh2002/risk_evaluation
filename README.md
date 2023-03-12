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
重要的参考文献目录

***
## 教程索引

* [命令行教程](tutorials/cmd.md) <br>
* [GitHub使用教程](tutorials/github.md) <br>
* [OpenSSH](tutorials/openssh.md)<br>

***
## 环境要求
* `python>=3.9`
* `pip`
* 如果使用`Windows`环境，建议安装`make`等工具。

使用`scripts` 中的`Makefile`来构建计算环境。

如果要在`Windows`下配置`make`，推荐使用`winget`工具：
* 执行`winget install GnuWin32.Make`
* 之后将`C:\Program Files (x86)\GnuWin32\bin`添加至`Path`

***
## 数据来源
项目的主要数据均上传至腾讯云cos存储桶。预期数据时间跨度为2000-2015年。

>项目的数据仍处于收集中，***资源不全***。

### 数据列表
* [x] [DEM（90m）][a] 来自[地理空间数据云][1]
* [x] [降雨量][b] 来自[中国科学院资源环境科学与数据中心][3]
* [x] [温度][c] 来自[zenodo.org][8]

    [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5111989.svg)](https://doi.org/10.5281/zenodo.5111989)

* [x] [风速][e] 来自[国家青藏高原科学数据中心][5]
* [x] [土地利用][I] 来自[30 m annual land cover and its dynamics in China from 1990 to 2019][8]

    [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4417810.svg)](https://doi.org/10.5281/zenodo.4417810)


* [x] [省级行政区边界][g] 来自来自[中国科学院资源环境科学与数据中心][2]
* [x] [人口密度][d] 来自[worldpop.org][4]
* [x] [GDP密度][h] 来自[全球变化科学研究数据出版系统][7]
* [x] [河流分布][f] 来自[全国地理信息资源目录服务系统][6]
* [ ] 洪水频率


[1]:<https://www.gscloud.cn/sources/accessdata/305?pid=302>
[2]:<https://www.resdc.cn/DOI/DOI.aspx?DOIID=122>
[3]:<https://www.resdc.cn/DOI/DOI.aspx?DOIID=103>
[4]:<https://hub.worldpop.org/geodata/listing?id=76>
[5]:<https://data.tpdc.ac.cn/zh-hans/data/c3a67628-bb4d-4fb3-9bb2-0a2b88bdb6fe>
[6]:<https://www.webmap.cn/commres.do?method=result100W>
[7]:<https://www.geodoi.ac.cn/WebCn/doi.aspx?Id=125>
[8]:<https://zenodo.org/record/4417810#.ZAXdchVBxD8>

[a]:<https://riskevaluate.zyzh20021020.cn/DEM-90/DEM-90.zip>
[b]:<https://riskevaluate.zyzh20021020.cn/PRECIP/cn_precip.csv>
[c]:<https://riskevaluate.zyzh20021020.cn/TEMP/TEMP.zip>
[d]:<https://riskevaluate.zyzh20021020.cn/POPULAR/POPU.zip>
[e]:<https://riskevaluate.zyzh20021020.cn/WIND/GGWS-PCNN-wind_speed-197301202112_v330202202p.nc>
[f]:<https://riskevaluate.zyzh20021020.cn/RIVER/river.zip>
[g]:<https://riskevaluate.zyzh20021020.cn/BOARDER/border_2022.zip>
[h]:<https://riskevaluate.zyzh20021020.cn/GDP/GDP.zip>
[I]:<https://riskevaluate.zyzh20021020.cn/CLCD/CLCD.zip>