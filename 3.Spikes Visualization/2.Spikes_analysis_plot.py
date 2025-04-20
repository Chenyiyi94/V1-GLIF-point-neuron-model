""" Basic statistical analysis and visualization of spikes files of V1 point model.  2025-03-17  Author:Chen Yi """
import pandas as pd
import matplotlib
matplotlib.use('TKAgg') # 使用TK后端
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.lines import Line2D

plt.rcParams['agg.path.chunksize'] = 10000  # 防止大数据崩溃

# set global style
plt.style.use('seaborn-v0_8')  # or ggplot
sns.set_palette("husl")


class SpikeAnalyzer:
    def __init__(self, file_path, output_dir="plots"):
        """init and load data"""
        plt.rcParams['toolbar'] = 'None'  # 禁用工具栏减少冲突
        plt.rcParams['figure.max_open_warning'] = 0  # 取消图形数量警告
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.df = pd.read_csv(file_path, sep=r'\s+', header=0)
        self.dataset_name = os.path.basename(file_path).split('_')[-1].split('.')[0].upper()
        self.color_map = {'e': 'red', 'i': 'blue'}
        self.results = {}

    def analyze(self):
        """do the whole analysis process"""
        self._basic_stats()
        self._calculate_firing_rates()
        self._plot_spike_raster()
        self._plot_timestamp_distribution()
        self._plot_firing_rates()
        self._plot_firing_rate_distribution()
        return self.results

    def _basic_stats(self):
        """calculate basic statistic information"""
        print("_basic_stats")
        self.results['total_spikes'] = len(self.df)
        self.results['num_neurons'] = self.df['node_ids'].nunique()
        self.results['average_spikes_per_neuron'] = self.results['total_spikes'] / self.results['num_neurons']

    def _calculate_firing_rates(self):
        print("_calculate_firing_rates")

        """calculate neuron's firing frequency"""
        spike_counts = self.df['node_ids'].value_counts()
        total_time = (self.df['timestamps'].max()-self.df['timestamps'].min()) / 1000   # ms->s
        self.average_firing_rates = spike_counts/total_time       # 频率 = 次数/时长
        self.results['total_time_seconds'] = total_time
        self.results['average_firing_rate'] = self.average_firing_rates.mean()    # ？？？mean?

    def _plot_spike_raster(self, layer_height_mode='equal'):
        """Raster plot or Scatter plot, and tag layer information."""
        print("_plot_spike_raster")

        try:
            plt.figure(figsize=(12, 8))

            # 1.get layer information.
            layers = sorted(self.df['location'].unique())
            max_id = self.df['node_ids'].max()

            custom_heights = {1: 0.8, 2: 1.1, 3: 1.1, 4: 1.0, 5: 1.1}

            print("2.set Y-axis range")

            # 2.set Y-axis range
            if layer_height_mode == 'equal':
                layer_height = max_id * 1.1
                y_offsets = {layer: i*layer_height for i, layer in enumerate(layers)}
                total_height = len(layers) * layer_height
            elif layer_height_mode == 'custom':
                base_height = max_id * 1.2
                y_offsets = {}
                current_y = 0
                for layer in layers:
                    y_offsets[layer] = current_y
                    current_y += base_height * custom_heights.get(layer, 1.0)
                total_height = current_y
            else:
                raise ValueError("layer_height_mode must be 'equal' or 'custom'")

            # 3.set background color
            print("3.set background color")

            for i, layer in enumerate(layers):
                colors = '#444444' if i % 2 == 0 else 'white'

                plt.axhspan(ymin=y_offsets[layer],
                            ymax=y_offsets[layer] + + (layer_height if layer_height_mode == 'equal'
                                                       else base_height * custom_heights.get(layer, 1.0)),
                            facecolor=colors, alpha=0.3, zorder=0)

            # 4.Plot data points
            print("4.Plot data points")

            for layer in layers:
                layer_data = self.df[self.df['location'] == layer]
                y = layer_data['node_ids'] + y_offsets[layer]
                colors = layer_data['ei'].map(self.color_map)
                plt.scatter(x=layer_data['timestamps'], y=y, c=colors, s=3, alpha=0.3, edgecolors='none', zorder=3)
            print("sssssssssssssssssssssssssssss")

            plt.ylim(0, total_height)
            plt.title(f'Spike Raster Plot -- {self.dataset_name}', fontsize=14)
            plt.xlabel('Timestamps (ms)', fontsize=12)
            plt.ylabel('Node ID(Group by Layer)', fontsize=12)

            # 5.calculate and set the Y-axis position
            print("5.calculate and set the Y-axis position")

            y_ticks_pos = []
            for layer in layers:
                if layer_height_mode == 'equal':
                    pos = y_offsets[layer] + layer_height / 2
                else:
                    pos = y_offsets[layer] + (base_height * custom_heights.get(layer, 1.0)) / 2
                y_ticks_pos.append(pos)

            plt.yticks(y_ticks_pos, [str(layer).replace("Vis", "") for layer in layers])   # 将Y轴刻度设置为每层中间位置，并标注层号

            plt.grid(False)
            plt.tight_layout()
            # plt.show()
            output_path = os.path.join(self.output_dir, f"raster_{self.dataset_name}.png")
            plt.savefig(output_path, dpi=150, bbox_inches='tight')
            print(f"图形已保存至: {output_path}")
        except Exception as e:
            print(f"Plotting save failed:{str(e)}")
        finally:
            plt.close('all')

    def _plot_timestamp_distribution(self):
        """绘制时间戳分布图"""
        print("_plot_timestamp_distribution")

        plt.figure(figsize=(12, 6))
        sns.histplot(self.df['timestamps'], bins=50, kde=True)
        plt.title(f'Spike Timestamps Distribution - {self.dataset_name}')
        plt.xlabel('Time (ms)')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.2)
        # plt.show()
        plt.savefig(os.path.join(self.output_dir, f"hist_{self.dataset_name}.png"))
        plt.close('all')

    def _plot_firing_rates(self):
        """绘制放电频率散点图：每个点代表一个神经元的平均放电率。"""
        print("_plot_firing_rates")

        plt.figure(figsize=(12, 6))
        plt.scatter(self.average_firing_rates.index, self.average_firing_rates.values, alpha=0.5)
        plt.title(f'Average Firing Rates per Neuron - {self.dataset_name}')
        plt.xlabel('Neuron/Node ID')
        plt.ylabel('Firing Rate (Hz)')
        plt.grid(True)
        # plt.show()
        plt.savefig(os.path.join(self.output_dir, f"rates_{self.dataset_name}.png"))
        plt.close('all')

    def _plot_firing_rate_distribution(self):
        """绘制放电频率分布箱线图:展示所有神经元放电率的分布情况。"""
        print("_plot_firing_rate_distribution")

        plt.figure(figsize=(8, 6))
        sns.boxplot(y=self.average_firing_rates)
        plt.title(f'Firing Rate Distribution - {self.dataset_name}')
        plt.ylabel('Firing Rate (Hz)')
        plt.grid(True, alpha=0.2)
        # plt.show()
        plt.savefig(os.path.join(self.output_dir, f"rates_distribution_{self.dataset_name}.png"))
        plt.close('all')


    def print_summary(self):
        """打印分析结果摘要"""
        print("print_summary")

        print(f"\n===== Analysis Summary for {self.dataset_name} =====")
        print(f"Total spikes: {self.results['total_spikes']}")
        print(f"Number of neurons: {self.results['num_neurons']}")
        print(f"Average spikes per neuron: {self.results['average_spikes_per_neuron']:.2f}")
        print(f"Recording duration: {self.results['total_time_seconds']:.2f} seconds")
        print(f"Average firing rate: {self.results['average_firing_rate']:.2f} Hz")


