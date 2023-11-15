import random as rand
import matplotlib.pyplot as pyplot
import math
import scipy.stats as scipy_stats

def build_hist(data):
    figure = pyplot.figure()
    ax = figure.add_subplot(111)
    ax.hist(data, bins=20, edgecolor='black')
    pyplot.show()

def get_mean(data):
    return sum(data) / len(data)

def get_variance(data):
    mean = get_mean(data)
    variance = 0
    for num in data:
        variance += (num - mean) ** 2
    variance = (1 / (len(data) - 1)) * variance
    return variance

def exp_theoretical_probability(x1, x2, lambd):
    return math.e ** (-lambd * x1) - math.e ** (-lambd * x2)

def uniform_theoretical_probability(x1, x2, a, b):
    return (1 / (b - a)) * (x2 - x1)

def chi_square(num_occurrences, theoretical_probabilities):
    chi_squared = 0
    total_nums_count = sum(num_occurrences)
    for i in range(len(num_occurrences)):
        theoretical_num_occurrence = total_nums_count * theoretical_probabilities[i]
        chi_squared += (num_occurrences[i] - theoretical_num_occurrence) ** 2 / theoretical_num_occurrence

    return chi_squared

def task1(lambd):
    num_list = []
    for i in range(10000):
        uniform_random_num = rand.uniform(0.0, 1.0)
        num_list.append((-1 / lambd) * math.log(uniform_random_num))

    mean = get_mean(num_list)
    variance = get_variance(num_list)

    print(f'Lambda value: {lambd}')
    print(' ')
    print(f'Mean: {mean}')
    print(f'Variance: {variance}')

    chi_squared_lambd = 1 / mean

    k = 20
    maximum, minimum = max(num_list), min(num_list)
    interval_length = (maximum - minimum) / k

    numb_occurrence = [0] * k
    theoretical_probabilities = [0] * k

    # calculate intervals
    for num in num_list:
        if num != maximum:
            if (num - minimum) % interval_length == 0.0:
                numb_occurrence[math.floor((num - minimum) / interval_length) - 1] += 1
            else:
                numb_occurrence[math.floor((num - minimum) / interval_length)] += 1
    numb_occurrence[k - 1] += 1

    # calculate theoretical probabilities
    for i in range(0, k):
        theoretical_probabilities[i] = exp_theoretical_probability(minimum + i * interval_length,
                                                                   minimum + (i + 1) * interval_length,
                                                                   chi_squared_lambd)

    # calculate chi squared
    significance_level = 1 - 0.05
    degree_freedom = k - 1 - 1
    chi_squared = chi_square(numb_occurrence, theoretical_probabilities)
    print('Chi squared:', chi_squared)
    print(f'Chi squared critical value({significance_level}, {degree_freedom}):',
          f'{scipy_stats.chi2.ppf(significance_level, degree_freedom)}')

    # build histogram
    build_hist(num_list)

def task2(a, sigma):
    num_list = []
    for i in range(10000):
        uniform_sum = 0
        for j in range(12):
            uniform_sum += rand.uniform(0.0, 1.0)
        uniform_sum -= 6
        num_list.append(sigma * uniform_sum + a)

    mu = mean = get_mean(num_list)
    variance = get_variance(num_list)
    sigma = math.sqrt(variance)

    print(' ')
    print(f'Variance: {variance}')
    print(f'Mean: {mean}')
    print(f'Variance: {variance}')

    k = 20
    maximum, minimum = max(num_list), min(num_list)
    interval_length = (maximum - minimum) / k

    num_occurrences = [0] * k
    theoretical_probabilities = [0] * k

    # calculate intervals
    for num in num_list:
        if num != maximum:
            if (num - minimum) % interval_length == 0.0:
                num_occurrences[math.floor((num - minimum) / interval_length) - 1] += 1
            else:
                num_occurrences[math.floor((num - minimum) / interval_length)] += 1
    num_occurrences[k - 1] += 1

    # calculate theoretical probabilities
    for i in range(0, k):
        theoretical_probabilities[i] = scipy_stats.norm.cdf(minimum + (i + 1) * interval_length, mu, sigma) - \
            scipy_stats.norm.cdf(minimum + i * interval_length, mu, sigma)

    # calculate chi squared
    significance_level = 1 - 0.05
    degree_freedom = k - 1 - 2
    chi_squared = chi_square(num_occurrences, theoretical_probabilities)
    print('Chi squared:', chi_squared)
    print(f'Chi squared critical value({significance_level}, {degree_freedom}):',
          f'{scipy_stats.chi2.ppf(significance_level, degree_freedom)}')

    build_hist(num_list)

def task3(a, c):
    z = 15
    num_list = []
    for i in range(10000):
        z = (a * z) % c
        num_list.append(z / c)

    mean = get_mean(num_list)
    variance = get_variance(num_list)

    print(' ')
    print(f'Mean: {mean}')
    print(f'Variance: {variance}')

    k = 20
    maximum, minimum = max(num_list), min(num_list)
    interval_length = (maximum - minimum) / k

    num_occurrences = [0] * k
    theoretical_probabilities = [0] * k

    # calculate intervals
    for num in num_list:
        if num != maximum:
            if (num - minimum) % interval_length == 0.0:
                num_occurrences[math.floor((num - minimum) / interval_length) - 1] += 1
            else:
                num_occurrences[math.floor((num - minimum) / interval_length)] += 1
    num_occurrences[k - 1] += 1

    # calculate theoretical probabilities
    for i in range(0, k):
        theoretical_probabilities[i] = uniform_theoretical_probability(minimum + i * interval_length,
                                                                       minimum + (i + 1) * interval_length,
                                                                       0, 1)

    # calculate chi squared
    significance_level = 1 - 0.05
    degree_freedom = k - 1 - 2
    chi_squared = chi_square(num_occurrences, theoretical_probabilities)
    print('Chi squared:', chi_squared)
    print(f'Chi squared critical value({significance_level}, {degree_freedom}):',
          f'{scipy_stats.chi2.ppf(significance_level, degree_freedom)}')

    build_hist(num_list)

# task1(5)
# task2(80, 70)
task3(5 ** 12, 2 ** 27)
