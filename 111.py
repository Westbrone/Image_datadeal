from PIL import Image
# 打开单通道图像文件
grayscale_image = Image.open("fixed_label.png")  # 替换成您的单通道图像文件路径

# 获取单通道图像的大小
width, height = grayscale_image.size


# 创建一个用于保存像素值的文本文件
with open("pixel_values.txt", "w") as file:
    # 遍历每个像素行
    for y in range(height):
        # 遍历每一行的像素值
        row_pixels = [f"{grayscale_image.getpixel((x, y)):03d}" for x in range(width)]
        # 确保每一行都包含256个数字
        if len(row_pixels) == 256:
            # 将一行像素值连接成一个字符串，并写入文本文件
            file.write(" ".join(row_pixels) + "\n")

# 关闭图像
grayscale_image.close()

