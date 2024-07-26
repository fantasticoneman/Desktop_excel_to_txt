①作为一个python编程新手，我知道这段代码还有很多不足之处。恳请各位前辈不吝赐教，指出其中的问题并分享您的经验。  
②软件实现的功能是把excel文件的内容通过特殊符号拼接起来，最后生成txt文本。  
③打包命令为：pyinstaller --onefile --noconsole --add-data "项目地址/ui/icons/feather/repeat.svg;icons/feather" --add-data "项目地址/ui/translations/*.qm;translations" -i 项目地址\ui\logo.ico .\main.py
---------------------------------------------------------
V1.0.0.2(2024.7.25)
1. 新增进度条重置功能，多次点击开始转换，进度条都会从0开始
2. 更新UI显示框架
---------------------------------------------------------
1. New progress bar reset function, multiple clicks to start conversion, progress bar will start from 0
2. Update UI display framework
---------------------------------------------------------
V1.0.0.1(2024.7.17)
1. 仅支持windows 10及以上操作系统
2. 解除中文“数量”列名限制，打印数量列名可以是中文“数量”或者是英文“Number of prints”（英文区分大小写）
3. 打印数量列情况细分：
	①当Excel里没有中文“数量”列名或者是英文“Number of prints”列名时，默认打印一次
	②当Excel里存在中文“数量”列名或者是英文“Number of prints”列名时，按存在列名下的数字进行打印
	③当Excel里同时存在中文“数量”列名及英文“Number of prints”列名时，按最左边的打印数量列名下的数字进行打印，其余当做需要打印内容
	④当Excel里存在多个中文“数量”列名或者是多个英文“Number of prints”列名时，按最左边的打印数量列名下的数字进行打印，其余当做需要打印内容
4. 英文翻译优化
---------------------------------------------------------
1. Only supports Windows 10 and above operating systems
2. Lift the restriction on Chinese "数量" column names, and print quantity column names can be either Chinese "数量" or English "Number of prints" (case sensitive in English)
3. Printing Breakdown:
	① When there is no Chinese column name for "数量" or English column name for "Number of prints" in Excel, it will be printed once by default
	② When there is a Chinese "数量" column name or an English "Number of prints" column name in Excel, print according to the number under the existing column name
	③ When there are both Chinese "数量" column names and English "Number of prints" column names in Excel, print according to the number under the leftmost printing quantity column name, and treat the rest as the content that needs to be printed
	④ When there are multiple Chinese "数量" column names or multiple English "Number of prints" column names in Excel, print according to the number under the leftmost printing quantity column name, and treat the rest as the content to be printed
4. English translation optimization
---------------------------------------------------------
V1.0.0.0(2024.7.16)
1. 支持中英文切换
2. 被转换Excel格式无要求，.xls或者是.xlsx都可以
3. 被转换Excel必须有一列的列名叫“数量”两个中文字，在哪一例没关系
4. 转换后的txt按电脑时间进行命名
---------------------------------------------------------
1. Support switching between Chinese and English
2. There is no requirement for converting to Excel format, either. xls or. xlsx are acceptable
3. To be converted to Excel, there must be a column name called "数量" with two Chinese characters. It doesn't matter which one it is
4. The converted txt is named according to computer time
