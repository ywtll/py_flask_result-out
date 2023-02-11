# # py_flask_resultOut

#### 介绍

一个基于python flask web的一个用于学习平台，用于发布成绩的一个开源项目

#### 安装教程

1. 下载python3
   ```sh
   yum -y install python3
   ```
2. pip包
   ```sh
   pip3 install flask
   pip3 install pyyaml
   pip3 install xlrd
   pip3 install openpyxl
   ```

#### 运行

1. 进入到py_flask_resultOut/xl目录下面
   ```sh
   cd py_flask_result-out/xl
   ```
2. 修改xls文件，自行修改
3. 修改xl目录下的config.yaml文件
   ```sh
   id_src:
     "[姓名+密码的表格]"
   score_src:
     "[姓名+成绩的表格]"
   subject:
     "[在第二窗口显示的标题]"
   log_src:
     "[日志目录]"
   ```
4. 完成后回到py_flask_resultOut路径下运行：

5. 注意：
   
   默认是**443**端口，如果需要修改，需要到bin目录下的各个文件，修改
   
   nohup python3 -m flask run -h0.0.0.0 -p443 &
   
   中的 -p443 改为您喜欢的端口。
   
   并且在app.py中的最后一行 app.run(host='0.0.0.0', port=443)，
   
   中的 -p443 同样改为您喜欢的端口即可！

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

#### 感谢

1. 感谢JetBrain公司

