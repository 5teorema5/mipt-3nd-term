import numpy as np

P_m = np.array([91.502, 76.59, 52.29])
sigma_P_m = np.array([0.732, 2.95, 3.99])
m = 0.831
sigma_m = 0.006
d = 0.5825
sigma_d = 0.0112
alpha = 0.3162
sigma_alpha = 0.008
beta = 43.547
sigma_beta = 3.435

B_h = (np.pi ** 2 * m * d ** 2) / (3 * alpha ** 2 * P_m)
sigma_B_h = B_h * np.sqrt(
    (sigma_m / m) ** 2 + (2 * sigma_d / d) ** 2 + (2 * sigma_alpha / alpha) ** 2 + (sigma_P_m / P_m) ** 2)
for i in range(3):
    print(fr'A & {P_m[i]} & {sigma_P_m[i]} & {round(B_h[i], 3)} & {round(sigma_B_h[i], 3)} \\ \hline')

B_v = beta / P_m
sigma_B_v = B_v * np.sqrt((sigma_beta / beta) ** 2 + (sigma_P_m / P_m) ** 2)
for i in range(3):
    print(fr'A & {P_m[i]} & {sigma_P_m[i]} & {round(B_v[i], 3)} & {round(sigma_B_v[i], 3)} \\ \hline')

for i in range(3):
    print(
        fr'A & {P_m[i]} & {sigma_P_m[i]} & {round(B_h[i], 3)} & {round(sigma_B_h[i], 3)} & {round(B_v[i], 3)} & {round(sigma_B_v[i], 3)} & {round(np.arctan(B_v[i] / B_h[i]) * 180 / np.pi, 3)} & {round(np.sqrt(B_v[i] ** 2 + B_h[i] ** 2), 3)} & {round(np.sqrt(sigma_B_v[i] ** 2 + sigma_B_h[i] ** 2), 3)} \\ \hline')

print(B_v)
print(B_h)
