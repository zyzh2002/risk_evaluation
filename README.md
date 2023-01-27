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

***
## 数据来源
项目的主要数据均上传至腾讯云cos存储桶。预期数据时间跨度为2000-2015年。
>项目的数据仍处于收集中，***资源不全***。
### 数据列表
* ✅[DEM（90m）][a] 来自[地理空间数据云][1]
* ⭕[降雨量][b] 来自[中国科学院资源环境科学与数据中心][2]，数据结构[如此][3]
* ⭕[温度][c] 来自[中国科学院资源环境科学与数据中心][2]
* ❎土地利用率
* ⭕[人口密度][d] 来自[worldpop.org][4]
* ❎GDP密度
* ❎河流分布
* ❎洪水频率


[1]:<https://www.gscloud.cn/>
[2]:<https://www.resdc.cn/>
[3]:<https://www.resdc.cn/DOI/DOI.aspx?DOIID=103>
[4]:<https://hub.worldpop.org/geodata/listing?id=76>

[a]:<https://riskevaluate.zyzh20021020.cn/DEM-90/DEM-90.zip>
[b]:<https://riskevaluate.zyzh20021020.cn/PRECIP/中国陆地1948-2016年降水量数据集.csv>
[c]:<https://riskevaluate.zyzh20021020.cn/TEMP/TEMP.zip>
[d]:<https://riskevaluate.zyzh20021020.cn/POPULAR/chn_pd_2000_1km_ASCII_XYZ.zip>