import numpy as np
import arviz as az

clusters = 2
n_cluster = [200, 150]
n_total = sum(n_cluster)
means = [5, 0]
std_devs = [2, 2]
mix = np.random.normal(
    np.repeat(means, n_cluster),
    np.repeat(std_devs, n_cluster)
    )
az.plot_kde(np.array(mix))
