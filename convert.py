import os
from PIL import Image

dir_name = 'original'
new_dir_name = 'convert'

files = os.listdir(dir_name)
new_width = 500 # リサイズ後の幅

for file in files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    img = Image.open(os.path.join(dir_name, file))
    width, height = img.size

    # アスペクト比を固定してリサイズ
    new_height = int((new_width / width) * height)
    img_resize = img.resize((new_width, new_height), resample=Image.LANCZOS)
    image = img_resize.convert("RGB")
    img_resize.save(os.path.join(new_dir_name, file_name + ".avif"), format="avif")
