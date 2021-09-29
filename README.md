# UPC_AutoLogin
中国石油大学 UPC Web网页认证自动连接脚本 可使用自动计划任务将批处理命令在每次用户登录时执行Python脚本，实现无缝有网

使用方法：
修改UPC_AutoLogin.py中的账号和密码部分，保存。需要安装schedule和requests两个库
将UPC_AutoLogin.py和UPC_AutoLogin.bat文件放置在C盘根目录下（只是为了方便，可以更改地址，但是要做路径修改）
控制面板->管理工具->计划任务  新建一个计划任务，将.bat文件添加进去，触发器选择每次登陆时，延时选择2S后执行（V1.2可不选择延时执行）
