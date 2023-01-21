# GitHub基础教程
<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width=80>\
这篇教程会对Github的注册以及基础操作进行教学。\
本教程中包含的可能需要你熟悉的其他概念有：
1. git基本操作
2. openSSH基本操作
3. 命令行入门

## 什么是GitHub？
> GitHub, Inc. is an Internet hosting service for software development and version control using Git. It provides the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project.

GitHub是一个使用Git进行软件开发版本控制的网站。对于新手，可以把它看作一个云端的多人git repo。

## 如何注册？
> 因为某些不可抗力原因，GitHub在中国大陆的访问常常被防火长城（GFW）干扰或阻断。因此对于中国大陆地区的用户，推荐使用科学上网来进行注册等一系列操作。

通常只需点击初始页面右上角的"Sign Up"按钮。\
![](https://riskevaluate.zyzh20021020.cn/img/1.png)\
在这之后，输入你的电子邮箱并点击确认邮件中的链接进行注册。

## 配置SSH公钥与私钥
>要方便的进行仓库的拉取操作，需要配置SSH密钥对来对仓库的访问进行身份验证。


该步骤的本质便是将SSH公钥上传至GitHub来对访问时客户端持有的私钥进行身份验证。如果你熟悉openSSH，那么你已经知道怎么做了。
对于初次入门者，请遵循以下步骤。
> 该步骤适用于Win10/Win11桌面环境。如果你使用Linux估计也不用我教吧（

1. 运行`ssh-keygen`命令生成密钥对
~~~cmd
PS C:\Users\zyzh0> ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\zyzh0/.ssh/id_rsa): # Enter
Enter passphrase (empty for no passphrase): # Enter
Enter same passphrase again: # Enter
Your identification has been saved in C:\Users\zyzh0/.ssh/id_rsa.
Your public key has been saved in C:\Users\zyzh0/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:0Tka0Cgh32YWiLPynzDzoTdqa89ZoaUpTN2QGb2uOQ4 zyzh0@SHELL-DESKTOP-H
The key's randomart image is:
+---[RSA 3072]----+
|  ..o+oo         |
|  ooo=oo.. .     |
|   o=.=.o +      |
|. .. *.  + .     |
| o. ..+ S        |
| o= .=..         |
|  EB+=.          |
|  ++Xo           |
| oo*=o           |
+----[SHA256]-----+
PS C:\Users\zyzh0>
~~~
这会在当前用户的`.ssh`目录下创建`id_rsa`和`id_rsa.pub`文件。扩展名为`.pub`的为公钥(pubkey)。该密钥对使用了非对称加密算法中的一种（[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))），其简单原理便是利用质因数分解（将质数相乘得到一个数很容易，反之要得到具体的质数却十分困难），使用公钥加密的数据只能用私钥进行解密。我们可以查看他们。
~~~cmd
PS C:\Users\zyzh0> cat C:\Users\zyzh0/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
PS C:\Users\zyzh0> cat C:\Users\zyzh0/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDo5eHWV9NGfYOkBi1iwo9n6zkAyRzronwmXkIbwUJt7cmwYT3MSDRDAmRpFom1AuwKccOQV8HaqhggSgvSkw655z/N3xgpi8ioSilG5Hw3GvcKqYm+ZobAbx48DycYATvdmz0Vdi1KY6wroQcZA9V3edr6vJf9SsLx7npOBZphY6h0Z7RVXAvzfBoLbZ2FeJt+/a4CWbIiJqtU/eglDOwayUCpu29UBVrICeKgtU0hfF8Tm1GN/DRl5YMkskyE4xjgCD7fEgT65i22fMkrwHJN9YULUgP2bmyZpXDWYmRpyw5WxU2Fq43o0JP2QXhuKSV3nXMqdzW7C8yqNb4wOUBR9SSNsQAxC3VdynU2D1tK1pQx8ftRz/tJVwzntoWloMUqxppkVOv6h+Nu85hhjebJzE7Pumu1QJ2hX7TllFXnOKdAmYXOL1/FCGNM0Hx0RYYdvzqfFprh9K72thq+mMZVYwk28P97OU1shRH71aRzoEzMZQKF7GKWlXs0SYZCPlk= zyzh0@SHELL-DESKTOP-H
PS C:\Users\zyzh0>
~~~
我们要上传到GitHub的便是公钥文件。

2. 公钥上传

进入账户设置\
![](https://riskevaluate.zyzh20021020.cn/img/4.png)\
点击左侧**SSH and GPG keys**进入相关设置选项\
![](https://riskevaluate.zyzh20021020.cn/img/5.png)
点击**New SSH key**，将刚才获取的公钥文件粘贴至文本框中，点击添加。
## 如何创建仓库并与本地相关联
进入你的个人主页。
![](https://riskevaluate.zyzh20021020.cn/img/2.png)\
在左侧有一个很显眼的"New"按钮。点击他即可进入新建仓库页面。
![](https://riskevaluate.zyzh20021020.cn/img/3.png)\
你可以选择仓库使用的模板，仓库名称，公有或私有以及开源许可协议等。创建完之后，便可以进行仓库的初始化设置。一般使用SSH协议以方便身份验证。\
接下来介绍两种方法。

### 创建本地仓库并设置origin
> 本教程假定你已熟练掌握git的基本操作
~~~bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin <repo addr>
git push -u origin main
~~~
### 直接拉取远程仓库到本地
~~~bash
git clone <repo addr>
~~~

至此，你便可以像使用git的远程仓库一样操作GitHub上的仓库。