
$$
A = \begin{bmatrix}
0 & 2  \\
1 & 1 
\end{bmatrix}
$$

$$
A^{-1} = \begin{bmatrix}
-1/2 & 1  \\
1/2 & 0 
\end{bmatrix}
$$

求這兩個矩陣的特徵值與特徵向量

對於 A

$$
\begin{vmatrix}
-λ & 2 \\
1 & 1-λ
\end{vmatrix} =0
$$

$-λ(1-λ)-2 = 0$

$-λ+λ^2-2 = 0$

$(λ-2)(λ+1) = 0$

$λ_1 = 2$
$λ_2 = -1$

$λ_1 + λ_2 = 1$ 等於A的跡數 

$λ_1λ_2 = -2$ 等於A的行列式


對於 $λ_1= 2$

$$
\begin{bmatrix}
-2 & 2  \\
1 & -1 
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
1 \\
1
\end{bmatrix}
$$

對於 $λ_2= -1$

$$
\begin{bmatrix}
1 & 2  \\
1 & 2 
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
-2 \\
1
\end{bmatrix}
$$

---

對於

$$
A^{-1} = \begin{bmatrix}
-1/2 & 1  \\
1/2 & 0 
\end{bmatrix}
$$

$$
\begin{vmatrix}
-1/2-λ & 1 \\
1/2 & -λ
\end{vmatrix} =0
$$

$-λ(-1/2-λ)-1/2=0$

$1/2λ+λ^2-1/2=0$

$(λ+1)(λ-1/2)=0$

$λ_1 = 1/2$
$λ_2 = -1$

$λ_1 + λ_2 = -1/2$ 等於 $A^{-1}$ 的跡數 

$λ_1λ_2 = -1/2$ 等於 $A^{-1}$ 的行列式

對於 $λ_1= 1/2$

$$
\begin{bmatrix}
-1 & 1  \\
1/2 & -1/2 
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
1 \\
1
\end{bmatrix}
$$

對於 $λ_2= -1$

$$
\begin{bmatrix}
1/2 & 1  \\
1/2 & 1 
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
-2 \\
1
\end{bmatrix}
$$


---

可以看出 兩者特徵向量一樣 
$A^{-1}$ 的 特徵值 是 A的特徵值 的倒數

其實可以不用算 $A^{-1}$

若 (λ,x) 是A的特徵對
Ax = λx

代表

$A^{-1}Ax = λA^{-1}x$

$Ix = λA^{-1}x$

$A^{-1}x = (1/λ)x$

則 $(1/λ,x)$ 是$A^{-1}$的特徵對

