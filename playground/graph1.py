# -*- coding: utf-8 -*-

import pylab

# -10から10まで0.1刻みの配列を作る(numpy.arange)
x = pylab.arange(-10.0, 10.0, 0.1)

# 関数numpy.sin:xの各要素にMath.sinを適用して配列オブジェクトを生成
y = pylab.sin(x)

# x,yを描画
pylab.plot(x,y)

# 描画
pylab.show()
