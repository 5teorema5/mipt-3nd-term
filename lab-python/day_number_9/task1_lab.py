import numpy as np
from PIL import Image

paths = ['lunar01_raw.jpg', 'lunar02_raw.jpg', 'lunar03_raw.jpg']

for path in paths:
    img = Image.open('doc/' + path)
    data = np.array(img, dtype=int)

    min_pixel, max_pixel = data.min(), np.concatenate(data).max()
    updated_data = np.array((data - min_pixel) * 255 / (max_pixel - min_pixel), dtype=int)

    res_img = Image.fromarray(updated_data).convert('RGB')
    res_img.save('doc/updated_' + path)
