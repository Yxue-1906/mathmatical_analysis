# 老贼写书不带答案

[![GitHub version](https://badge.fury.io/gh/Yxue-1906%2Fmathmatical_analysis.svg)](https://github.com/Yxue-1906/mathmatical_analysis/releases/latest)
[![Build Status](https://github.com/Yxue-1906/mathmatical_analysis/workflows/Main/badge.svg)](https://github.com/Yxue-1906/mathmatical_analysis/releases)

## 项目说明

我的《数学分析习题课讲义》解答的备份，顺便也是学习LaTex.

欢迎提出issue斧正答案或者pull request

现在使用的宏包是[elegantbook](https://github.com/ElegantLaTeX/ElegantBook),将宏包选项中的result设置为noanswer即可消去答案.

## 自行编译

确保已安装Python以及[Texlive](https://www.tug.org/texlive/), 同时Windows系统需要安装Fonts文件夹下的四个字体文件

### Windows

- 替换格式文件, 一般来说应当是``%Texlive Install Directory%/<Year>/texmf-dist/tex/latex/elegantbook/``
- 运行``build.py``
- 执行两次``xelatex main.pdf``即可

### Linux

\* 本流程仅在Ubuntu20.04下进行过测试, 其他系统请自行测试

- 替换格式文件, 一般来说应当是在``/usr/share/texlive/texmf-dist/tex/latex/elegantbook/``下
- 在项目根目录下运行``make``即可 
