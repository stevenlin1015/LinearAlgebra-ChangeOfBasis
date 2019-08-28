#
# ChangeOfBasis.py
# Created by Steven on 2019/08/22
# Copyright © 2019 Steven. All rights reserved.
#

import numpy as np

#
# R^2 中的向量範例"延伸" : 利用標準基底的座標向量(已知)回推非標準基底的座標向量(未知)
# 請參考線性代數-第二版 (謝朝和著) 第4.8節 P.167 例題2
#

#非標準基底B = {v1, v2} = {(1, 0), (1, 2)}
v = np.array([[1, 1], 
              [0, 2]])
#標準基底B'下之座標向量standardBasisOfVectorX = (7, 4)
standardBasisOfVectorX = np.array([7, 4])
#標準基底B' = {u1, u2} = {(1, 0), (0, 1)}
u = np.array([[1, 0], 
              [0, 1]])

#求標準基底B'中standardBasisOfVectorX的座標向量在非標準基底B下之座標向量x
x = np.linalg.inv(v).dot(standardBasisOfVectorX)
print("Sol. of ex.2 : " , x)


#
# R^2 中的向量範例"延伸" : 利用標準基底的座標向量(已知)回推非標準基底的座標向量(未知)
# 請參考線性代數-第二版 (謝朝和著) 第4.8節 P.167 例題3
#

#標準基底B = {e1, e2} = {(1, 0), (0, 1)}
e = np.array([[1, 0], 
              [0, 1]])
#非標準基底B下之座標向量standardBasisOfVectorX = (3, 1)
standardBasisOfVectorX = np.array([2, 4])
#非標準基底B' = {u1, u2} = {(1, 1), (-1, 1)}
u = np.array([[1, -1], 
               [1, 1]])


#求標準基底B中standardBasisOfVectorX的座標向量在非標準基底B下之座標向量x
x = np.linalg.inv(u).dot(standardBasisOfVectorX)
print("Sol. of ex.3 : " , x)

