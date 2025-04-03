"""Add the ei and location/layer information to the spikes file."""
import pandas as pd
import os


def add_ei_info_to_spikes(spikes_file_path,nodes_file_path,output_suffix):
    """
    为spikes文件添加ei和location/layer信息，并保存为新的csv文件

    参数:
        spikes_file_path: spikes数据文件路径
        nodes_file_path: 节点类型数据文件路径
        output_suffix: 输出文件的后缀(如'efc','mc','vis')
    """
    try:
        spike_data = pd.read_csv(spikes_file_path, sep=r'\s+', header=0)
        node_type_data = pd.read_csv(nodes_file_path, sep=r'\s+', header=0)

        # Match spike_data's node_ids and  node_type_data's id, to get ei and layer information.
        spike_data_ei = spike_data.merge(
            node_type_data[['id', 'ei', 'location']],     # only select some column
            left_on='node_ids',               # 左表的匹配列
            right_on='id',                    # 右表的匹配列
            how='left'                        # 左连接，保留spike_data的所有行
        )

        print("print some spike_data_ei data")
        print(spike_data_ei.head(10))

        output_dir = os.path.dirname(spikes_file_path)
        output_filename = f"spike_data_ei_{output_suffix}.csv"
        output_path = os.path.join(output_dir, output_filename)

        # save file
        spike_data_ei.to_csv(output_path, index=False, sep=' ')
        print(f"files saved at：{output_path}")

        return spike_data_ei

    except Exception as e:
        print(f"Error when processing the file.")
        return None


# main program, using the above function.
if __name__ == "__main__":
    base_dir = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data files'

    # define some suffix
    suffixes = ['EFC', 'MC', 'VIS', 'SS']

    nodes_file = os.path.join(base_dir, 'raw data', 'v1_nodes.csv')

    for suffix in suffixes:
        spikes_filename = f"spikes_{suffix}.csv"
        spikes_file = os.path.join(base_dir, 'point spikes files', spikes_filename)

        # check if the file exists
        if not os.path.exists(spikes_file):
            print(f"Warning: file {spikes_file} does not exist, skip.")
            continue

        add_ei_info_to_spikes(
            spikes_file_path=spikes_file,
            nodes_file_path=nodes_file,
            output_suffix=suffix
        )

