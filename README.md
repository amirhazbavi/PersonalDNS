🟣 PersonalDNS

قوی‌ترین و سریع‌ترین پلتفرم مدیریت DNS شخصی چندکاربره برای ایران 🇮🇷

PersonalDNS یک پلتفرم مدرن برای مدیریت دامنه‌ها، رکوردهای DNS، کاربران و زیرساخت DNS است که با تمرکز بر سرعت، امنیت، مقیاس‌پذیری و رابط کاربری فارسی/RTL طراحی شده است.

<p align="center">""GitHub" (https://img.shields.io/badge/GitHub-PersonalDNS-black?logo=github&logoColor=white)" (https://github.com/amirhazbavi/PersonalDNS)
""License" (https://img.shields.io/badge/License-MIT-green.svg)" (LICENSE)
""Backend" (https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)" (https://fastapi.tiangolo.com/)
""Frontend" (https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=black)" (https://react.dev/)
""Docker" (https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)" (https://www.docker.com/)

</p>---

🚀 امکانات

- 🌐 مدیریت چندین دامنه
- 👥 پشتیبانی از چند کاربر
- 📋 مدیریت رکوردهای DNS
- ⚡ مدیریت سریع رکوردها
- 🔐 پشتیبانی از DNSSEC
- 🔑 API Key
- 🛡️ احراز هویت امن
- 📝 ثبت Audit Log
- 📊 آمار و مانیتورینگ
- 🌍 PowerDNS Authoritative
- 🐘 PostgreSQL
- ⚡ Redis
- 🐳 Docker
- 📱 رابط کاربری Responsive
- 🇮🇷 رابط فارسی و RTL
- 🔒 کنترل دسترسی کاربران
- 👑 پنل مدیریت
- 🚦 Rate Limiting
- 🔄 آماده برای توسعه و مقیاس‌پذیری

---

📋 رکوردهای پشتیبانی‌شده

نوع| توضیح
"A"| آدرس IPv4
"AAAA"| آدرس IPv6
"CNAME"| نام مستعار دامنه
"MX"| Mail Server
"TXT"| متن و تنظیمات سرویس‌ها
"NS"| Name Server
"CAA"| مجوز صدور گواهی
"SRV"| اطلاعات سرویس

---

🏗️ معماری

                    ┌──────────────────┐
                    │     Browser      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Nginx       │
                    └───────┬───┬──────┘
                            │   │
                 ┌──────────┘   └──────────┐
                 ▼                         ▼
          ┌─────────────┐          ┌─────────────┐
          │    React    │          │   FastAPI   │
          │  Dashboard  │          │     API     │
          └─────────────┘          └──────┬──────┘
                                          │
                         ┌────────────────┼────────────────┐
                         ▼                ▼                ▼
                  ┌────────────┐   ┌────────────┐   ┌────────────┐
                  │ PostgreSQL │   │   Redis    │   │  PowerDNS  │
                  └────────────┘   └────────────┘   └─────┬──────┘
                                                           │
                                                           ▼
                                                      DNS :53

---

📁 ساختار پروژه

PersonalDNS/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── powerdns/
│   └── pdns.conf
│
├── nginx/
│   └── nginx.conf
│
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/
│
├── docker-compose.yml
├── README.md
└── LICENSE

---

⚡ نصب سریع

git clone https://github.com/amirhazbavi/PersonalDNS.git

cd PersonalDNS

cp backend/.env.example backend/.env

docker compose up -d --build

---

🌐 سرویس‌ها

سرویس| آدرس
🖥️ Dashboard| "http://localhost:3000"
⚙️ API| "http://localhost:8000"
📚 Swagger| "http://localhost:8000/docs"

---

🔌 API

نمونه Endpointها:

POST   /api/auth/register
POST   /api/auth/login

GET    /api/domains
POST   /api/domains
DELETE /api/domains/{id}

GET    /api/domains/{id}/records
POST   /api/domains/{id}/records

PUT    /api/records/{id}
DELETE /api/records/{id}

---

🔐 امنیت

PersonalDNS برای محیط چندکاربره با قابلیت‌های امنیتی زیر طراحی می‌شود:

- JWT Authentication
- Password Hashing
- API Keys
- Role-Based Access Control
- Rate Limiting
- Input Validation
- Audit Logs
- مدیریت Secretها با Environment Variables
- محدودسازی دسترسی PowerDNS API
- پشتیبانی از HTTPS در محیط Production

«🔒 هیچ Secret یا API Key واقعی را داخل Repository قرار ندهید.»

---

🌍 DNS واقعی

برای استفاده از PersonalDNS به‌عنوان Authoritative DNS، باید Nameserverهای دامنه به سرور DNS شما اشاره کنند.

نمونه:

ns1.example.com → SERVER_IP
ns2.example.com → SERVER_IP

همچنین در رجیسترار دامنه، در صورت نیاز باید Glue Record مربوط به Nameserverها ایجاد شود.

«⚠️ GitHub Pages برای اجرای Authoritative DNS روی پورت 53 طراحی نشده است. برای DNS واقعی به یک سرور عمومی یا زیرساخت DNS مناسب نیاز دارید.»

---

📊 Monitoring

زیرساخت مانیتورینگ:

PowerDNS
   │
   ▼
Prometheus
   │
   ▼
Grafana
   │
   ▼
📈 Metrics

---

⚙️ Environment Variables

نمونه:

DATABASE_URL=postgresql://user:password@postgres:5432/personaldns

REDIS_URL=redis://redis:6379

SECRET_KEY=CHANGE_ME

POWERDNS_API_URL=http://powerdns:8081

POWERDNS_API_KEY=CHANGE_ME

---

🛠️ Production Checklist

- [ ] تنظیم دامنه اصلی
- [ ] تنظیم SSL/TLS
- [ ] تنظیم Nameserver
- [ ] تنظیم Glue Records
- [ ] تنظیم PowerDNS
- [ ] تنظیم PostgreSQL
- [ ] تنظیم Backup
- [ ] تنظیم Redis
- [ ] فعال‌سازی DNSSEC
- [ ] تنظیم Firewall
- [ ] محدودسازی API
- [ ] تنظیم Monitoring
- [ ] تست DNS
- [ ] تست Failover

---

📜 License

این پروژه تحت مجوز MIT منتشر شده است.

---

🔗 Repository

""GitHub Repository" (https://img.shields.io/badge/GitHub-PersonalDNS-black?logo=github&logoColor=white)" (https://github.com/amirhazbavi/PersonalDNS)

"مشاهده مخزن PersonalDNS" (https://github.com/amirhazbavi/PersonalDNS)

---

<p align="center">🟣 PersonalDNS © 2026

Multi-User DNS Management Platform

</p>
