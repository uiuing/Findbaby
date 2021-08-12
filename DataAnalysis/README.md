# NAME: DataAnalysis
# BY：uiu
# ©️：uiuing.com
# time： 2021-05-12
---------------------------------------------------------
## 编程语言：Python
## 说明：该模块最终为Jar包，运行于HADOOP——MapReduce框架
## 功能：对走失儿童的成功案例进行 清洗、聚合、以及编写预测模型
## 说明：通过源于宝贝回家网站的万余条寻亲成功案例作为样本集，通过分类特征提取对样本数据进行归类，采用机器学习有监督学习分类--逻辑回归算法的底层基本逻辑，计算出预测模型数据

## 文件说明：
> 文件
    Training_set : 训练集
    part-00000 :  训练结果

> 文件夹
    Statistical_Analysis : Mapreduce数据归类程序
    Probabilistic_Analysis : Mapreduce概率计算程序
    Data_Stored_To_Cloud : 将结果数据集存储于Mysql中，供给DataVisualization模块调用
    Verification : 准确率计算