# python3
# author Silence Lu
# version 4.2.3
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

if __name__ == '__main__':
    #get dataset ，
    dataset = pd.read_csv('GPRS_remix.csv', engine='python')
    dataset = dataset.fillna(0)
    X_col = pd.DataFrame(dataset, columns=[ 'GPRSdown','GPRSup','GPRS_Traffic','Mobile_Tra_flow','mobile_passenger_num'])
    X_col = X_col.values
    #print(X_col)
    #the code maybe useful in dataset ,not 1D array

    rs = np.random.RandomState(64)
    lendata = dataset.shape[0]
    ifmodel = IsolationForest(n_estimators=100, verbose=2,n_jobs=2, max_samples=lendata, random_state=rs,max_features=5)
    ifmodel.fit(X_col)
    Iso_anomaly_score = ifmodel.decision_function(X_col)
    Iso_predict = ifmodel.predict(X_col)

    #Iso_anomaly_score 异常分数  评分越低，则越是异常

    Iso_anomaly_score = np.column_stack((dataset['Date'],Iso_anomaly_score))
    Iso_predict = np.column_stack((dataset['Date'],Iso_predict))
    Iso_predict = Iso_predict.tolist()
    Iso_anomaly_score = Iso_anomaly_score.tolist()
    #print(Iso_date)

    #threshold 阈值定义 也可以 根据实际情况手动添加也可以根据不同情况以公式表示，这里我设置为-0.1
    threshold = -0.1
    print("隔离森林检测可能为异常数据：[日期,异常评分],评分越低越可能是异常数据")
    for i in Iso_anomaly_score:
           if i[1] < threshold:
                print(i)

