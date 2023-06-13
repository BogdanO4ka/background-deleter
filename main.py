from rembg import remove
from PIL import Image
import os

input_directory = "images" # Папка куда нужно закидывать файлы для обработки
output_directory = "ready_images" # Папка где будут сохранятся файлы после обработки

file_list_input = []
file_list_output = []
count = 0
for filename in os.listdir('images'):
    input_path = f"{input_directory}/{filename}"
    output_path = filename.partition('.')[0]
    output_path = f"{output_directory}/{output_path}_output.png"
    file_list_input.append(input_path)
    file_list_output.append(output_path)
for i in file_list_input:
    open_image = Image.open(i)
    output = remove(open_image)
    output_elem = file_list_output[count]
    output.save(output_elem)
    count += 1
    print(f"{count} файл обработан.")

print(file_list_input)
print(file_list_output)
