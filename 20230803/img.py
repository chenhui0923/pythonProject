
from  PIL import Image

image_path = './20230803/lALPKHe21gt_pvzNBNjNBXg_1400_1240.png'
image = Image.open(image_path)
image_data = np.array(image)
print(image_data)