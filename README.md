# minghua78
for minghua78 by flask
在heroku部署时有两个问题

1. 使用windows的命令行生成requirements会有编码问题，查看日志发现heroku平台会报错，提示requirements.txt出错：TypeError: must be encoded string without NULL bytes, not str，需要将文件编码转为utf-8，再次上传github即可。

2.如果一开始部署的时候缺少Procfile文件，后续即使提示部署成功依然不能访问，查看日志提示提示：No web processes running github。 需要在上传Profile，然后heroku删除app之后重新创建app（不删除即使上传profile依然会有同样错误）。


其他问题

heroku平台使用py2，python版本不同可能导致环境初始化失败
