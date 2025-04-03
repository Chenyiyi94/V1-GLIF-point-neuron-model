# load data
df = pd.read_csv(r'C:\Users\ChenYi\Desktop\V1_model\V1point Project\3.Spikes Visualization\spike_data_ei_efc.csv', sep=r'\s+', header=0)
print(df.head(5))

# define color
color_map = {'e': 'red', 'i': 'blue'}
colors = df['ei'].map(color_map)

# scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(x=df['timestamps'], y=df['node_ids'], c=colors, s=2, alpha=0.3, edgecolors='none')

plt.title('Spike Timestamps vs Node IDs', fontsize=14)
plt.xlabel('Timestamps (ms)', fontsize=12)
plt.ylabel('Node IDs', fontsize=12)
plt.show()


# calculate the average firing frequency of each neuron
spike_counts = df['node_ids'].value_counts()   # value_counts用于统计每个node id在列中出现的次数
total_time = df['timestamps'].max() - df['timestamps'].min()  # time stamps的单位是ms
total_time = total_time / 1000    # ms -> s
average_firing_rates = spike_counts / total_time   # Hz 每秒发放次数

print("Spike counts per neuron:\n", spike_counts)
print("Total time in seconds:", total_time)
print("Average firing rates per neuron (Hz):\n", average_firing_rates)


# 计算平均放电次数
total_spikes = len(df)
num_neurons = df['node_ids'].nunique()
average_spikes_per_neuron = total_spikes / num_neurons

print("Total number of spikes:", total_spikes)
print("Number of unique neurons:", num_neurons)
print("Average spikes per neuron:", average_spikes_per_neuron)


# histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['timestamps'], bins=50, kde=True)
plt.title('Spike Timestamps Distribution')
plt.xlabel('Time (ms)')
plt.ylabel('Frequency')
plt.show()

# 发放频率图
plt.figure(figsize=(10, 6))
plt.scatter(average_firing_rates.index, average_firing_rates.values, alpha=0.5)
print(type(average_firing_rates.index))
print(type(average_firing_rates.values))
plt.title('Average Firing Rates per Neuron')
plt.xlabel('Neuron/Node ID')
plt.ylabel('Firing Rate (Hz)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(y=average_firing_rates)
plt.title('Distribution of Firing Rates')
plt.ylabel('Firing Rate (Hz)')
plt.show()


'''
# 发放模式图（选择一个神经元）
neuron_id = 125771  # 选择一个神经元ID
neuron_spikes = spike_data[spike_data['node_ids'] == neuron_id]['timestamps']
plt.figure(figsize=(10, 6))
plt.eventplot(neuron_spikes, orientation='horizontal', colors='b')
plt.title(f'Spike Train for Neuron {neuron_id}')
plt.xlabel('Time (ms)')
plt.ylabel('Spikes')
plt.show()



# 交叉相关分析（选择两个神经元）
neuron1_spikes = spike_data[spike_data['node_ids'] == 125771]['timestamps']
neuron2_spikes = spike_data[spike_data['node_ids'] == 120162]['timestamps']
cross_corr = correlate(neuron1_spikes, neuron2_spikes, mode='full')
plt.figure(figsize=(10, 6))
plt.plot(cross_corr)
plt.title('Cross-Correlation between Neuron 125771 and Neuron 120162')
plt.xlabel('Lag')
plt.ylabel('Correlation')
plt.show()


# 保存发放频率数据
average_firing_rates.to_csv('average_firing_rates.csv')

# 保存发放时间直方图
plt.savefig('spike_timestamps_distribution.png')

'''