import base64

with open("gambar.jpg", "rb") as img_file:
    base64_string = base64.b64encode(img_file.read()).decode("utf-8")

# Simpan hasil konversi ke file convert.txt
with open("convert.txt", "w") as output_file:
    output_file.write(base64_string)

print("Gambar berhasil dikonversi dan disimpan ke convert.txt")