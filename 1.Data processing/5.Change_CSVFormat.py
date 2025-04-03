"""Change csv file format to match the  V1 point model network's requirement."""

import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_EFC.csv')

# 将两列数据对调
column1 = 'syn_weight'  # 替换为第一列的名称
column2 = 'syn_weight_EFC_EFC'  # 替换为第二列的名称
df[column1], df[column2] = df[column2], df[column1]

# 将某一列数据的小数点保留10位
column_to_round = 'syn_weight'  # 替换为要保留小数位的列名
df[column_to_round] = df[column_to_round].round(12)

# 取前九列的数据
df = df.iloc[:, :9]  # 选择所有行的前9列

# save file
df.to_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_EFC.csv', sep=' ', index=False)  # 设置空格作为分隔符

