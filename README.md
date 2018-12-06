# 2018-Woongjin-Cooperation-Project

통계적 방법으로 K-means clustering을 활용해 10대 미만, 10대, 3.40대, 50대 이상 총 4개의 군집으로 clustering을 진행함

57명 및 2000명의 clustering결과에서 cluster0가 10대 미만, cluster1이 3.40대, cluster2가 10대, cluster3가 50대 이상인 것으로 추측

K-means clustering을 하는 과정에서 기준으로 사용한 zone들은 14개로, 다시 말해 feature들이 14개이므로 시각화에 어려움이 있음
-> PCA 알고리즘을 이용해 차원을 축소해 시각화
