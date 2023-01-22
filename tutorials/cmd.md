# 命令行基础教程
> 命令行，也称cmd(Command Prompt)。命令行构成的用户界面(cui)与图形界面(gui)为常见的两种计算机操作方式。

命令行操作有简洁、高效、准确等优点，在软件开发、系统运维中有广泛应用。一般的现代操作系统都提供命令行界面以供高级用户使用。\
接下来将会介绍一些背景知识。

## 输入输出(I/O)流
计算机与外界的信息交换均通过I/O流来实现。比如，键盘鼠标提供输入信息流，字符信息作为输出流。I/O的对象不只是计算机，该概念可以应用于计算机中的程序等。

## 终端(Terminal)
早期的个人电脑通常分为两部分，主机(Host)和终端(Terminal)。主机只负责计算，终端负责处理用户输入输出，将有关信息在屏幕上进行呈现。
>![](https://upload.wikimedia.org/wikipedia/commons/8/89/IBM_2260.jpg)\
图片中展示的便是IBM 2260计算机的终端界面。可以看到负责输出字符的显示器与电传打字机键盘。

如今编程中的很多概念均来自于终端，比如**换行**与**回车**的区别。本篇教程不再过多叙述冗长的历史，若想进一步了解可以阅读[Terminal的英文维基百科页面](https://en.wikipedia.org/wiki/Computer_terminal)。

虽然之后操作系统发展出了图形界面以方便大众使用，终端仍然以一种相对高级的操作方式留存在操作系统中。直接与终端互动的方式已经大部分被淘汰，在图形界面中访问终端通常需要借助***终端模拟器***。对于Windows用户，你会在进入命令提示符的时候看到终端窗口。对于Linux用户，图形界面下的`Konsole`以及其他应用程序便是终端模拟器，但在`systemd` 达成`graphical.target`之前是与终端的直接互动。

### 常用的终端模拟器
* Windows
    * Windows 控制台主机
    * Windows Terminal
* Linux
    * 取决于你使用的桌面环境
* macOS
    * Terminal

## shell
shell是命令行界面的解析器。用户访问终端需要与该程序交互以实现相关功能。
>广义的shell并不仅指命令解释器，也可以指代图形界面提供程序，比如Windows下的`explorer.exe`。

shell的许多规则继承自比Windows和Linux更久远的Unix。
### 常见的shell
* Windows
    * cmd
    * PowerShell
* 类Unix
    * sh
    * bash
    * zsh

### shell基本操作
* 你可以使用键盘的方向键在shell中进行导航。常见的操作是上下箭头可以浏览命令历史记录，左右箭头用来移动光标
* Home 与 End 键可快速移动到命令的首尾
* Ctrl-C(^C)键用于终止当前任务

### 环境变量
shell中也存在着变量，这些变量在程序执行时可以被程序读取来做出有关响应。比如：
~~~
PS C:\Users\zyzh0> ls env:

Name                           Value
----                           -----
ALLUSERSPROFILE                C:\ProgramData
APPDATA                        C:\Users\zyzh0\AppData\Roaming
asl.log                        Destination=file
CommonProgramFiles             C:\Program Files\Common Files
CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
CommonProgramW6432             C:\Program Files\Common Files
COMPUTERNAME                   SHELL-DESKTOP-H
ComSpec                        C:\WINDOWS\system32\cmd.exe
DriverData                     C:\Windows\System32\Drivers\DriverData
FPS_BROWSER_APP_PROFILE_STRING Internet Explorer
FPS_BROWSER_USER_PROFILE_ST... Default
HOMEDRIVE                      C:
HOMEPATH                       \Users\zyzh0
JAVA_HOME                      C:\Program Files\Microsoft\jdk-17.0.4.8-hotspot\
LOCALAPPDATA                   C:\Users\zyzh0\AppData\Local
LOGONSERVER                    \\SHELL-DESKTOP-H
NUMBER_OF_PROCESSORS           8
OneDrive                       C:\Users\zyzh0\OneDrive
OneDriveConsumer               C:\Users\zyzh0\OneDrive
OS                             Windows_NT
Path                           C:\ProgramData\Anaconda3\Library\bin;C:\Program Files\Microsoft\jdk-17.0.4.8-hotspot\...
PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL
PROCESSOR_ARCHITECTURE         AMD64
PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
PROCESSOR_LEVEL                6
PROCESSOR_REVISION             3c03
ProgramData                    C:\ProgramData
ProgramFiles                   C:\Program Files
ProgramFiles(x86)              C:\Program Files (x86)
ProgramW6432                   C:\Program Files
PSModulePath                   C:\Users\zyzh0\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell...
PUBLIC                         C:\Users\Public
PyCharm Community Edition      C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.1\bin;
SystemDrive                    C:
SystemRoot                     C:\WINDOWS
TEMP                           C:\Users\zyzh0\AppData\Local\Temp
TMP                            C:\Users\zyzh0\AppData\Local\Temp
USERDOMAIN                     SHELL-DESKTOP-H
USERDOMAIN_ROAMINGPROFILE      SHELL-DESKTOP-H
USERNAME                       zyzh0
USERPROFILE                    C:\Users\zyzh0
windir                         C:\WINDOWS
WSLENV                         WT_SESSION::WT_PROFILE_ID
WT_PROFILE_ID                  {61c54bbd-c2c6-5271-96e7-009a87ff44bf}
WT_SESSION                     4e60b6f2-357d-4b54-ae2a-48e7b34e21b3
PS C:\Users\zyzh0>
~~~
该命令列出了Windows系统环境下当前存在的所有环境变量。\
又比如:
~~~
root@iZf8zd8nr6i1432p4s9vujZ:~# set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:globasciiranges:histappend:interactive_comments:login_shell:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=([0]="0")
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION_VERSINFO=([0]="2" [1]="11")
BASH_LINENO=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="5" [1]="1" [2]="16" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
BASH_VERSION='5.1.16(1)-release'
COLUMNS=161
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/0/bus
DIRSTACK=()
EUID=0
GROUPS=()
HISTCONTROL=ignoredups:ignorespace
HISTFILE=/root/.bash_history
HISTFILESIZE=2000
HISTSIZE=1000
HOME=/root
HOSTNAME=iZf8zd8nr6i1432p4s9vujZ
HOSTTYPE=x86_64
IFS=$' \t\n'
LANG=en_US.UTF-8
LESSCLOSE='/usr/bin/lesspipe %s %s'
LESSOPEN='| /usr/bin/lesspipe %s'
LINES=63
LOGNAME=root
LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:'
MACHTYPE=x86_64-pc-linux-gnu
MAILCHECK=60
# ...
~~~
这是Ubuntu环境下存在的环境变量。

### 内部与外部命令
内部命令指shell与os自带的命令，可以被直接执行。外部命令则并不集成在shell中，他们往往是独立的程序，shell调用他们来执行相关操作。\
shell会在一个叫做`PATH`的环境变量中读取外部命令存储的路径。`PATH`中存储的都是目录信息。当shell执行外部命令时，他会优先在`PATH`中包含
的目录内搜索同名的文件加以执行。

### 参数
命令一般要跟相关参数以定义要执行的操作。比如`ping`:
~~~
PS C:\Users\zyzh0> ping bing.com

正在 Ping bing.com [204.79.197.200] 具有 32 字节的数据:
来自 204.79.197.200 的回复: 字节=32 时间=74ms TTL=113
来自 204.79.197.200 的回复: 字节=32 时间=77ms TTL=113
来自 204.79.197.200 的回复: 字节=32 时间=71ms TTL=113
来自 204.79.197.200 的回复: 字节=32 时间=77ms TTL=113

204.79.197.200 的 Ping 统计信息:
    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 71ms，最长 = 77ms，平均 = 74ms
PS C:\Users\zyzh0>
~~~
我们可以追加不同的参数以达到不同的效果。
~~~
PS C:\Users\zyzh0> ping -n 1 bing.com

正在 Ping bing.com [204.79.197.200] 具有 32 字节的数据:
来自 204.79.197.200 的回复: 字节=32 时间=106ms TTL=113

204.79.197.200 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 106ms，最长 = 106ms，平均 = 106ms
PS C:\Users\zyzh0>
~~~
我们指定了参数`-n 1`，这表明只需要`ping`一次。\
通常，有关命令的帮助页面里会详细讲述参数名称以及作用。
~~~
用法: ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS]
            [-r count] [-s count] [[-j host-list] | [-k host-list]]
            [-w timeout] [-R] [-S srcaddr] [-c compartment] [-p]
            [-4] [-6] target_name

选项:
    -t             Ping 指定的主机，直到停止。
                   若要查看统计信息并继续操作，请键入 Ctrl+Break；
                   若要停止，请键入 Ctrl+C。
    -a             将地址解析为主机名。
    -n count       要发送的回显请求数。
    -l size        发送缓冲区大小。
    -f             在数据包中设置“不分段”标记(仅适用于 IPv4)。
    -i TTL         生存时间。
    -v TOS         服务类型(仅适用于 IPv4。该设置已被弃用，
                   对 IP 标头中的服务类型字段没有任何
                   影响)。
    -r count       记录计数跃点的路由(仅适用于 IPv4)。
    -s count       计数跃点的时间戳(仅适用于 IPv4)。
    -j host-list   与主机列表一起使用的松散源路由(仅适用于 IPv4)。
    -k host-list    与主机列表一起使用的严格源路由(仅适用于 IPv4)。
    -w timeout     等待每次回复的超时时间(毫秒)。
    -R             同样使用路由标头测试反向路由(仅适用于 IPv6)。
                   根据 RFC 5095，已弃用此路由标头。
                   如果使用此标头，某些系统可能丢弃
                   回显请求。
    -S srcaddr     要使用的源地址。
    -c compartment 路由隔离舱标识符。
    -p             Ping Hyper-V 网络虚拟化提供程序地址。
    -4             强制使用 IPv4。
    -6             强制使用 IPv6。
~~~