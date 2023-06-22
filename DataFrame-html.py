import pandas as pd
# 读取之前爬取的表格数据
table = pd.read_csv("Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv")
# 将表格数据转换成HTML格式
html = table.to_html()
# 打印HTML格式的表格数据
print(html)
