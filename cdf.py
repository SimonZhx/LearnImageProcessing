# ヒストグラムの累積分布関数（Cumulative Distribution Function、CDF）は、統計学や信号処理などで使用される概念です。
# ヒストグラムの各ビン（階級）に含まれるデータの累積を表す関数です。
# ヒストグラムは、データセット内の値の出現頻度をビン（階級）ごとに数えて表現します。一方、累積分布関数（CDF）は、ヒストグラムに基づいて各ビンの累積頻度を表します。
# CDFの計算手順は以下の通りです：
# ヒストグラムの最初のビンから順に、現在のビンまでの頻度を合計していきます。これにより、累積頻度が求められます。
# 各ビンに対して、そのビンまでの累積頻度を全体のデータ数で割り、0から1までの範囲に正規化します。これにより、CDFが求められます。
# CDFは、データの分布を理解するために使用されます。具体的には、CDFを使って以下の情報が得られます：
# 各データ値以下の割合：特定のデータ値以下のデータの割合（確率）を求めることができます。
# データのパーセンタイル：特定のパーセンタイルに対応するデータ値を求めることができます。
# データの範囲や分布の特性：CDFの形状や勾配を分析することで、データの範囲や分布の特性を把握することができます。
# 画像処理の文脈では、ヒストグラム平坦化（EqualizeHist）やCLAHE（Contrast Limited Adaptive Histogram Equalization）などの手法で、
# CDFが使用されます。CDFを利用して画像のピクセル値を変換することで、コントラストの改善やヒストグラムの均等化が行われます。

import numpy as np
import matplotlib.pyplot as plt

def compute_cdf(hist):
    cdf = np.cumsum(hist)
    cdf_normalized = cdf / (float)(cdf.max())
    return cdf_normalized

hist = np.array([10,15,8,20,12,5])

cdf = compute_cdf(hist)

plt.plot(cdf)
plt.xlabel('Pixel Value')
plt.ylabel('CDF')
plt.title('Cumlative Distribution Function (CDF)')
plt.show()

