# 删除处理过的csv文件里的两个列，使得新的csv文件匹配固定的格式

import pandas as pd

# 读取 CSV 文件
df = pd.read_csv(r'C:\Users\ChenYi\Desktop\network_simulation\Bouton Density\visualization code\point_v1_v1_edge_types_EFC.csv')

# 删除指定的三列
df = df.drop(columns=['syn_weight_init', 'target_layer_information', 'layer_info'])

# 保存修改后的文件
df.to_csv('v1_v1_edge_types_EFC.csv', index=False)

print("列已删除，文件已保存为。")