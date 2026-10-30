<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,50:6366f1,100:8b5cf6&height=200&section=header&text=PersonalDNS&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Personal%20DNS%20Management%20Platform&descAlignY=58&descSize=18" width="100%" alt="PersonalDNS Banner"/>

# 🌐 PersonalDNS

### پلتفرم مدیریت DNS شخصی، چندکاربره و حرفه‌ای

**⚡ سریع • 🔒 امن • 📈 مقیاس‌پذیر • 🇮🇷 فارسی / RTL**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-PersonalDNS-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/amirhazbavi/PersonalDNS)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=111827)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![PowerDNS](https://img.shields.io/badge/DNS-PowerDNS-FF6B6B?style=for-the-badge)](https://www.powerdns.com/)
[![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/amirhazbavi/PersonalDNS)

<br>

[![Stars](https://img.shields.io/github/stars/amirhazbavi/PersonalDNS?style=for-the-badge&color=facc15)](https://github.com/amirhazbavi/PersonalDNS/stargazers)
[![Forks](https://img.shields.io/github/forks/amirhazbavi/PersonalDNS?style=for-the-badge&color=38bdf8)](https://github.com/amirhazbavi/PersonalDNS/network/members)
[![Issues](https://img.shields.io/github/issues/amirhazbavi/PersonalDNS?style=for-the-badge&color=ef4444)](https://github.com/amirhazbavi/PersonalDNS/issues)
[![Last Commit](https://img.shields.io/github/last-commit/amirhazbavi/PersonalDNS?style=for-the-badge&color=22c55e)](https://github.com/amirhazbavi/PersonalDNS/commits)

</div>

---

## 📖 PersonalDNS چیست؟

**PersonalDNS** یک پلتفرم مدیریت DNS چندکاربره است که یک **پنل مدیریت مدرن و فارسی** را به یک **DNS Authoritative Server واقعی** (PowerDNS) متصل می‌کند. این پروژه برای مدیریت متمرکز دامنه‌ها، Zoneها، رکوردهای DNS، کاربران، API، امنیت و مانیتورینگ طراحی شده است.

برخلاف پنل‌های ساده که فقط ظاهر مدیریتی دارند، PersonalDNS در صورت اتصال صحیح به PowerDNS و زیرساخت عمومی، **رابط مدیریت یک DNS Authoritative واقعی** است و می‌تواند پاسخ‌دهی به کوئری‌های DNS را بر عهده بگیرد.

<div align="center">
<img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&h=350&fit=crop" alt="DNS Server" width="100%" style="border-radius: 12px;"/>
</div>

---

## 🎯 این برنامه چه کاری انجام می‌دهد؟

فرض کنید دامنهٔ `example.com` را در اختیار دارید. به‌جای دست‌کاری مستقیم فایل‌های Zone یا تنظیمات پیچیدهٔ سرور، وارد داشبورد PersonalDNS می‌شوید و یک رکورد ایجاد می‌کنید:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | `www` | `1.2.3.4` | `3600` |

PersonalDNS این اطلاعات را مدیریت می‌کند و در معماری واقعی آن را به **PowerDNS** منتقل می‌کند. نتیجه:

```
www.example.com  →  DNS Query  →  PowerDNS  →  1.2.3.4
```

این جداسازی باعث می‌شود **پنل مدیریت، دیتابیس و DNS Server** از یکدیگر مستقل باشند و هر بخش بتواند جداگانه مقیاس‌پذیر شود.

---

## ✨ امکانات

<table>
<tr>
<td width="50%">

### 🗂️ مدیریت دامنه
- ✅ افزودن دامنه
- ✅ حذف دامنه
- ✅ مشاهدهٔ وضعیت دامنه
- ✅ مدیریت Zone
- ✅ مدیریت Nameserver

</td>
<td width="50%">

### 📝 مدیریت رکوردها
- ✅ پشتیبانی از رکوردهای رایج:
  - `A` · `AAAA` · `CNAME`
  - `MX` · `TXT` · `NS`
  - `CAA` · `SRV`
- ✅ مدیریت TTL و Priority
- ✅ ویرایش و حذف رکورد

</td>
</tr>
<tr>
<td>

### 👥 سیستم چندکاربره
- ✅ هر کاربر منابع خودش را مدیریت می‌کند
- ✅ نقش‌های `User` · `Manager` · `Admin` · `SuperAdmin`
- ✅ دسترسی مبتنی بر نقش (RBAC)

</td>
<td>

### 🔐 احراز هویت و API
- ✅ JWT
- ✅ Password Hashing
- ✅ API Keys
- ✅ Session Management
- ✅ مستندات Swagger و ReDoc

</td>
</tr>
</table>

---

## 🏗️ معماری

<div align="center">

```mermaid
graph TB
    subgraph Internet["🌍 Internet"]
        C1[👤 Web Browser]
        C2[🌐 DNS Clients]
    end

    subgraph Platform["🖥️ PersonalDNS Platform"]
        N[🔀 Nginx<br/>Reverse Proxy]
        R[⚛️ React Dashboard]
        F[⚡ FastAPI Backend]
        P[(🐘 PostgreSQL)]
        RD[(⚡ Redis Cache)]
        PD[🛰️ PowerDNS<br/>Authoritative]
        M[📊 Prometheus + Grafana]
    end

    C1 -->|HTTPS :443| N
    C2 -->|UDP/TCP :53| PD
    N --> R
    R --> F
    F --> P
    F --> RD
    F -->|Internal API| PD
    F --> M
    PD --> M

    style Platform fill:#0f172a,stroke:#6366f1,color:#fff
    style Internet fill:#1e293b,stroke:#0ea5e9,color:#fff
```

</div>

### 🔄 نحوهٔ کار سیستم

```mermaid
sequenceDiagram
    autonumber
    participant U as 👤 User
    participant R as ⚛️ React Dashboard
    participant F as ⚡ FastAPI API
    participant DB as 🐘 PostgreSQL
    participant PD as 🛰️ PowerDNS

    U->>R: ایجاد رکورد جدید
    R->>F: POST /api/domains/{id}/records
    F->>DB: ذخیرهٔ رکورد
    F->>PD: ارسال به Zone
    PD-->>F: تأیید
    F-->>R: پاسخ موفق
    R-->>U: نمایش رکورد
```

> **نکته:** PowerDNS API باید فقط از داخل شبکهٔ داخلی Docker در دسترس باشد و هرگز مستقیماً روی اینترنت عمومی قرار نگیرد.

---

## 🛠️ تکنولوژی‌ها

| بخش | تکنولوژی |
|-----|----------|
| **Frontend** | React + TypeScript |
| **Backend** | FastAPI + Python |
| **DNS** | PowerDNS Authoritative |
| **Database** | PostgreSQL |
| **Cache** | Redis |
| **Reverse Proxy** | Nginx |
| **Monitoring** | Prometheus + Grafana |
| **Container** | Docker + Docker Compose |

---

## 📁 ساختار پروژه

```
PersonalDNS/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── powerdns/
│   └── pdns.conf
├── nginx/
│   └── nginx.conf
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

## 🚀 نصب سریع

### ۱. دریافت پروژه

```bash
git clone https://github.com/amirhazbavi/PersonalDNS.git
cd PersonalDNS
```

### ۲. ساخت فایل تنظیمات

```bash
cp backend/.env.example backend/.env
nano backend/.env
```

نمونهٔ مقادیر:

```env
DATABASE_URL=postgresql://personaldns:CHANGE_ME@postgres:5432/personaldns
REDIS_URL=redis://redis:6379
SECRET_KEY=CHANGE_THIS_TO_A_LONG_RANDOM_SECRET
POWERDNS_API_URL=http://powerdns:8081
POWERDNS_API_KEY=CHANGE_ME
```

> ⚠️ **هشدار امنیتی:** مقادیر `SECRET_KEY`، `DATABASE_PASSWORD` و `POWERDNS_API_KEY` را هرگز عمومی نکنید و فایل `.env` را در Git ذخیره نکنید.

### ۳. اجرا با Docker

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f
```

### ۴. آدرس‌های محلی

| سرویس | آدرس |
|-------|------|
| **Dashboard** | `http://localhost:3000` |
| **Backend API** | `http://localhost:8000` |
| **Swagger** | `http://localhost:8000/docs` |
| **ReDoc** | `http://localhost:8000/redoc` |

---

## 🌍 نصب کامل روی VPS

برای اجرای واقعی DNS، به یک **VPS با IPv4 عمومی**، **دامنه** و دسترسی به **پورت ۵۳ (UDP/TCP)** نیاز دارید.

### گام‌های کلی

1. **اتصال به VPS** با SSH
2. **نصب Git و Docker**:

   ```bash
   apt update && apt install git curl -y
   curl -fsSL https://get.docker.com | sh
   ```

3. **دریافت پروژه** و تنظیم `.env`
4. **تنظیم Firewall**:

   ```bash
   ufw allow 53/udp
   ufw allow 53/tcp
   ufw allow 22/tcp
   ufw allow 80/tcp
   ufw allow 443/tcp
   ufw enable
   ```

5. **تنظیم Glue Record و Nameserver دامنه** در Registrar:

   ```
   ns1.example.com → 1.2.3.4
   ns2.example.com → 1.2.3.4
   ```

6. **تنظیم رکوردهای NS دامنه** به `ns1.example.com` و `ns2.example.com`

> ⚠️ صرفاً اجرای سایت یا GitHub Pages باعث فعال‌شدن DNS واقعی نمی‌شود. مسیر کامل باید از **Registrar → NS Records → Public IP → Firewall → Port 53 → PowerDNS** برقرار باشد.

---

## 🧪 تست DNS

```bash
dig example.com
dig @SERVER_IP example.com A
dig @SERVER_IP example.com MX
dig @SERVER_IP example.com TXT
```

---

## 🔌 API

### احراز هویت

| متد | مسیر | توضیح |
|-----|------|-------|
| `POST` | `/api/auth/register` | ثبت‌نام |
| `POST` | `/api/auth/login` | ورود |

### دامنه‌ها

| متد | مسیر | توضیح |
|-----|------|-------|
| `GET` | `/api/domains` | لیست دامنه‌ها |
| `POST` | `/api/domains` | ایجاد دامنه |
| `GET` | `/api/domains/{id}` | جزئیات دامنه |
| `DELETE` | `/api/domains/{id}` | حذف دامنه |

### رکوردها

| متد | مسیر | توضیح |
|-----|------|-------|
| `GET` | `/api/domains/{id}/records` | لیست رکوردها |
| `POST` | `/api/domains/{id}/records` | ایجاد رکورد |
| `PUT` | `/api/records/{id}` | ویرایش رکورد |
| `DELETE` | `/api/records/{id}` | حذف رکورد |

### سلامت

| متد | مسیر | توضیح |
|-----|------|-------|
| `GET` | `/health` | بررسی سلامت سرویس |

📚 مستندات کامل: `http://SERVER_IP:8000/docs`

---

## 🔒 امنیت

برای محیط **Production** موارد زیر الزامی است:

- ✅ استفاده از **HTTPS**
- ✅ **Secretهای قوی** و عدم ذخیره در Git
- ✅ **Hash کردن رمز عبورها**
- ✅ **JWT امن** و **API Keyهای امن**
- ✅ **Rate Limiting** و **Validation**
- ✅ **RBAC** و **Audit Logs**
- ✅ محدودکردن دسترسی **PowerDNS API** به شبکهٔ داخلی
- ✅ **Firewall** و **Backup** منظم
- ✅ عدم قرار دادن **PostgreSQL** روی اینترنت عمومی

---

## 🛡️ DNSSEC

DNSSEC برای افزایش اعتبار و امنیت پاسخ‌های DNS استفاده می‌شود. فعال‌سازی کامل آن به تنظیمات واقعی PowerDNS، Zoneها و Registrar وابسته است.

ساختار کلی:

```
Domain
  │
  ▼
DNSSEC
  ├── DNSKEY
  ├── RRSIG
  └── DS
```

---

## 📊 مانیتورینگ

PersonalDNS با **Prometheus** و **Grafana** قابل مانیتور است.

```mermaid
graph LR
    A[PersonalDNS] --> B[API Metrics]
    A --> C[Database Metrics]
    A --> D[DNS Metrics]
    A --> E[System Metrics]
    B --> F[Prometheus]
    C --> F
    D --> F
    E --> F
    F --> G[Grafana]
```

موارد قابل مانیتور:

- تعداد درخواست‌ها
- خطاها
- وضعیت API و DNS
- مصرف منابع
- Latency
- وضعیت Database

---

## 💾 Backup

### PostgreSQL

```bash
# Backup
docker compose exec postgres pg_dump -U personaldns personaldns > backup.sql

# Restore
cat backup.sql | docker compose exec -T postgres psql -U personaldns personaldns
```

> نام کاربر و دیتابیس باید با `docker-compose.yml` واقعی پروژه یکسان باشد.

---

## 🧯 عیب‌یابی

| مشکل | دستور / راه‌حل |
|------|----------------|
| Docker اجرا نمی‌شود | `docker --version` و `docker compose version` |
| Backend اجرا نمی‌شود | `docker compose logs backend` و بررسی `.env` |
| Frontend باز نمی‌شود | `docker compose logs frontend` |
| PowerDNS اجرا نمی‌شود | `docker compose logs powerdns` |
| DNS پاسخ نمی‌دهد | بررسی فایروال، پورت ۵۳ و Glue Record |
| خطای مجوز | بررسی `SECRET_KEY` و `POWERDNS_API_KEY` |

---

## 🗺️ Roadmap

- [x] پنل مدیریت دامنه و رکورد
- [x] سیستم چندکاربره و RBAC
- [x] API با JWT و API Key
- [x] Docker Compose کامل
- [x] اتصال به PowerDNS
- [ ] رابط کاربری کاملاً RTL و فارسی
- [ ] پشتیبانی از DNSSEC به‌صورت کامل
- [ ] داشبورد تحلیلی پیشرفته
- [ ] اعلان‌های لحظه‌ای (WebSocket)
- [ ] افزودن تست‌های خودکار جامع

---

## 🤝 مشارکت

از مشارکت شما استقبال می‌شود!

1. **Fork** کنید
2. یک **Branch** جدید بسازید (`feature/amazing-feature`)
3. تغییرات را **Commit** کنید
4. **Push** کنید
5. یک **Pull Request** باز کنید

### گزارش باگ

هنگام ثبت Issue موارد زیر را اضافه کنید:

- **OS:**
- **Docker Version:**
- **Docker Compose Version:**
- **Browser:**
- **Error:**
- **Steps to Reproduce:**
- **Logs:**

🔗 [Issues](https://github.com/amirhazbavi/PersonalDNS/issues)

---

## 📄 License

این پروژه تحت مجوز **MIT** منتشر شده است. برای جزئیات بیشتر فایل [LICENSE](LICENSE) را ببینید.

---

<div align="center">

### 🌟 اگر این پروژه برایتان مفید بود، به آن ⭐ بدهید!

**PersonalDNS** — مدیریت DNS، به سادگی و قدرت.

ساخته‌شده با ❤️ برای جامعهٔ فارسی‌زبان

<br>

[![GitHub Stars](https://img.shields.io/github/stars/amirhazbavi/PersonalDNS?style=social)](https://github.com/amirhazbavi/PersonalDNS/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/amirhazbavi/PersonalDNS?style=social)](https://github.com/amirhazbavi/PersonalDNS/network/members)
[![GitHub Watchers](https://img.shields.io/github/watchers/amirhazbavi/PersonalDNS?style=social)](https://github.com/amirhazbavi/PersonalDNS/watchers)

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8b5cf6,50:6366f1,100:0ea5e9&height=120&section=footer" width="100%" alt="Footer"/>

</div>
