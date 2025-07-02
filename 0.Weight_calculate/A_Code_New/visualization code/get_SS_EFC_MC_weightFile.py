import numpy as np
import pandas as pd
import re
import csv

# 假设 CSV 文件名为 'data.csv'
df = pd.read_csv(r'C:\Users\ChenYi\Desktop\network_simulation\Bouton Density\visualization code\new_point_v1_v1_edge_types.csv')


def extract_layer_info(source_query, target_layer_info):
    # 确保输入是字符串
    if not isinstance(source_query, str) or not isinstance(target_layer_info, str):
        return None

    # 去掉 source_query 中的 "pop_name==" 部分
    source_query = source_query.replace("pop_name=='", "").rstrip("'")
    # 使用正则表达式提取 source_query 中的数字
    source_match = re.search(r'[ei](\d+)', source_query)
    # 使用正则表达式提取 target_layer_info 中的数字
    target_match = re.search(r'[ei](\d+)', target_layer_info)

    if source_match and target_match:
        source_layer = int(source_match.group(1))
        target_layer = int(target_match.group(1))
        return f"Layer{source_layer}->{target_layer}"
    else:
        return None


# 应用函数到DataFrame的每一行
df['layer_info'] = df.apply(lambda row: extract_layer_info(row['source_query'], row['target_layer_information']),
                            axis=1)

# 输出结果
print(df[['edge_type_id', 'source_query', 'target_layer_information', 'layer_info']])

# 将修改后的DataFrame保存回CSV文件
df.to_csv(r'C:\Users\ChenYi\Desktop\network_simulation\Bouton Density\visualization code\new_point_v1_v1_edge_types_with_layer_info.csv', index=False)

# 标准化后的矩阵数据
normalized_matrices = {
    'VIS_VIS': np.array([[1.0, 1.0], [1.0, 1.0]]),
    'SS_SS': np.array([[0.211, 0.241], [0.049, 0.154]]),
    'EFC_EFC': np.array([[2.642, 3.111], [3.277, 0.986]]),
    'MC_MC': np.array([[1.064, 1.616], [4.087, 1.418]])
}

# 初始化字典来存储系数
coefficient_dicts = {}

# 定义映射关系
layer_mapping = {
    'VIS_VIS':['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5'],
    'SS_SS': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5'],
    'EFC_EFC': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5'],
    'MC_MC': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5']
}

# 遍历每个矩阵并生成相应的系数字典
for key, matrix in normalized_matrices.items():
    coefficients = []
    # 提取对角线和非对角线的值
    # 假设顺序是 [top-left, top-right, bottom-left, bottom-right]
    coefficients.append(matrix[0, 0])
    coefficients.append(matrix[0, 1])
    coefficients.append(matrix[1, 0])
    coefficients.append(matrix[1, 1])

    # 使用映射关系生成字典
    coefficient_dicts[key] = dict(zip(layer_mapping[key], coefficients))

# 打印结果
for key, coeff_dict in coefficient_dicts.items():
    print(f"{key}: {coeff_dict}")


# 假设 CSV 文件名为 'data.csv'
df2 = pd.read_csv(r'C:\Users\ChenYi\Desktop\network_simulation\Bouton Density\visualization code\new_point_v1_v1_edge_types_with_layer_info.csv')

# 定义一个函数来根据 layer_info 调整 syn_weight
def adjust_syn_weight(row):
    layer_info = row['layer_info']
    if layer_info in coefficient_dicts['MC_MC']:
        return row['syn_weight'] * coefficient_dicts['MC_MC'][layer_info]
    else:
        return row['syn_weight']  # 如果不匹配，则保持原值

# 应用函数来调整 syn_weight 列
df2['syn_weight_MC'] = df.apply(adjust_syn_weight, axis=1)

# 输出结果到控制台
print(df2)

# 如果需要，将修改后的 DataFrame 保存回 CSV 文件
df2.to_csv('point_v1_v1_edge_types_MC.csv', index=False)