def analyze_all_datasets(file_paths):
    """分析所有数据集"""
    all_results = {}

    for file_path in file_paths:
        analyzer = SpikeAnalyzer(file_path)
        results = analyzer.analyze()
        analyzer.print_summary()
        all_results[analyzer.dataset_name] = results

    return all_results


if __name__ == "__main__":
    try:
        # 设置数据文件路径
        data_dir = r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\4.Data_files\point spikes files'
        file_names = [
            'spike_data_ei_EFC.csv',
            'spike_data_ei_MC.csv',
            'spike_data_ei_SS.csv',
            'spike_data_ei_VIS.csv'
        ]
        file_paths = [os.path.join(data_dir, fname) for fname in file_names]

        # 检查文件是否存在
        valid_paths = []
        for path in file_paths:
            if os.path.exists(path):
                valid_paths.append(path)
            else:
                print(f"Warning: File not found - {path}")

        if valid_paths:
            # 分析所有数据集
            final_results = analyze_all_datasets(valid_paths)

            # 可选：保存结果到文件
            results_df = pd.DataFrame(final_results).T
            results_df.to_csv(os.path.join(data_dir, 'analysis_summary.csv'))
            print("\nAnalysis summary saved to analysis_summary.csv")
        else:
            print("Error: No valid data files found")
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("按Enter键退出...")   # 防止窗口闪退



