FROM python:3.10-slim

WORKDIR /app

# Salin file ke direktori kerja
COPY . .

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Pastikan start.sh memiliki izin eksekusi
RUN chmod +x start.sh

# Tentukan perintah untuk dijalankan
CMD ["bash", "./start.sh"]