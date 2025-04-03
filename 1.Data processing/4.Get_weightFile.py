"""根据layer x->y的值和系数矩阵来修改syn_weight的值，得到对应于SS、EFC、MC区域的csv files."""

import numpy as np
import pandas as pd

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
    'VIS_VIS': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5'],
    'SS_SS': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5'],
    'EFC_EFC': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5'],
    'MC_MC': ['Layer23->23', 'Layer23->5', 'Layer5->23', 'Layer5->5']
}

# 遍历每个矩阵并生成相应的系数字典
for key, matrix in normalized_matrices.items():
    coefficients = []
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


# load csv file
df = pd.read_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_point_with_layerInfo.csv')


# 定义一个函数来根据 layer_info 调整 syn_weight
def adjust_syn_weight(row):
    layer_info = row['layer_info']
    if layer_info in coefficient_dicts['EFC_EFC']:     # 修改这个参数，获取不同region的csv文件
        return row['syn_weight'] * coefficient_dicts['EFC_EFC'][layer_info]
    else:
        return row['syn_weight']  # 如果不匹配，则保持原值


# 应用函数来调整 syn_weight 列
df['syn_weight_EFC_EFC'] = df.apply(adjust_syn_weight, axis=1)

print(df)

# save files
df.to_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_EFC.csv', index=False)
