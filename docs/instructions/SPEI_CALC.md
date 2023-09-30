# SPEI计算指南

## 构建差值序列

构建单个区块内给定时间尺度下降雨量$\{P_i\}^n_{i=1}$与潜在蒸散发$\{PET_i\}^n_{i=1}$的差值序列$\{D_i\}^n_{i=1}$，

$$\{D_i\}^n_{i=1}= \{P_i\}^n_{i=1}-\{PET_i\}^n_{i=1}$$

这个序列下文记作$D_i$，使用**genextreme**分布对其进行拟合。该分布下文简称**GEV**分布。

## 拟合参数

使用线性矩法对$D_i$的分布进行参数估计。

### 拟合方法

GEV分布的CDF为

$$
\begin{equation}
F(x)=\left\{
    \begin{aligned}
    \mathrm{exp}(-(1-\kappa\frac{x-\xi}{\alpha})^{1/\kappa}),\kappa\not= 0 \\
    \mathrm{exp}(\mathrm{exp}(-\frac{x-\xi}{\alpha})),\kappa = 0
    \end{aligned}
\right.
\end{equation}
$$

其中$\alpha,\xi,\kappa$为参数。

记L-mean，L-scale，L-skewness分别为$\lambda_1,\lambda_2,\tau_3$，GEV分布的三个参数可以用如下公式近似估计：

$$
\begin{equation}
\kappa =\left\{
    \begin{aligned}
    &0.488138(\tau_3)^{1.70839}-1.7631(\tau_3)^{0.981824}+0.285706, 0.01\le\tau_3\le 0.5 \\
    &0.483706(\tau_3)^{1.679096}-1.73786(\tau_3)^{1.008948}+0.255108, 0.5\le\tau_3\le 0.95
    \end{aligned}
\right.
\end{equation}
$$
$$
\begin{equation}
\frac{\alpha}{\lambda_2}=\left\{
    \begin{aligned}
    &1.023602813(\tau_3)^{1.8850974}-2.95087636(\tau_3)^{1.195591244}+1.7599614982, -0.5\le \kappa \le 0.3 \\
    &1.5954866(\tau_3)^{1.5816175}-3.886135(\tau_3)^{0.89522}+2.310643, \kappa > 0.3
    \end{aligned}
\right.
\end{equation}
$$
$$
\begin{equation}
\frac{\xi-\lambda_1}{\lambda_2}=-0.0937(\tau_3)^4-0.2198(\tau_3)^3+1.407(\tau_3)^2-1.4825(\tau_3)-0.6205, 0.01\le\tau_3\le 0.95
\end{equation}
$$

将$D_i$带入GEV分布的CDF，得到相应的概率序列$P_i$。

### 正态化

将求得的概率带入标准正态分布CDF的反函数，得到SPEI：

$$ SPEI_i = \varPhi^{-1}(P_i) $$