# import packages and functions
import numpy as np
from scipy.stats import chi2_contingency


# give the contigency table with observed counts
Titanic = np.array([[122, 203], [167, 118], [528, 178], [673, 212]])

# do the test for independence
print('\n\n', chi2_contingency(Titanic))




