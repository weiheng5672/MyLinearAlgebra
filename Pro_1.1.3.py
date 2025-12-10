import numpy as np
import matplotlib.pyplot as plt

# 已知條件
v_plus_w = np.array([5, 1])
v_minus_w = np.array([1, 5])

# 計算 v 和 w
v = (v_plus_w + v_minus_w) / 2
w = (v_plus_w - v_minus_w) / 2

print("v =", v)
print("w =", w)

# 繪圖
fig, ax = plt.subplots()
ax.set_aspect('equal')

# 繪製向量
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
ax.quiver(0, 0, v_plus_w[0], v_plus_w[1], angles='xy', scale_units='xy', scale=1, color='g', label='v + w')
ax.quiver(0, 0, v_minus_w[0], v_minus_w[1], angles='xy', scale_units='xy', scale=1, color='purple', label='v - w')

# 設定範圍與刻度
ax.set_xlim(-1, 6)
ax.set_ylim(-3, 5)
ax.set_xticks(np.arange(-1, 7, 1))
ax.set_yticks(np.arange(-3, 6, 1))

ax.grid(True)
ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vectors v, w, v+w, v-w')
plt.show()
