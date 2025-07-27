from PIL import Image
import numpy as np

img = Image.open(input())
data = np.array(img)
l = int(data.size)
new_data = np.zeros((data.shape[0] // 2, data.shape[1] // 2))

for i in range(1, data.shape[0], 2):
    for j in range(1, data.shape[1], 2):
        s = int(data[i - 1][j - 1]) + int(data[i - 1][j]) + int(data[i][j - 1]) + int(data[i][j])
        new_data[i // 2][j // 2] = int(s // 4)
print(int(new_data.min()), int(new_data.max()))