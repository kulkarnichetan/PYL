import numpy as np
from scipy import stats, integrate, optimize, signal, special

# 1. Generate normal distribution samples
samples = np.random.normal(loc=0, scale=1, size=1000)

# 2. Compute mean and standard deviation
mean = np.mean(samples)
std_dev = np.std(samples)

# 3. Perform a one-sample t-test
t_stat, p_val = stats.ttest_1samp(samples, popmean=0)

# 4. Perform a two-sample t-test
sample1 = np.random.normal(0, 1, 100)
sample2 = np.random.normal(0.5, 1, 100)
t2_stat, p2_val = stats.ttest_ind(sample1, sample2)

# 5. Compute Pearson correlation
corr, p_corr = stats.pearsonr(sample1, sample2)

# 6. Chi-square test for observed frequencies
observed = [10, 20, 30]
expected = [15, 15, 30]
chi2, chi_p = stats.chisquare(f_obs=observed, f_exp=expected)

# 7. Probability density function of a normal distribution
pdf_val = stats.norm.pdf(0)

# 8. Cumulative distribution function (CDF)
cdf_val = stats.norm.cdf(1.96)

# 9. Inverse CDF (percent-point function)
ppf_val = stats.norm.ppf(0.975)

# 10. Numerical integration of a function
result, error = integrate.quad(lambda x: x**2, 0, 1)

# 11. Double integral over a region
dbl_result, dbl_err = integrate.dblquad(lambda x, y: x*y, 0, 1, lambda x: 0, lambda x: 2)

# 12. Solve a simple equation (root finding)
root = optimize.root(lambda x: x**2 - 4, x0=1)
root.x

# 13. Minimize a function
min_result = optimize.minimize(lambda x: x**2 + 5*np.sin(x), x0=0)
min_result.x

# 14. Solve an ordinary differential equation (ODE)
def dydt(y, t): return -2 * y
t = np.linspace(0, 5, 100)
y0 = 1
ode_result = integrate.odeint(dydt, y0, t)

# 15. Find local peaks in data
data = np.array([1, 3, 7, 1, 2, 6, 0, 1])
peaks, _ = signal.find_peaks(data)

# 16. Convolve two signals
signal1 = np.array([1, 2, 3])
signal2 = np.array([0, 1, 0.5])
convolved = signal.convolve(signal1, signal2)

# 17. Fourier transform of a signal
fft_data = np.fft.fft(data)

# 18. Evaluate a special function (gamma function)
gamma_val = special.gamma(5)

# 19. Compute the factorial using special
factorial_val = special.factorial(5)

# 20. Bessel function of the first kind (useful in physics/eng)
bessel_val = special.jv(0, 2.5)
