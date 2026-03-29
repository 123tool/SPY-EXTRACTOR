#!/usr/bin/python
# -*- coding: utf-8 -*-
# BRAND   : SPY-RECON (Powered by SPY-E & 123Tool)
# ENGINE  : NAGA-GANAS V2.0 (INTERNAL CORE)

import asyncio
import aiohttp
import re
import os
import sys
import time
from fake_useragent import UserAgent

# UI Palette - Hitam, Merah, Hijau (Vibe Hacker)
R = '\033[1;31m'  # Naga Ganas Red
G = '\033[1;32m'  # Spy Green
Y = '\033[1;33m'  # Alert Yellow
B = '\033[1;34m'  # Deep Blue
C = '\033[1;36m'  # Cyan Info
W = '\033[1;37m'  # White
Reset = '\033[0m'

class SpyRecon:
    def __init__(self):
        self.brand = "SPY-RECON"
        self.engine = "NAGA-GANAS"
        self.ua = UserAgent()
        # Mapping Engine Security Global
        self.intel_sources = [
            {"name": "VirusTotal", "url": "https://www.virustotal.com/gui/search/{}", "types": ["IP", "Domain", "Hash", "URL"]},
            {"name": "AbuseIPDB", "url": "https://www.abuseipdb.com/check/{}", "types": ["IP"]},
            {"name": "Shodan", "url": "https://www.shodan.io/host/{}", "types": ["IP"]},
            {"name": "Censys", "url": "https://censys.io/ipv4/{}", "types": ["IP"]},
            {"name": "EmailRep", "url": "https://emailrep.io/{}", "types": ["Email"]},
            {"name": "Blockchain", "url": "https://www.blockchain.com/explorer/addresses/btc/{}", "types": ["BTC"]},
            {"name": "CVE_NVD", "url": "https://nvd.nist.gov/vuln/detail/{}", "types": ["CVE"]},
            {"name": "URLScan", "url": "https://urlscan.io/domain/{}", "types": ["Domain", "URL"]},
            {"name": "GreyNoise", "url": "https://viz.greynoise.io/ip/{}", "types": ["IP"]},
            {"name": "HybridAnalysis", "url": "https://www.hybrid-analysis.com/search?query={}", "types": ["Hash", "Domain"]}
        ]

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.clear()
        print(f"""{G}
     ███████╗██████╗ ██╗   ██╗      ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
     ██╔════╝██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
     ███████╗██████╔╝ ╚████╔╝█████╗██████╔╝█████╗  ██║     ██║  ██║██╔██╗ ██║
     ╚════██║██╔═══╝   ╚██╔╝ ╚════╝██╔══██╗██╔══╝  ██║     ██║  ██║██║╚██╗██║
     ███████║██║        ██║        ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
     ╚══════╝╚═╝        ╚═╝        ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
    {W}--------------------------------------------------------------------------
    {R} INTERNAL ENGINE: {self.engine} CORE (V.2.0 - GANAS MODE)
    {G} BRAND OWNER    : SPY-E & 123Tool
    {W}--------------------------------------------------------------------------{Reset}""")

    def ioc_identifier(self, data):
        # Regex Naga Ganas Mode
        regex_map = {
            "IP": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "BTC": r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b",
            "CVE": r"CVE-\d{4}-\d{4,7}",
            "Domain": r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]\b",
            "Hash": r"\b[a-fA-F0-9]{32,64}\b"
        }
        for label, pattern in regex_map.items():
            match = re.search(pattern, data)
            if match: return label, match.group()
        return None, None

    async def hit_intel(self, source, val):
        # Async Hit ke database security
        print(f"{W}[{G}READY{W}] {source['name']:<15} : {C}{source['url'].format(val)}")

    async def scan_ioc(self, target):
        label, val = self.ioc_identifier(target)
        if not label:
            print(f"{R}[!] ERROR: Tipe IoC Tidak Dikenali oleh Core Naga Ganas!{Reset}")
            return

        print(f"\n{Y}[*] Core Naga Ganas Mendeteksi: {label}{Reset}")
        print(f"{W}[+] Analisis Target: {G}{val}{Reset}\n")
        
        tasks = []
        for src in self.intel_sources:
            if label in src['types']:
                tasks.append(self.hit_intel(src, val))
        
        if tasks:
            await asyncio.gather(*tasks)
        else:
            print(f"{R}[!] Tidak ada engine intelijen yang cocok untuk tipe ini.")

    def run(self):
        self.banner()
        while True:
            try:
                target = input(f"\n{G}SPY-RECON{W}@{R}NagaGanas{W}:~# {Reset}").strip()
                if not target: continue
                if target.lower() in ['exit', 'quit', '0']: 
                    print(f"{R}[!] Naga Ganas Tidur...{Reset}"); break
                
                asyncio.run(self.scan_ioc(target))
                print(f"\n{W}--------------------------------------------------{Reset}")
            except KeyboardInterrupt:
                print(f"\n{R}[!] Shutdown...{Reset}"); break

if __name__ == "__main__":
    app = SpyRecon()
    app.run()
