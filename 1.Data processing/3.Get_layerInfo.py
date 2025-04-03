"""从csv file 的 source query 和 target layer info 这两列里提取layer x->y的信息，记录为新列layer_info的值。"""

import numpy as np
import pandas as pd
import re
import csv

# load csv file
df = pd.read_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_point_addlayer.csv')


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
df['layer_info'] = df.apply(lambda row: extract_layer_info(row['source_query'], row['target_layer_information']),axis=1)


print(df[['edge_type_id', 'source_query', 'target_layer_information', 'layer_info']])

# save result file
df.to_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_point_with_layerInfo.csv', index=False)

