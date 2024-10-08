import os
import requests
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

try:
    # Load konfigurasi dari file .env
    load_dotenv('CONFIG.ENV')
    gist_url = os.getenv('GIST_URL')

    # Mengunduh file credentials.json dari Gist
    response = requests.get(gist_url)

    # Periksa apakah file berhasil diunduh
    if response.status_code == 200:
        # Memuat konten JSON ke dalam objek Python
        credentials_json = json.loads(response.text)
    else:
        print(f"Gagal mengunduh credentials.json, status code: {response.status_code}")
        exit(1)

    # Ambil token bot dan konfigurasi lainnya dari variabel environment
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
    INOUT_ID = os.getenv("INOUT_ID")
    LIST_ID = os.getenv("LIST_ID")
    RANGE_NAME = os.getenv("RANGE_NAME")
    RANGE_INOUT = os.getenv("RANGE_INOUT")
    RANGE_STOK = os.getenv("RANGE_STOK")
    RANGE_LIST = os.getenv("RANGE_LIST")

    # Periksa apakah variabel environment terisi dengan benar
    if not BOT_TOKEN or not SPREADSHEET_ID:
        print("Error: Pastikan BOT_TOKEN dan SPREADSHEET_ID terisi dengan benar di file .env")
        exit(1)

    # Ganti 'credentials.json' dengan objek JSON kredensial akun layanan Anda
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # Membuat kredensial menggunakan service account dari JSON yang diunduh
    creds = Credentials.from_service_account_info(credentials_json, scopes=SCOPES)

    # Membuat layanan Google Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    print("Bot berhasil diinisialisasi dan siap beroperasi!")

except Exception as e:
    print(f"Error occurred: {e}")