------基于Linux环境------

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
