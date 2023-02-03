import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from scipy.stats import uniform
from scipy.stats import chi2
from scipy.stats import gamma
from scipy.stats import beta
import seaborn as sns

def T_K(r, n):
    K = n ** 2
    left, right = 0, 1
    samples = []
    for i in range(K):
        sample = np.random.uniform(left, right, n)
        samples.append(sample)

    for i in range(K):
        samples[i] = sorted(samples[i])

    r_order_statistics = []
    for i in range(K):
        r_order_statistics.append(samples[i][r - 1])

    F_x = []
    x = sorted(r_order_statistics)

    for i in range(len(x)):
        F_x.append(i / K)

    T_k = 0
    for i in range(len(x) - 1):
        T_k = max(T_k, abs(F_x[i] - beta.cdf(x[i], r, n + 1 - r)), abs(F_x[i + 1] - beta.cdf(x[i], r, n + 1 - r)))
    T_k = max(T_k, abs(F_x[len(x) - 1] - beta.cdf(x[len(x) - 1], r, n + 1 - r)))

    return T_k


def T_K_list(r, N):
    T_k = []
    num_of_mesures = 1
    for n in N:
        T = 0
        for i in range(num_of_mesures):
            T += T_K(r, n)
        T_k.append(T / num_of_mesures)
    return T_k


N = np.arange(50, 200, 100)
fig, axes = plt.subplots(2, 2, figsize=(20, 15))

list1 = T_K_list(40, N)
axes[0, 0].plot(N, list)
axes[0, 0].plot(N, list, '.', color="red")
axes[0, 0].set_title("r = 50")
axes[0, 0].set_xlabel("n")
axes[0, 0].set_ylabel('$T_K$')
axes[0, 0].grid()

# axes[0, 1].plot(N, T_K_list(100, N))
# axes[0, 1].plot(N, T_K_list(100, N), '.', color="red")
# axes[0, 1].set_title("r = 100")
# axes[0, 1].set_xlabel("n")
# axes[0, 1].set_ylabel('$T_K$')
# axes[0, 1].grid()
#
# axes[1, 0].plot(N, T_K_list(150, N))
# axes[1, 0].plot(N, T_K_list(150, N), '.', color="red")
# axes[1, 0].set_title("r = 150")
# axes[1, 0].set_xlabel("n")
# axes[1, 0].set_ylabel('$T_K$')
# axes[1, 0].grid()
#
# axes[1, 1].plot(N, T_K_list(200, N))
# axes[1, 1].plot(N, T_K_list(200, N), '.', color="red")
# axes[1, 1].set_title("r = 200")
# axes[1, 1].set_xlabel("n")
# axes[1, 1].set_ylabel('$T_K$')
# axes[1, 1].grid()