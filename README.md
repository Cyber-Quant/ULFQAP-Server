# Cyber Quant

## 开发运行环境搭建
### macOS
#### 安装开发工具
`brew install python mysql`

#### 配置mysql
运行

`mysql.server start`

启动mysql，然后运行

`mysql_secure_installation`

按提示操作，完成对mysql的初始化配置。主要是设置mysql的root用户登陆口令，后面用PASS代指。

然后登陆mysql

`mysql -uroot -pPASS`

在mysql的终端中依次运行

`use mysql;`

`update user set host='%' where user='root';` 用来允许mysql的root用户远程登陆。

`grant all privileges on *.* to 'root'@'%' with grant option;`

`alter user 'root'@'%' identified with mysql_native_password by 'PASS';`

`alter user 'root'@'%' identified by 'PASS' password expire never;`

`flush privileges;`

使用

`select user,host from user;`

来确认mysql root用户的`host`字段值是`%`

`Ctrl+D`退出mysql终端。

`mysql.server restart`重启mysql即可。

#### 创建数据库
登陆mysql

`mysql -uroot -pPASS`

在mysql的终端中运行

`create database cyber_quant default character set utf8mb4 collate 
utf8mb4_0900_ai_ci;`

来创建我们使用的叫做`cyber_quant`的数据库。

#### 安装python工具包
`pip3 install virtualenv`

#### 下载代码
`git clone https://github.com/Cyber-Quant/cyber-quant-be.git`

#### 创建运行环境并安装pip包
`cd cyber-quant-be`

`virtualenv venv`

`source venv/bin/activate`

`pip install django mysqlclient`

### Linux
参照macOS的自己弄吧，Linux用户动手能力都很强，都是UNIX，大同小异。


## 开发环境运行
`cd cyber-quant-be`

`source venv/bin/activate`

`python manage.py runserver`
