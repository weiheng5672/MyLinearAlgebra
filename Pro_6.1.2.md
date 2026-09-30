
$$
A = \begin{bmatrix}
1 & 4  \\
2 & 3 
\end{bmatrix}
$$

$$
A+I = \begin{bmatrix}
2 & 4  \\
2 & 4 
\end{bmatrix}
$$

求這兩個矩陣的特徵值與特徵向量

對於 A
$λ_1 + λ_2$ = 4
$λ_1λ_2$ = 3-8 = -5
$λ_1= 5$
$λ_2 = -1$ 

對於 $λ_1= 5$

$$
\begin{bmatrix}
-4 & 4  \\
2 & -2 
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
2 & 4  \\
2 & 4 
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
A+I = \begin{bmatrix}
2 & 4  \\
2 & 4 
\end{bmatrix}
$$


$λ_1 + λ_2$ = 6
$λ_1λ_2$ = 0
$λ_1= 6$
$λ_2 = 0$ 

對於 $λ_1= 6$

$$
\begin{bmatrix}
-4 & 4  \\
2 & -2 
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

對於 $λ_2= 0$

$$
\begin{bmatrix}
2 & 4  \\
2 & 4 
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
A+I 的 特徵值 是 A的特徵值 +1

其實可以不用算 A+I

若 (λ,x) 是A的特徵對
Ax = λx

代表
(A+I)x = Ax+x = λx+x = (λ+1)x

則 (λ+1,x) 是A+I的特徵對

