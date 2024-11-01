# Menggunakan image Python sebagai base
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Copy semua file dari direktori lokal ke direktori kerja di dalam container
COPY . .

# Install dependencies dari file requirements.txt jika ada
# Jika tidak ada requirements.txt, baris ini bisa dihapus
RUN pip install --no-cache-dir -r requirements.txt

# Menjalankan main.py saat container dimulai
CMD ["python", "main.py"]