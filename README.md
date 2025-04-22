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
### 代码、数据、结果放在哪里？

### 备注
1.连接权重或者连接强度的定义，可以根据具体的需求和场景进行修改，value值的计算也需根据情况修改。
2.是关注region还是single neuron based on your paper idea,关注哪些region也是based on your idea.




## step 2:用V1 point network 运行仿真
### 修改配置文件，定义网络的输入和权重文件

### 代码、数据、结果放在哪里？
### 备注
1.从Allen 实验室的website可以下载他们的网络的相关代码和资料。website is：https://portal.brain-map.org/explore/models/mv1-all-layers
2.我对他们的网络输出文件做了一个修改，在输出文件夹里添加一个weight文件，所以，输出文件应该有5个文件：log文件，
config文件，weight文件，spikes csv和spikes h5。
3.将spikes csv文件转化为txt文件，可以用作者的raster plot code绘制spike的结果图。

## step 3:分析仿真结果
### 如何对比不同region的结果
### raster plot
### metrics
### 代码、数据、结果放在哪里？
### 备注

## step 4:V1 biophysical network
### 怎么定义连接权重？
### 不同区域是哪些？
### 代码、数据、结果放在哪里？
### 备注
