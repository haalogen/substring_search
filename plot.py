import matplotlib.pyplot as plt

n = 1e6
bruteRes = [
    4.50611114502e-06,
    0.000823402404785,
    0.0210448980331,
    0.154466199875,
    0.527451992035,
    0.621789693832,
    0.701891088486,
    0.707935500145,
    0.709453701973,
    0.703685498238,
    0.703602409363 ]

rabinRes = [
    0.0389488935471,
    0.0399548053741,
    0.0573272943497,
    0.169061088562,
    0.4725481987,
    0.550091409683,
    0.62067129612,
    0.605745911598,
    0.626036000252,
    0.600534009933,
    0.592835211754 ]

m = [1, 5, 7, 9, 10, 11, 12, 15, 20, 40, 100]
plt.plot(m, bruteRes, marker='o', label='BruteForce')
plt.plot(m, rabinRes, marker='o', label='Rabin-Karp')
plt.title("Substring search: Bruteforce vs Rabin-Karp")
plt.xlabel('M (length of substrings)')
plt.ylabel('Time per 1 search, sec')
plt.legend(loc=4)

plt.show()
