# IsolationForest
IsolationForest wiht Sk-learn

算法起源于08年的一篇论文《Isolation Forest》，这论文由澳大利亚莫纳什大学的两位教授Fei Tony Liu, Kai Ming Ting(这两个名字看起来都像是华人)和
南京大学的周志华教授共同完成，而这三人在2011年又发表了《Isolation-based Anomaly Detection》，这两篇论文算是确定了这个算法的基础。

后来我发现Sk-learn 有这个算法包，就像尝试一下，如果可以不用造轮子，自然是最好的，过段时间再啃一啃包里的源码，窥探一下开源怎么写算法，不过最近工作来了
新指标，只能暂时延后。

网上自然也是搜集了很多资料，发现很多都只是展示现场给你造一个2维的随机数组 作为输入，看着就觉得很烦心，于是我就来做一个Iforest的实战项目
数据是采用两个月的北京移动的5列GPRS流量数据，对我而言5列都是特征，
具体原理：https://blog.csdn.net/LIYUAN123ZHOUHUI/article/details/51604692




构建树tree的 参数parameters
n_estimators是树的构建数，通常为100即可
n_jobs=2 为使用的核心处理器cpu 如果你填写-1 那么就可以 将全部cpu计算资源用来构建树
max_samples=lendata  最大采样数，Iforest 不建议过多采样，封顶建议为256 再多就有可能使树无法更好采集特征
max_features=5 最大特征数，如果你对特征不是很了解，我说个通俗的，那就是大多数情况有几列数据或几行就代表几个特征或几个-1个特征。
               更细的就是数据集描述这组数据的基本都可以叫做特征。
更多参数方法：http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.predict
 
Iso_anomaly_score 为异常分数  评分越低，则越是异常
Iso_predict 为粗暴的判断是否为异常，1是正常，-1是异常
threshold   阈值定义 也可以 根据实际情况手动添加也可以根据不同情况以公式表示，这里我设置默认为-0.1

最后来谈谈这个实现，大部分和官网上写的用法一样，其实我也就是拿来用。
还有就是我把异常分数数组和时间合为一个数组然后tolist，方便输出异常数据时还能查看是哪天的数据。

以上，转载转发请注明出处，谢谢。
