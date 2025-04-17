import pandas as pd
import os

# CSV文件
csv_file = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data_files\our_result_point\spikes.csv'

# 生成对应的TXT文件路径
txt_file = os.path.splitext(csv_file)[0] + '.txt'

# 读取CSV文件
df = pd.read_csv(csv_file, header=0, names=['timestamps population node_ids'])
# 按空格分割列数据，并展开成多列
df = df['timestamps population node_ids'].str.split(' ', expand=True)

# 提取第一列和第三列
selected_columns = df.iloc[:, [0, 2]]

# 保存为TXT文件（无列名，空格分隔，不保存索引）
selected_columns.to_csv(txt_file, sep=' ', header=False, index=False)

print(f"文件已成功转换并保存为: {txt_file}")