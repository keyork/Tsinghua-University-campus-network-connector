# Tsinghua-University-campus-network-connector
## 1 介绍
Ubuntu，Firefox浏览器，使用selenium的方式自动填充用户名和密码登陆清华大学校园网。

## 2 使用方法
1. 请到这里下载[浏览器驱动](https://github.com/mozilla/geckodriver/releases)；
2. 下载完成后，将驱动移动至`/usr/bin/`目录下
```
cp geckodriver /usr/bin
```
3. 环境配置
```
pip install selenium
pip install Pyyaml
```
4. 修改`userinfo.yaml`中的信息，在冒号后填入校园网的用户名和密码
5. 运行程序，自动连接校园网
```
python auto_login.py 1
```
或
```
python auto_login.py 2
```
注：后面为1，则单次登录；后面为2，则每10分钟登录/检查一次。
## 3 Enjoy it