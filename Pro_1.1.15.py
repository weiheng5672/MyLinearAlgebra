import numpy as np
import matplotlib.pyplot as plt

# 向量
v = np.array([4, 1])
w = np.array([1, 4])
v_half_plus_w_half = (v + w)/2
three_v_over_4_plus_w_over_4 = 3*v/4 + w/4
v_over_4_plus_w_over_4 = v/4 + w/4
v_plus_w = v + w

# 建立繪圖
fig, ax = plt.subplots()
ax.set_aspect('equal')  # 保持比例尺一致

# 使用 quiver 繪製向量
# quiver(x起點, y起點, x方向分量, y方向分量, ...)
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')

# 使用 scatter 繪製 v+w 和 v-w 的點
ax.scatter(v_half_plus_w_half[0], v_half_plus_w_half[1], s=30, color='g', marker='o', label='v/2 + w/2')
ax.scatter(three_v_over_4_plus_w_over_4[0], three_v_over_4_plus_w_over_4[1], s=30, color='purple', marker='o', label='3v/4 + w/4')
ax.scatter(v_over_4_plus_w_over_4[0], v_over_4_plus_w_over_4[1], s=30, color='y', marker='o', label='v/4 + w/4')
ax.scatter(v_plus_w[0], v_plus_w[1], s=30, color='r', marker='x', label='v + w')

# 設定座標範圍
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# 手動設定刻度
ax.set_xticks(np.arange(-10, 10, 1))  # x 軸每 1 單位
ax.set_yticks(np.arange(-10, 10, 1))  # y 軸每 1 單位

# 加上網格與圖例
ax.grid(True)
ax.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Vectors v, w, v+w, v-w')
plt.show()
