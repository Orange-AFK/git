------基于Linux环境------

django学习简要笔记
学习资源来自b站:http://space.bilibili.com/252028233/#/channel/detail?cid=28138
感谢up主的无私分享！在此附上视频资源url。若您意外看到此文档又刚好想要学习django2.0请毫不犹豫点击以上链接
笔记仅为个人学习记录方便查阅故此放在git上

1.建立虚拟环境
	python -m venv 虚拟环境名称

2.激活虚拟环境
	source 虚拟环境名称/bin/activate

3.停止虚拟环境
	deactivate

4.安装django(虚拟环境激活的情况下)
	pip install django

5.在django中创建项目
	django-admin startproject 项目名称 .

6.设置后台管理为中文界面
编辑全局设置settings.py文件找到LANGUAGE_CODE字段，修改参数为
zh-Hans
