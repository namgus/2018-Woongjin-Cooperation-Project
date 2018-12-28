# 2018-Woongjin-Cooperation-Project

### 웅진플레이도시 워터파크 데이터 분석

</br>

- **목표**

 웅진플레이도시 워터파크를 방문하는 고객의 위치 데이터를 분석하여, 고객 특성을 구분하고, 고객에 맞는 맞춤형 서비스를 제안

</br>

- **상세계획**
1. 비콘(위치) 데이터를 이용해 고객의 동선 분석
2. 고객의 동선을 통해 고객 연령대 예측

=> 고객 맞춤형 서비스 아이디어 제안

</br>

## 고객 동선 분석
![image](https://user-images.githubusercontent.com/28288186/50400979-af774f00-07ce-11e9-84ee-ec45f6aadd72.png)


---
## 연령대 예측

- **User prediction**을 위한 통계적 방법으로 K-means clustering을 활용해 10대 미만, 10대, 3.40대, 50대 이상 총 4개의 군집으로 clustering을 진행함
-> 57명 및 2000명의 clustering결과에서 cluster0가 10대 미만, cluster1이 3.40대, cluster2가 10대, cluster3가 50대 이상인 것으로 추측

- K-means clustering을 하는 과정에서 기준으로 사용한 zone들은 14개로, 다시 말해 feature들이 14개이므로 시각화에 어려움이 있음
-> PCA 알고리즘을 이용해 차원을 축소해 시각화

---
### Visualization of K-means clustering

![default](https://user-images.githubusercontent.com/28288186/49593734-9b061a80-f9b7-11e8-85ba-0c3a2f8567c7.png)
![s](https://user-images.githubusercontent.com/28288186/49593772-ad805400-f9b7-11e8-90a2-c496c51871af.png)
 
                     2000명 데이터                                                57명 데이터 
