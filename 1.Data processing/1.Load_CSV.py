"""读取bio_model 和 point model 的 v1_v1_edge_types.csv文件"""

import pandas as pd


def standardize_point_csv(input_file,output_file):
    """
    将非标准的CSV文件处理为标准的CSV文件，并保存为Python可以轻松读取的格式。
    参数:
    - input_file: 输入文件路径（非标准 CSV 文件）
    - output_file: 输出文件路径（标准 CSV 文件）
    """
    # 初始化空列表存储数据
    data = []

    # 打开文件并读取
    with open(input_file, 'r') as file:
        columns = file.readline().strip().split(' ')[:10]         # 读取第一行作为列名，只读取前10列的数据。
        # 读取剩余行作为数据
        for line in file:
            # 去除行首尾的空白字符，并按空格分割，只读取前8列的数据。
            row = line.strip().split(' ')[:10]
            # 将每一行的数据添加到 data 列表中
            data.append(row)

    # 将数据转换为 pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    # 打印数据框的前几行
    print("文件内容预览：")
    print(df.head())
    print("文件列数:", len(df.columns))
    print("列名:", df.columns.tolist())
    # 保存为标准的 CSV 文件
    df.to_csv(output_file, index=False, encoding='utf-8-sig', sep=',')
    print(f"文件已保存为 {output_file}")


def standardize_bio_csv(input_file,output_file):
    # 初始化空列表存储数据
    data = []

    # 打开文件并读取
    with open(input_file, 'r') as file:
        columns = file.readline().strip().split(' ')[:8]         # 读取第一行作为列名，只读取前8列的数据。因为第9列是特殊格式，难处理。
        # 读取剩余行作为数据
        for line in file:
            # 去除行首尾的空白字符，并按空格分割，只读取前8列的数据。
            row = line.strip().split(' ')[:8]
            # 将每一行的数据添加到 data 列表中
            data.append(row)

    # 将数据转换为 pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    # 打印数据框的前几行
    print("文件内容预览：")
    print(df.head())
    print("文件列数:", len(df.columns))
    print("列名:", df.columns.tolist())
    # 保存为标准的 CSV 文件
    df.to_csv(output_file, index=False, encoding='utf-8-sig', sep=',')
    print(f"文件已保存为 {output_file}")


# load point model's csv file
file_path1 = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\point_network_dynsyns\v1_v1_edge_types.csv'
output_path1 = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_point.csv'
standardize_point_csv(file_path1, output_path1)

# load bio_model's csv file
file_path2 = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\bio_network\v1_v1_edge_types.csv'
output_path2 = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files\result data\v1_v1_edge_types_bio.csv'
standardize_bio_csv(file_path2, output_path2)




