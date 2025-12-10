import numpy as np
import matplotlib.pyplot as plt

# 向量
v = np.array([4, 1])
w = np.array([1, 4])
minus_v_plus_2_w = -v + 2*w
two_v_minus_w = 2*v - w

# 建立繪圖
fig, ax = plt.subplots()
ax.set_aspect('equal')  # 保持比例尺一致

# 使用 quiver 繪製向量
# quiver(x起點, y起點, x方向分量, y方向分量, ...)
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
ax.quiver(0, 0, -v[0], -v[1], angles='xy', scale_units='xy', scale=1, color='pink', label='-v')

# 使用 scatter 繪製點
ax.scatter(minus_v_plus_2_w[0], minus_v_plus_2_w[1], s=30, color='g', marker='o', label='-v + 2w')
ax.scatter(two_v_minus_w[0], two_v_minus_w[1], s=30, color='y', marker='o', label='2v - w')

# 方法 3：使用 numpy 的 polyfit 擬合直線
x_points = [minus_v_plus_2_w[0], two_v_minus_w[0]]
y_points = [minus_v_plus_2_w[1], two_v_minus_w[1]]

# 擬合一階多項式（直線）
coefficients = np.polyfit(x_points, y_points, 1)
poly_func = np.poly1d(coefficients)

# 生成延伸的 x 值
x_line = np.linspace(-10, 10, 100)
y_line = poly_func(x_line)

# 繪製延伸的直線
ax.plot(x_line, y_line, color='green', linestyle=':', linewidth=1.5,
        alpha=0.7, label='')

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
