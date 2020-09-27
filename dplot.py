import numpy as np
import scipy.stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"] = (10, 6)
# plt.rcParams["font.size"] = 14

def binned_plot(x, y, n_bins=101, color="g", title='', *, axis):
    at_least_one_nan_t = (np.isnan(x) | np.isnan(y))
    x, y = x[~at_least_one_nan_t], y[~at_least_one_nan_t]

    y_mean_T, bin_edges_T, _ = scipy.stats.binned_statistic(x, y,  statistic="mean", bins=n_bins)
    bin_edges_T = 0.5 * (bin_edges_T[1:] + bin_edges_T[:-1])

    y_std_T  = scipy.stats.binned_statistic(x, y, statistic="std", bins=n_bins)[0]
    y_std_T /= np.sqrt(scipy.stats.binned_statistic(x, y, statistic="count", bins=n_bins)[0])

    clf = LinearRegression()
    clf.fit(x[:, None], y)

    # Plot lin reg
    axis.plot(bin_edges_T, clf.intercept_ + clf.coef_[0] * bin_edges_T, color=color)
    axis.errorbar(bin_edges_T, y_mean_T, y_std_T, fmt="o", color=color)
    # Plot distribution
    twin_axis = axis.twinx()
    twin_axis.hist(x, bins=n_bins, histtype="step", color=color,
                   normed=True, log=True)
    twin_axis.set_ylabel("pdf")

    axis.set_title(f"{title}\n{clf.coef_[0]:.3f} x + {clf.intercept_:.3f}, "
                   f"corr = {np.corrcoef(x, y)[0,1]:.3f}")
    axis.grid()
    return axis