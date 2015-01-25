# -*- coding: utf-8 -*-

import pylab

# -10から10まで0.1刻みの配列を作る(numpy.arange)
x = pylab.arange(-10.0, 10.0, 0.1)

# 関数numpy.sin:xの各要素にMath.sinを適用して配列オブジェクトを生成
y1 = pylab.sin(x)
# 関数numpy.cos:xの各要素にMath.cosを適用して配列オブジェクトを生成
y2 = pylab.cos(x)

# x,yを描画
pylab.plot(x,y1, label='sin(x)')
pylab.plot(x,y2, label='cos(x)')

# Add labels
pylab.title('sinx and cosx')
pylab.xlabel('x')
pylab.ylabel('y')

# 凡例
pylab.legend()

# 描画
pylab.show()
