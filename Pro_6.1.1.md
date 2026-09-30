
$$
A = \begin{bmatrix}
.8 & .3  \\
.2 & .7 
\end{bmatrix}
$$

$$
A^{2} = \begin{bmatrix}
.70 & .45  \\
.30 & .55 
\end{bmatrix}
$$

$$
A^{\infty} = \begin{bmatrix}
.6 & .6  \\
.4 & .4 
\end{bmatrix}
$$

求這些矩陣的特徵值，所有的次方都有相同的特徵向量。 
(a) 從 A 說明 row交換 或如何得到不同的特徵值。 
(b) 為什麼零特徵值在消去步驟下不會改變?

---

特徵值 與 特徵向量
對於2*2矩陣
我們利用 
$λ_1 + λ_2$ = 跡數
$λ_1λ_2$ = 行列式

---

對於 A
$λ_1 + λ_2$ = 1.5
$λ_1λ_2$ = 0.56-0.06 = 0.5
$λ_1= 1$
$λ_2 = 0.5$ 

對於 $λ_1= 1$

$$
\begin{bmatrix}
-.2 & .3  \\
.2 & -.3 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

對於 $λ_2= 0.5$

$$
\begin{bmatrix}
.3 & .3  \\
.2 & .2 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
1
\end{bmatrix}
$$

---

對於

$$
A^{2} = \begin{bmatrix}
.70 & .45  \\
.30 & .55 
\end{bmatrix}
$$

$λ_1 + λ_2$ = 1.25
$λ_1λ_2$ = 0.385-0.135 = 0.25
$λ_1= 1$
$λ_2 = 0.25$ 

對於 $λ_1= 1$

$$
\begin{bmatrix}
-.30 & .45  \\
.30 & -.45 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

對於 $λ_2= 0.25$

$$
\begin{bmatrix}
.45 & .45  \\
.30 & .30 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
1
\end{bmatrix}
$$

---

對於

$$
A^{\infty} = \begin{bmatrix}
.6 & .6  \\
.4 & .4 
\end{bmatrix}
$$

$λ_1 + λ_2$ = 1
$λ_1λ_2$ = 0
$λ_1= 1$
$λ_2 = 0$ 

對於 $λ_1= 1$

$$
\begin{bmatrix}
-.4 & .6  \\
.4 & -.6 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

對於 $λ_2= 0$

$$
\begin{bmatrix}
.6 & .6  \\
.4 & .4 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
1
\end{bmatrix}
$$

---


(a)
令 B 是 兩個row 互換

$$
B = \begin{bmatrix}
.2 & .7   \\
.8 & .3
\end{bmatrix}
$$

$λ_1 + λ_2$ = 0.5
$λ_1λ_2$ = 0.06-0.56 = -0.5

好 其實到這邊就可以 解釋 為何兩行互換 特徵值會變
不用繼續算下去了

(b)


零特徵值 $\lambda = 0$ 的定義是：存在非零向量 $\mathbf{x}$ 使得 $A\mathbf{x} = 0\mathbf{x} = \mathbf{0}$

這意味著，$\lambda = 0$ 對應的特徵向量空間，就是矩陣 $A$ 的零空間

當我們對矩陣 $A$ 進行基本列運算（包含列交換、列加減、列倍乘）得到矩陣 $R$ 時，這個過程相當於左乘一個可逆矩陣 $E$，即 $R = EA$。

求解零空間時，我們解的是齊次方程組：

$$
A\mathbf{x} = \mathbf{0}
$$

兩邊左乘 $E$：

$$
E(A\mathbf{x}) = E\mathbf{0} \implies (EA)\mathbf{x} = \mathbf{0} \implies R\mathbf{x} = \mathbf{0}
$$

矩陣經由消去法後，$\lambda = 0$ 依然是新矩陣的特徵值

