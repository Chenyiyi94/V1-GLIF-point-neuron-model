import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 权重矩阵存储在一个NumPy数组或Pandas DataFrame中
weights = {
    'VIS_VIS': np.array([[292.697, 210.606], [38.0, 293.071]]),
    'SS_SS': np.array([[61.75, 50.679], [1.878, 45.076]]),
    'EFC_EFC': np.array([[773.316, 655.184], [124.543, 289.029]]),
    'MC_MC': np.array([[311.333, 340.333], [155.3, 415.633]])
}
# 使用列表推导式展开
weights_list = [item for sublist in weights.values() for item in sublist.flatten()]
print(weights_list)

# 创建一个2x2子图的图像
fig,axes = plt.subplots(2,2,figsize=(12,12))

# 遍历权重矩阵并创建热图
for i,(label, matrix) in enumerate(weights.items()):
    # 确定子图的位置
    row = i // 2
    col = i % 2

    sns.heatmap(matrix, annot=True, fmt=".3f", cmap='coolwarm',ax=axes[row,col])
    axes[row,col].set_title(f'Connection Weight Heatmap/Matrix for {label}')
    axes[row, col].set_xticklabels(['goal_layer2/3', 'goal_layer5'])
    axes[row,col].set_yticklabels(['source_layer2/3', 'source_layer5'])


plt.subplots_adjust(hspace=0.2)
#plt.tight_layout()
plt.show()

# 将权重矩阵进行处理，VIS区域视为1（基准），其他区域转化为该基准的背书关系。
# 获取基准矩阵（VIS_VIS）
baseline_matrix = weights['VIS_VIS']

# 初始化一个字典用于存储标准化后的矩阵
normalized_weights = {}

# 计算每个区域的标准化矩阵
for region, matrix in weights.items():
    # 通过逐元素除法计算倍数关系
    normalized_matrix = matrix / baseline_matrix
    normalized_weights[region] = np.round(normalized_matrix,3)  # 保留三位小数点

# 输出标准化后的矩阵
for region, matrix in normalized_weights.items():
    print(f"{region} normalized matrix:")
    print(matrix)
    print()

# 创建一个新的2x2子图的图像
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

# 遍历标准化后的权重矩阵并创建热图
for i, (label, matrix) in enumerate(normalized_weights.items()):
    row = i // 2
    col = i % 2
    sns.heatmap(matrix, annot=True, fmt=".3f", cmap='coolwarm', ax=axes[row, col])
    axes[row, col].set_title(f'Normalized Weight Heatmap for {label}')
    axes[row, col].set_xticklabels(['goal_layer2/3', 'goal_layer5'])
    axes[row, col].set_yticklabels(['source_layer2/3', 'source_layer5'])

plt.subplots_adjust(hspace=0.3)
plt.show()