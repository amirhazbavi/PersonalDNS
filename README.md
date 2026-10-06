<div align="center">🟣 PersonalDNS

پلتفرم مدیریت DNS شخصی، سریع و چندکاربره 🇮🇷

مدیریت دامنه‌ها، رکوردهای DNS، کاربران و زیرساخت DNS در یک پنل مدرن

<br>""GitHub" (https://img.shields.io/badge/GitHub-PersonalDNS-181717?style=for-the-badge&logo=github)" (https://github.com/amirhazbavi/PersonalDNS)
""License" (https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)" (LICENSE)
""Backend" (https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)" (https://fastapi.tiangolo.com/)
""Frontend" (https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=111827)" (https://react.dev/)
""Docker" (https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)" (https://www.docker.com/)

<br>⚡ سریع • 🔐 امن • 🌐 مقیاس‌پذیر • 🇮🇷 فارسی و RTL

</div>---

🚀 PersonalDNS چیست؟

PersonalDNS یک پلتفرم مدیریت DNS چندکاربره است که برای مدیریت حرفه‌ای دامنه‌ها و رکوردهای DNS طراحی شده است.

هدف پروژه این است که مدیریت DNS را از یک کار پیچیده به یک تجربه ساده، سریع و قابل‌کنترل تبدیل کند.

                 🌐 Internet
                      │
                      ▼
              ┌───────────────┐
              │   PersonalDNS │
              │   Dashboard   │
              └───────┬───────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       🌐 Domains   📋 Records   👥 Users
          │           │           │
          └───────────┼───────────┘
                      ▼
                 ⚡ PowerDNS
                      │
                      ▼
                  DNS :53

---

✨ امکانات اصلی

<table>
<tr>
<td width="50%">🌐 مدیریت DNS

- مدیریت چندین دامنه
- ساخت و حذف Zone
- مدیریت رکوردها
- TTL قابل تنظیم
- مدیریت Nameserver

</td><td width="50%">👥 چندکاربره

- ثبت‌نام کاربران
- ورود امن
- مدیریت پروفایل
- Role و Permission
- پنل مدیریت

</td>
</tr><tr>
<td>🔐 امنیت

- JWT Authentication
- Password Hashing
- API Keys
- Rate Limiting
- Audit Logs
- کنترل دسترسی

</td><td>📊 مانیتورینگ

- آمار DNS
- وضعیت سرویس‌ها
- Health Check
- Prometheus
- Grafana
- گزارش رویدادها

</td>
</tr>
</table>---

📋 رکوردهای DNS

PersonalDNS برای رکوردهای رایج DNS طراحی شده است:

Record| کاربرد
"A"| IPv4
"AAAA"| IPv6
"CNAME"| Alias
"MX"| Mail Server
"TXT"| Verification / SPF / سایر اطلاعات
"NS"| Name Server
"CAA"| Certificate Authority
"SRV"| Service Discovery

---

🎨 پنل مدیریت

رابط کاربری پروژه با تمرکز روی تجربه کاربری ساخته می‌شود:

┌─────────────────────────────────────────────────────────┐
│ 🟣 PersonalDNS                         🔔   👤 User     │
├──────────────┬──────────────────────────────────────────┤
│              │                                          │
│ 🏠 Dashboard │   Overview                               │
│              │                                          │
│ 🌐 Domains   │   ┌────────┐ ┌────────┐ ┌────────┐     │
│              │   │   12   │ │   84   │ │   11   │     │
│ 📋 Records   │   │Domains │ │Records │ │ Active │     │
│              │   └────────┘ └────────┘ └────────┘     │
│ 🔐 DNSSEC    │                                          │
│              │   🌐 example.com                         │
│ 🔑 API Keys  │   ┌──────────────────────────────────┐   │
│              │   │ 🟢 Active   12 Records           │   │
│ 📊 Analytics │   │ ns1.example.com                  │   │
│              │   └──────────────────────────────────┘   │
│ 📝 Logs      │                                          │
│              │   [+ Add Domain]                         │
│ ⚙️ Settings  │                                          │
└──────────────┴──────────────────────────────────────────┘

«رابط نهایی پروژه می‌تواند کاملاً فارسی، RTL و Responsive باشد.»

---

🧠 معماری

                           ┌─────────────────┐
                           │     Client      │
                           │  Web / Mobile   │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │      Nginx      │
                           │ Reverse Proxy   │
                           └───────┬─┬───────┘
                                   │ │
                    ┌──────────────┘ └──────────────┐
                    ▼                               ▼
             ┌──────────────┐              ┌──────────────┐
             │    React     │              │   FastAPI    │
             │  Frontend    │              │     API      │
             └──────────────┘              └──────┬───────┘
                                                  │
                     ┌────────────────────────────┼───────────────┐
                     │                            │               │
                     ▼                            ▼               ▼
              ┌─────────────┐             ┌─────────────┐  ┌─────────────┐
              │ PostgreSQL  │             │    Redis    │  │  PowerDNS   │
              │   Database  │             │    Cache    │  │ Authoritative│
              └─────────────┘             └─────────────┘  └──────┬──────┘
                                                                   │
                                                                   ▼
                                                              DNS :53

---

🛠️ Tech Stack

<div align="center">بخش| فناوری
🎨 Frontend| React + TypeScript
⚙️ Backend| FastAPI + Python
🌐 DNS| PowerDNS Authoritative
🐘 Database| PostgreSQL
⚡ Cache| Redis
🌍 Proxy| Nginx
📊 Monitoring| Prometheus + Grafana
🐳 Deployment| Docker / Docker Compose

</div>---

📁 ساختار پروژه

PersonalDNS/
│
├── 📁 backend/
│   ├── 📁 app/
│   │   ├── 📁 api/
│   │   ├── 📁 core/
│   │   ├── 📁 models/
│   │   ├── 📁 schemas/
│   │   ├── 📁 services/
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── 📁 frontend/
│   ├── 📁 src/
│   ├── 📁 public/
│   ├── package.json
│   └── Dockerfile
│
├── 📁 powerdns/
│   └── pdns.conf
│
├── 📁 nginx/
│   └── nginx.conf
│
├── 📁 monitoring/
│   ├── prometheus.yml
│   └── grafana/
│
├── 🐳 docker-compose.yml
├── 📄 README.md
└── 📄 LICENSE

---

⚡ نصب سریع

1️⃣ دریافت پروژه

git clone https://github.com/amirhazbavi/PersonalDNS.git
cd PersonalDNS

2️⃣ تنظیم Environment

cp backend/.env.example backend/.env

3️⃣ اجرای سرویس‌ها

docker compose up -d --build

4️⃣ بررسی وضعیت

docker compose ps

---

🔗 آدرس سرویس‌ها

سرویس| آدرس
🖥️ Dashboard| "http://localhost:3000"
⚙️ API| "http://localhost:8000"
📚 Swagger| "http://localhost:8000/docs"
📖 ReDoc| "http://localhost:8000/redoc"

---

🔌 API

نمونه Endpointهای اصلی:

POST /api/auth/register
POST /api/auth/login

GET /api/domains
POST /api/domains
GET /api/domains/{id}
DELETE /api/domains/{id}

GET /api/domains/{id}/records
POST /api/domains/{id}/records

PUT /api/records/{id}
DELETE /api/records/{id}

---

🔐 Security

PersonalDNS با درنظرگرفتن امنیت یک سرویس چندکاربره طراحی می‌شود.

🔒 Authentication

User
 │
 ▼
Login
 │
 ▼
JWT
 │
 ▼
API

🛡️ قابلیت‌ها

- JWT Authentication
- Password Hashing
- API Keys
- Role-Based Access Control
- Rate Limiting
- Input Validation
- Audit Logging
- CORS Configuration
- HTTPS در Production
- محدودسازی PowerDNS API
- مدیریت Secretها با Environment Variables

«🚨 هیچ Password، Token یا API Key واقعی را داخل GitHub قرار ندهید.»

---

🔐 DNSSEC

ساختار پروژه برای استفاده از DNSSEC آماده طراحی شده است.

Domain
   │
   ▼
DNSSEC
   │
   ├── DNSKEY
   ├── DS
   └── RRSIG

فعال‌سازی نهایی DNSSEC باید متناسب با تنظیمات واقعی PowerDNS و Registrar انجام شود.

---

🇮🇷 امکانات مخصوص ایران

PersonalDNS با تمرکز ویژه روی کاربران فارسی‌زبان طراحی شده است:

- 🇮🇷 رابط فارسی
- ↔️ پشتیبانی RTL
- 💰 نمایش قیمت به تومان در صورت اضافه‌شدن Billing
- 📱 طراحی مناسب موبایل
- 🌐 آماده اتصال به Registrarهای مختلف
- 🛠️ معماری قابل توسعه برای سرویس‌های داخلی

«اتصال واقعی به یک Registrar یا درگاه پرداخت، نیازمند API رسمی همان سرویس و پیاده‌سازی Adapter مربوطه است.»

---

📊 Monitoring

                 PersonalDNS
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      Application              PowerDNS
          │                       │
          └───────────┬───────────┘
                      ▼
                 Prometheus
                      │
                      ▼
                   Grafana
                      │
                      ▼
                📈 Dashboard

---

🌍 استفاده به‌عنوان DNS واقعی

برای استفاده واقعی از PersonalDNS به‌عنوان Authoritative DNS، سرویس باید روی زیرساختی اجرا شود که امکان دریافت ترافیک DNS روی:

UDP 53
TCP 53

را داشته باشد.

نمونه Nameserver:

ns1.example.com → SERVER_IP
ns2.example.com → SERVER_IP

و در صورت نیاز Registrar باید Glue Recordهای مربوط به Nameserverها را نیز تنظیم کند.

«⚠️ GitHub Pages فقط برای Frontend/Static Website مناسب است و جایگزین Authoritative DNS Server نیست.»

---

⚙️ Environment

نمونه تنظیمات:

DATABASE_URL=postgresql://user:password@postgres:5432/personaldns

REDIS_URL=redis://redis:6379

SECRET_KEY=CHANGE_ME

POWERDNS_API_URL=http://powerdns:8081

POWERDNS_API_KEY=CHANGE_ME

---

🧪 توسعه

Backend:

cd backend

python -m venv .venv

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

Frontend:

cd frontend

npm install

npm run dev

---

🐳 Docker

اجرای کامل:

docker compose up -d --build

مشاهده Logها:

docker compose logs -f

خاموش‌کردن:

docker compose down

---

📈 مسیر توسعه

- [x] معماری Multi-User
- [x] REST API Design
- [x] Docker Architecture
- [x] React + FastAPI Architecture
- [ ] اتصال کامل PowerDNS
- [ ] DNSSEC کامل
- [ ] Billing
- [ ] سیستم Subscription
- [ ] Registrar Adapters
- [ ] Advanced Analytics
- [ ] Backup & Restore
- [ ] Multi-Server DNS
- [ ] High Availability

---

🗺️ Roadmap

Phase 1
████████████████████  Architecture

Phase 2
████████████████░░░░  DNS Management

Phase 3
████████████░░░░░░░░  Multi-User

Phase 4
████████░░░░░░░░░░░░  DNSSEC

Phase 5
██████░░░░░░░░░░░░░░  Billing

Phase 6
████░░░░░░░░░░░░░░░░  High Availability

---

🤝 مشارکت

Pull Requestها و Issueها برای توسعه پروژه استقبال می‌شوند.

git clone https://github.com/amirhazbavi/PersonalDNS.git

cd PersonalDNS

git checkout -b feature/my-feature

بعد از اعمال تغییرات:

git add .
git commit -m "Add new feature"
git push origin feature/my-feature

---

📜 License

PersonalDNS تحت مجوز MIT منتشر شده است.

---

🔗 Links

📦 Repository

""GitHub" (https://img.shields.io/badge/Repository-PersonalDNS-181717?style=for-the-badge&logo=github)" (https://github.com/amirhazbavi/PersonalDNS)

🐛 Issues

""Issues" (https://img.shields.io/badge/Report-Issue-e11d48?style=for-the-badge&logo=github)" (https://github.com/amirhazbavi/PersonalDNS/issues)

---

<div align="center">🟣 PersonalDNS

DNS Management, Simplified.

⚡ Fast • 🔐 Secure • 🌐 Scalable • 🇮🇷 RTL

<br>Made with ❤️ for Persian developers

PersonalDNS © 2026

</div>
