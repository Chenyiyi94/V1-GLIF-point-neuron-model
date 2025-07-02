# ------------------------------English Version ------------------------
# V1 Models
Based on the Allen Institute's paper "Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex", 
we aim to reproduce and modify their work.

## Research Objective
To develop a data-driven model of the primary visual cortex (V1) based on extensive experimental data. 
By providing different background (bkg) inputs and LGN inputs, we observe the model's spike outputs to study the running features of cortical circuits. 
More specifically, we define the network's connection weights by calculating the connection strengths between different neurons/regions.


## Step 1: Calculating Connection Weights Between Regions

### How to Define Connection Weights?
For a neuron whose soma is located in the source region, if part of its axon and boutons extend into the goal region, 
we calculate the number of axons and boutons in the goal region. 
A weighted value is then computed to represent the connection strength between the source and goal regions.

### Which Regions Are Considered?
We currently focus on four major regions:
1.Visual Cortical Areas (VIS): (All subregions within VIS)
2.Sensory Cortical Areas (SS): (Includes both SSp and SSs)
3.Executive Function Cortical Areas (EFC): (AId, AIp, AIv, MOp, MOs, ORB, PL)
4.Memory Cortical Areas (MC): (PERI, RSP, TEa)

### Where Are the Code, Data, and Results Stored?
Under the project directory: 0.Weight_calculate/

### Notes
1.The definition of connection weights/strengths can be adjusted based on specific research needs. 
The calculation method for the weighted value can also be modified.
2.Whether to focus on regions or single neurons depends on the research idea, as does the selection of regions.


## Step 2: Running Simulations with V1 Point Network

### Structure figure of the V1 Point Model


### Modifying Configuration Files to Define Network Inputs and Weights
1.Modify bkg_inputs/ to adjust background (BKG) inputs.
2.Modify lgn_stimulus/ to adjust LGN inputs.
3.Modify v1_v1_edge_types.csv in network_dynsyns/ to adjust connection weights.

### Where Are the Code, Data, and Results Stored about V1 point model ?
1.Under the project directory: 1-2/ 
2.Primarily used for running simulations on the server via command line in cmd, then copying results for further processing.
3.command line like "sbatch xxxx.sh".

### Notes
1.The original network code and resources from the Allen Institute can be downloaded from: https://portal.brain-map.org/explore/models/mv1-all-layers.
2.We modified their output files to include a weight file, so the output now consists of 5 files/parts:Log file , Config file , Weight file , Spikes (CSV), Spikes (h5).
3.The spikes.csv file can be converted to txt format for visualization using the author's raster plot code.


## Step 3: Analyzing Simulation Results

### Example: How to Obtain Simulation Results for Full-Field Flash Input?
1.Download the spikes.trial_n file corresponding to Full-Field Flash from:V1 Network Models from the Allen Institute /simulations /lgn_stimulus /results.
2.Put the spikes.trial_n file in the lgn_stimulus/ folder on the cluster.
3.Modify the configuration file (e.g., config.dynsyns_EFC.json):Set $OUTPUT_DIR to control the output folder name. And, set input_file to specify the input file/type.
4.Submit the job using sbatch: run "python run_pointnet_EFC.py config.dynsyns_EFC.json".
5.Check the results in: v1_point/output_dynsyns_EFC/FullField_Flash/
6.Process spikes.csv into .txt format and use the author provided raster plot code to generate spike train visualizations.

### Comparing Results Across Different Regions
1.Use the author provided raster plot code to compare our results with those in the original paper.




# ------------------------------Chinese Version ------------------------

# V1 Models
根据Allen实验室的《Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex》
做一些复现和修改工作。
 
## 研究目的
基于大量实验数据，做一个数据驱动的初级视觉皮层的模型，通过给定不同的bkg输入和lgn输入，观察模型的spike输出，
以此来研究大脑皮层回路的运行特点。更具体地，我们是通过计算不同neuron/region之间的连接强度，来定义网络的连接权重。

## step 1:计算不同区域的连接权重
### 怎么定义连接权重？
一个nueron，如果它的soma落在source region，而它的一部分axon和bouton落在goal region里，则我们计算落在goal region里axon number和bouton number，
以某种加权方式计算出一个value，将这个value视为source region 和goal region的连接强度。

### 不同区域是哪些？
我们目前关注的是四个区域：
Visual cortical areas: VIS  (pool every region in VIS)
Sensory cortical areas: SS  (both SSp and SSs)
Executive Function cortical areas: EFC  (AId AIp AIv MOp MOs ORB  PL)
Memory cortical areas: MC   (PERI  RSP  TEa)

### 计算权重相关的代码、数据、结果放在哪里？
在这个项目下的0.Weight_calculate文件夹下面。

### 备注
1.连接权重或者连接强度的定义，可以根据具体的需求和场景进行修改，value值的计算也需根据情况修改。
2.是关注region还是single neuron based on your paper idea,关注哪些region也是based on your idea.




## step 2:用V1 point network 运行仿真
### V1 point model 的示意图

### 修改配置文件，定义网络的输入和权重文件
修改bkg_inputs文件夹可修改BKG模块的输入，修改lgn_stimulus文件夹可修改LGN模块的输入。
修改network_dynsyns文件夹的v1_v1_edge_types.csv文件，可修改网络的权重设置。

### V1 point network相关的代码、数据、结果放在哪里？
在这个项目下的1-2 文件夹下面，主要是用在服务器上用命令行执行仿真，然后把结果复制过来，进行后续处理。

### 备注
1.从Allen 实验室的website可以下载他们的网络的相关代码和资料。website is：https://portal.brain-map.org/explore/models/mv1-all-layers
2.我对他们的网络输出文件做了一个修改，在输出文件夹里添加一个weight文件，所以，输出文件应该有5个文件：log文件，
config文件，weight文件，spikes csv和spikes h5。
3.将spikes csv文件转化为txt文件，可以用作者的raster plot code绘制spike的结果图。

## step 3:分析仿真结果
### 举例：如何得到输入为 Full field Flash类型的仿真结果？
1.从V1 Network Models from the Allen Institute /simulations /lgn_stimulus /results 这个路径获取Full field flash类型
对应的spikes.trial_n的文件。
2.将对应的full field 文件放到集群上的lgn_stimulus文件夹里。
3.修改对应区域的配置文件，如config.dynsyns_EFC.json，修改$OUTPUT_DIR控制输出文件夹命名，修改input_file控制输入文件/类型。
4.用sbatch建立任务，运行“python run_pointnet_EFC.py config.dynsyns_EFC.json”。
5.查看v1_point/output_dynsyns_EFC/FullField_Flash文件夹，获取结果文件。
6.用python代码处理spikes.csv文件，转化为txt后，用已有raster plot 代码绘制结果图。

### 如何对比不同region的结果
用作者提供的代码绘图，主要是raster plot，可以将我们的结果和paper‘s plot 进行对比。

