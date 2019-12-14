import pickle






# 存储其他类型的数据

list = [12,'nihao', 'xiaoming']
with open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\myFirst.txt', 'wb') as f:
    pickle.dump(list, f)

with open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\myFirst.txt', 'rb') as f:
    si = pickle.load(f,encoding='utf-8')
    print(si)