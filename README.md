# 🕵️‍♂️ SPY-RECON: Advanced IoC Extractor
**Intelligence Gathering Tool by SPY-E & 123Tool**

SPY-RECON adalah tool intelijen berbasis terminal yang ditenagai oleh mesin internal **NAGA-SPY-E**. Tool ini dirancang untuk mendeteksi secara otomatis berbagai *Indicators of Compromise* (IoC) dan menghubungkannya dengan database intelijen keamanan global secara instan.

## 🐉 Core Mesin: NAGA-SPY-E
Berbeda dengan tool OSINT biasa, SPY-RECON menggunakan **NAGA-SPY-E Engine** yang bekerja secara asinkron. Kamu tidak perlu memilih kategori; cukup tempelkan data (IP, Hash, CVE, dsb), dan naga kami akan membedahnya untukmu.

## ✨ Fitur Unggulan
- **⚡ Fast Async**: Menembak puluhan database intelijen sekaligus.
- **🧠 Auto-Logic**: Mengenali otomatis format IP, Domain, Email, BTC, dan CVE.
- **🛡️ Stealth Recon**: Menggunakan rotasi identitas browser untuk menghindari blokir.
- **📱 Termux Ready**: Ringan, tanpa GUI, murni kekuatan terminal.

## ⚙️ Jenis Data yang Didukung
- **IPv4 Address**
- **Domain & URL**
- **CVE (Vulnerability ID)**
- **Crypto Wallets (BTC)**
- **Hashes (MD5, SHA1, SHA256)**
- **Email Addresses**

## 🛠️ Instalasi

### 1. Persyaratan
- Python 3.8+
- Library: `aiohttp`, `fake-useragent`

### 2. Cara Install
```bash
git clone [https://github.com/123tool/SPY-EXTRACTOR.git](https://github.com/123tool/SPY-EXTRACTOR.git)
cd SPY-EXTRACTOR
pip install -r requirements.txt
atau
pip install aiohttp fake-useragent
python spy_recon.py
```

### 3. Cara Penggunaan
​Cukup jalankan script, lalu masukkan data IoC target.
Contoh:
```bash
​Masukkan IP: 8.8.8.8
​Masukkan CVE: CVE-2024-1234
​Masukkan Hash: 44d88612fea8a8f36de82e1278abb02f
