# OpenSSH基础教程
> OpenSSH(也被叫做OpenBSD Secure Shell)是一个基于SSH协议的网络套件。

## SSH(Secure Shell Protocol)
>下文为了简便起见，统一将其称为**ssh**

ssh应用基于客户端-服务器(C-S)架构，使用ssh客户端连接至ssh服务器。该协议能为客户端与服务器之间提供安全加密的连接。
## 使用例子
在该测试场景中，**A**lice与**B**ob分别拥有两台连接至Internet的计算机，他们的IP地址分别为`3.12.2.56`和`181.26.243.17`，
Alice希望连接到Bob的计算机上运行程序，因此她联系了Bob，希望使用ssh协议进行连接。Bob在他的计算机上搭建了ssh服务器。
连接时，有必要验证连接者的身份以保证安全。下面有两种验证方式。
## 用户名密码验证
> ssh服务端支持使用服务端计算机上已经存在的用户身份信息进行身份验证。

Bob在他的计算机上新建了Alice使用的账户，并将用户名(这里假设为`alice`)与密码分别告诉Alice。之后Alice便可以在她的终端之中执行以下命令
~~~
alice@A:~$ ssh alice@181.26.243.17
~~~
之后她会被要求输入预设的密码，验证成功之后便可以使用账户成功登录进入Bob的计算机，并获得用户`alice`相应的访问权限。
~~~
alice@A:~$ ssh alice@181.26.243.17
alice@A's password: # password here

alice@B:~$
~~~
> **密码验证的缺点**\
密码验证可以被暴力破解，因此是不安全的。在生产环境中，一般推荐使用*公钥验证*。

## SSH公钥验证
为了更好的理解这种验证方式，我们需要一些密码学基础知识。
### 加密、解密，Alice与Bob
> **为什么要加密？**\
> 互联网上的通信是不安全的，就像你上课给同学传的小纸条一样，其中的数据可以很容易的被监听或者篡改。收发双方获取到的信息因此会变得不一致，导致无法预期的行为。这种攻击通常被叫做中间人(Man-in-the-Middle)攻击。数据加密后对于第三方来说是不可见的，因此加密保障了通信的安全性。

* 对称加密

    这种加密算法加密与解密的密钥是相同的。
    使用常见的Alice与Bob假设，Alice与Bob共有一对预先共享的密钥(Pre-shared Key, PSK)，
    Alice加密后传输给Bob，随后Bob进行解密读出明文内容。
    将加密过程看作对于原文 $x$ 的函数，则加密函数为 $f(x)$ ，解密函数即为 $f^{-1}(x) $，
    二者为反函数。常见的ChaCha20，SM4，AES即为此类算法。
    > **对称加密的局限性**\
    > 上文提到Alice与Bob有一对预先共享的密钥(PSK)，但是若Alice与Bob之间没有安全的交换密钥的途径，直接传输密钥仍然可以使得其被第三方获取，从而使接下来的交流等同于明文。这就需要另一种加密算法。
* 非对称加密

    对于这种加密算法，加密与解密使用不同的密钥，分别称为**公钥**和**私钥**。使用公钥加密的明文只能用私钥进行解密。
    这样的算法数学表达即为 $d(c(x))=x$ ， $c(x)$ 为加密函数， $d(x)$ 为解密函数。\
    回到刚才的Alice与Bob假设。
    * Alice要向Bob发送信息，因此她撰写了明文 $x$ 。
    * Bob先向Alice发送他的公钥。Alice加密后发送的信息无法通过公钥解密，因此就算公钥被窃听也没问题。
    * Alice将公钥加密得到的信息 $c(x)$ 发送给Bob，之后Bob使用$d$对其进行解密，得到明文 $d(c(x))$ 。

    这种加密通常是单向的，只有Alice向Bob发送的信息才能被保护。\
    在实际使用中，通常Alice会向Bob加密发送对称加密的密钥，这样Bob就能安全的收到密钥，发起对称加密连接。这一过程被叫做**密钥交换(key exchange)**。密钥交换被广泛应用于我们的生活中，比如访问网站时的`https`协议便是基于`TLS(Transport Layer Security)`的`http`协议，而`TLS`协议在握手时便会进行密钥交换以建立安全信道。

    常见的非对称加密算法有RSA、ECDSA、ECDH等。

### 公钥验证方法
* 验证过程

    假设A计算机要连接到B计算机，在A、B计算机中分别存放了相配对的私钥和公钥。B计算机验证A计算机的身份时，可以采取以下步骤：
    * B生成一串随机数，使用公钥加密，发送给A。
    * A使用本地存储的私钥对密文进行解密，之后将解密得到的随机数发送给B。
    * B验证随机数是否相同，进而验证密钥对是否有效。

* 配置验证

    首先使用`ssh-keygen`命令生成密钥对。该命令通常已包含在ssh套件中。
    ~~~
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
    这会在`~/.ssh`目录下创建`id_rsa`和`id_rsa.pub`文件。扩展名为`.pub`的为公钥(pubkey)。
    > "`~`"代表当前用户的主目录。

    将`id_rsa`复制到Alice的`~/.ssh`目录下，将`id_rsa.pub`文件的内容追加到B计算机上Bob为Alice创建的对应用户的`~/.ssh/authorized_keys`文件中即可实现公钥验证。