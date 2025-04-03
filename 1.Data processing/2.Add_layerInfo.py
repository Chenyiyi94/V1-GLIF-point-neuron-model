"""在point model里，v1_v1_edge_types.csv的文件，target query列没有layer信息，需要从bio model文件里的v1_v1_edge_types.csv里获取。"""

import pandas as pd


def add_layerinf_to_goalFile(source_file,goal_file,output_file):
    """
    从 source_file 中提取 node_type_id 和 pop_name，在 goal_file 中找到 node_type_id 匹配的行，
    并将 target_pop_name 作为新列添加到 goal_file 中。

    参数:
    - source_file: 源文件路径（bio csv file,with layer information）
    - goal_file: 目标文件路径（point csv file）
    - output_file: 输出文件路径（a new point csv file）
    """
    try:
        # 打印源文件和目标文件的列名
        with open(source_file, 'r', encoding='utf-8-sig') as f:
            header = f.readline().strip().split()
            print("源文件列名:", header)

        with open(goal_file, 'r',encoding='utf-8-sig') as f:
            header = f.readline().strip().split()
            print("目标文件列名:", header)

        df1 = pd.read_csv(source_file, encoding='utf-8-sig')
        df2 = pd.read_csv(goal_file, encoding='utf-8-sig')
        print("文件列数:", len(df1.columns))
        print("列名:", df1.columns.tolist())
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return


    node_to_pop_name = {}

    for index,row in df1.iterrows():
        target_query = row['target_query']
        if pd.isna(target_query) or target_query is None:  # 检查是否为空值
            print(f"Warning:空值出现在{index},跳过该行。")
            continue  # 跳过空值行
        parts = target_query.split('&')    # 以&作为分隔符
        if len(parts) == 2:
            node_type_id1 = parts[0]
            pop_name = parts[1].split('==')[1].strip("'")
            node_to_pop_name[node_type_id1] = pop_name
        else:
            print("An error in split.")

    df2['target_layer_information'] = None

    for index,row in df2.iterrows():
        target_query = row['target_query']
        if pd.isna(target_query) or target_query is None:  # 检查是否为空值
            print(f"Warning:空值出现在{index},跳过该行。")
            continue  # 跳过空值行
        node_type_id2 = target_query.split('&')[0]
        if node_type_id2 in node_to_pop_name:
            df2.at[index,'target_layer_information'] = node_to_pop_name[node_type_id2]

    df2.to_csv(output_file, index=False)
    print(f"Result was saved in {output_file}")


# use the above function
add_layerinf_to_goalFile(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_bio.csv',
                      r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_point.csv',
                      r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_point_addlayer.csv')


