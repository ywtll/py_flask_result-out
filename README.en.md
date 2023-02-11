
# py_flsk_ resultOut
####Introduction
An open source project based on python flask web for learning platform and for publishing results
####Installation Tutorial
1. Download python3
```sh
yum -y install python3
```
2. pip package
```sh
pip3 install flask
pip3 install pyyaml
pip3 install xlrd
pip3 install openpyxl
```
####Run
1. Enter py_ flask_ Under the resultOut/xl directory
```sh
cd py_ flask_ result-out/xl
```
2. Modify the xls file and modify it yourself
3. Modify the config.yaml file in the xl directory
```sh
id_ src:
"[name+password form]"
score_ src:
"[name+score table]"
subject:
"[Title displayed in the second window]"
log_ src:
[Log directory]
```
4. Return to py after completion_ flask_ Run under the resultOut path:
5. Note:
The default is * * 443 * * port. If you need to modify it, you need to go to each file in the bin directory and modify it
nohup python3 -m flask run -h0.0.0.0 -p443 &
Change the - p443 in to your preferred port.
And in the last line of app.py, app.run (host='0.0.0.0 ', port=443),
The - p443 in can also be changed to your preferred port!
####Participation contribution
1. Fork warehouse
2. New Feat_ Xxx branch
3. Submit code
4. Create a new Pull Request
####Thank you
1. Thank JetBrainask_resultOut
