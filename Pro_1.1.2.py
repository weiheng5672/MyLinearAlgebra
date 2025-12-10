import numpy as np
import matplotlib.pyplot as plt

# 向量
v = np.array([4, 1])
w = np.array([-2, 2])
v_plus_w = v + w
v_minus_w = v - w

# 建立繪圖
fig, ax = plt.subplots()
ax.set_aspect('equal')  # 保持比例尺一致

# 使用 quiver 繪製向量
# quiver(x起點, y起點, x方向分量, y方向分量, ...)
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
ax.quiver(0, 0, v_plus_w[0], v_plus_w[1], angles='xy', scale_units='xy', scale=1, color='g', label='v + w')
ax.quiver(0, 0, v_minus_w[0], v_minus_w[1], angles='xy', scale_units='xy', scale=1, color='purple', label='v - w')

# 設定座標範圍
ax.set_xlim(-4, 6)
ax.set_ylim(-2, 5)

# 手動設定刻度
ax.set_xticks(np.arange(-4, 7, 1))  # x 軸每 1 單位
ax.set_yticks(np.arange(-2, 6, 1))  # y 軸每 1 單位

# 加上網格與圖例
ax.grid(True)
ax.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Vectors v, w, v+w, v-w')
plt.show()
