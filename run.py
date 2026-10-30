#!/usr/bin/env python3
"""
================================================================================
 PersonalDNS — Launcher (run.py)
================================================================================
 اسکریپت راه‌اندازی خودکار: README + LICENSE + .env + dependencies + run
================================================================================
"""

from __future__ import annotations

import os
import sys
import time
import shutil
import socket
import subprocess
import webbrowser
import importlib.util
from pathlib import Path
from textwrap import dedent

# ============================================================================
# CONSTANTS
# ============================================================================

BASE_DIR = Path(__file__).resolve().parent
README_PATH = BASE_DIR / "README.md"
LICENSE_PATH = BASE_DIR / "LICENSE"
ENV_PATH = BASE_DIR / ".env"
MAIN_PY = BASE_DIR / "main.py"

APP_HOST = "127.0.0.1"
APP_PORT = 8000
DOCS_URL = f"http://{APP_HOST}:{APP_PORT}/docs"

REQUIRED_PACKAGES = [
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn[standard]"),
    ("sqlalchemy", "sqlalchemy"),
    ("pydantic", "pydantic"),
    ("pydantic_settings", "pydantic-settings"),
    ("passlib", "passlib[bcrypt]"),
    ("jose", "python-jose[cryptography]"),
    ("httpx", "httpx"),
    ("multipart", "python-multipart"),
    ("email_validator", "email-validator"),
]


# ============================================================================
# ANSI COLORS
# ============================================================================

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


def _supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            return True
        except Exception:
            return False
    return sys.stdout.isatty()


if not _supports_color():
    for attr in dir(C):
        if not attr.startswith("_"):
            setattr(C, attr, "")


def info(msg: str) -> None:
    print(f"{C.CYAN}ℹ{C.RESET}  {msg}")


def ok(msg: str) -> None:
    print(f"{C.GREEN}✔{C.RESET}  {msg}")


def warn(msg: str) -> None:
    print(f"{C.YELLOW}⚠{C.RESET}  {msg}")


def err(msg: str) -> None:
    print(f"{C.RED}✘{C.RESET}  {msg}", file=sys.stderr)


def step(n: int, total: int, title: str) -> None:
    print(f"\n{C.BOLD}{C.MAGENTA}[{n}/{total}]{C.RESET} {C.BOLD}{title}{C.RESET}")


def banner() -> None:
    print(f"""{C.BOLD}{C.CYAN}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   ██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗ █████╗ ██╗     ║
║   ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔══██╗██║     ║
║   ██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║███████║██║     ║
║   ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║██╔══██║██║     ║
║   ██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║██║  ██║███████╗║
║   ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝║
║                                                                      ║
║              Personal DNS Management Platform — Launcher             ║
╚══════════════════════════════════════════════════════════════════════╝
{C.RESET}""")


# ============================================================================
# 1. README CONTENT
# ============================================================================

README_CONTENT = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,50:6366f1,100:8b5cf6&height=200&section=header&text=PersonalDNS&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Personal%20DNS%20Management%20Platform&descAlignY=58&descSize=18" width="100%" alt="PersonalDNS Banner"/>

# 🌐 PersonalDNS

### پلتفرم مدیریت DNS شخصی، چندکاربره و حرفه‌ای

**⚡ سریع • 🔒 امن • 📈 مقیاس‌پذیر • 🇮🇷 فارسی / RTL**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-PersonalDNS-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/amirhazbavi/PersonalDNS)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![PowerDNS](https://img.shields.io/badge/DNS-PowerDNS-FF6B6B?style=for-the-badge)](https://www.powerdns.com/)

</div>

---

## 📖 PersonalDNS چیست؟

**PersonalDNS** یک پلتفرم مدیریت DNS چندکاربره است که یک **پنل مدیریت مدرن و فارسی** را به یک **DNS Authoritative Server واقعی** (PowerDNS) متصل می‌کند.

---

## ⚡ اجرا در یک قدم

```bash
python run.py
