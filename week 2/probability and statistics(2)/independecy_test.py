# import packages and functions
import numpy as np
from scipy.stats import chi2_contingency


# give the contigency table with observed counts
cats = np.array([[28, 12], [16, 24]])

# do the test for independence
print('\n\n', chi2_contingency(cats))


print(np.float64(0.01343346520577156))