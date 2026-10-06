🌐 PersonalDNS

قوی‌ترین و سریع‌ترین پلتفرم مدیریت DNS شخصی چندکاربره برای ایران 🇮🇷

""GitHub" (https://img.shields.io/badge/GitHub-PersonalDNS-black?logo=github)" (https://github.com/amirhazbavi/PersonalDNS)
""License" (https://img.shields.io/badge/License-MIT-green.svg)" (LICENSE)
""Backend" (https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)" (https://fastapi.tiangolo.com/)
""Frontend" (https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)" (https://react.dev/)
""Docker" (https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)" (https://www.docker.com/)

PersonalDNS یک پلتفرم مدیریت DNS چندکاربره است که امکان مدیریت دامنه‌ها، Zoneها و رکوردهای DNS را از طریق یک پنل مدرن فراهم می‌کند.

---

🚀 امکانات

🌐 DNS واقعی

- ✅ PowerDNS Authoritative Server
- ✅ PostgreSQL Backend
- ✅ مدیریت Zone
- ✅ مدیریت رکوردهای DNS
- ✅ A Record
- ✅ AAAA Record
- ✅ CNAME Record
- ✅ MX Record
- ✅ TXT Record
- ✅ NS Record
- ✅ CAA Record
- ✅ SRV Record
- ✅ DNSSEC Ready
- ✅ REST API
- ✅ Real-Time Zone Updates

---

⚡ Performance

- Redis Cache
- Nginx Reverse Proxy
- Async FastAPI
- Connection Pooling
- Health Checks
- Load Balancing Ready
- CDN Ready
- Docker Ready
- Kubernetes Ready

«سرعت واقعی DNS به سرور، شبکه، فاصله کاربر، Cache و تنظیمات DNS بستگی دارد و اعداد Performance باید با Benchmark واقعی اندازه‌گیری شوند.»

---

🎨 Frontend

- React 18
- TypeScript
- Vite
- TailwindCSS
- DaisyUI
- Dark Mode
- Light Mode
- RTL
- LTR
- فارسی
- Responsive
- Mobile First
- Dashboard
- Real-Time Notifications

---

🔧 Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- RabbitMQ Ready
- JWT Authentication
- OAuth2 Ready
- API Keys
- Rate Limiting
- Audit Logging

---

🔐 امنیت

PersonalDNS با تمرکز روی امنیت طراحی شده است.

- 🔒 Password Hashing
- 🔒 JWT Authentication
- 🔒 API Key Management
- 🔒 HTTPS / TLS
- 🔒 CORS Protection
- 🔒 Rate Limiting
- 🔒 SQL Injection Protection
- 🔒 XSS Protection
- 🔒 CSRF Protection
- 🔒 Audit Logs
- 🔒 Session Security
- 🔒 API Key Rotation
- 🔒 2FA Ready

⚠️ مهم

هیچ Password، API Key، JWT Secret یا Database Credential واقعی نباید داخل Repository عمومی قرار بگیرد.

---

📊 Monitoring

قابلیت اتصال به:

- Prometheus
- Grafana
- Alertmanager
- DNS Query Statistics
- API Metrics
- CPU Monitoring
- RAM Monitoring
- Error Tracking
- Health Checks

---

🇮🇷 امکانات مخصوص ایران

- 🇮🇷 رابط کاربری فارسی
- 🇮🇷 RTL
- 🇮🇷 قیمت‌گذاری تومانی
- 🇮🇷 آماده اتصال به درگاه پرداخت
- 🇮🇷 آماده اتصال به Registrar
- 🇮🇷 مناسب برای VPSهای ایران
- 🇮🇷 قابلیت توسعه برای سرویس‌های ثبت دامنه ایرانی

«اتصال واقعی به Registrarها نیازمند API رسمی و مجوز استفاده از سرویس مربوطه است.»

---

🏗️ Architecture

                    ┌──────────────────────┐
                    │       Frontend       │
                    │   React + TypeScript  │
                    └──────────┬───────────┘
                               │ HTTPS
                               ▼
                    ┌──────────────────────┐
                    │        Nginx         │
                    │ Reverse Proxy / LB    │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                 ▼             ▼             ▼
            ┌─────────┐   ┌─────────┐   ┌─────────┐
            │Backend 1│   │Backend 2│   │Backend 3│
            │ FastAPI │   │ FastAPI │   │ FastAPI │
            └────┬────┘   └────┬────┘   └────┬────┘
                 │             │             │
                 └─────────────┼─────────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                 ▼             ▼             ▼
            ┌──────────┐ ┌──────────┐ ┌──────────┐
            │PostgreSQL│ │  Redis   │ │ RabbitMQ │
            └────┬─────┘ └──────────┘ └──────────┘
                 │
                 ▼
          ┌──────────────────┐
          │    PowerDNS      │
          │ Authoritative DNS│
          └────────┬─────────┘
                   │
                   ▼
              Internet DNS

---

📁 ساختار پروژه

PersonalDNS/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy.yml
│       └── security.yml
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── auth.py
│   │   │   │   ├── domains.py
│   │   │   │   ├── records.py
│   │   │   │   ├── dns_lookup.py
│   │   │   │   ├── api_keys.py
│   │   │   │   ├── admin.py
│   │   │   │   └── webhooks.py
│   │   │   ├── deps.py
│   │   │   └── errors.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   ├── db.py
│   │   │   ├── cache.py
│   │   │   ├── logging.py
│   │   │   └── celery.py
│   │   │
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env.example
│   └── alembic.ini
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   │
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── Dockerfile
│   └── .env.example
│
├── powerdns/
│   ├── pdns.conf
│   ├── schema.sql
│   ├── Dockerfile
│   └── init-db.sh
│
├── nginx/
│   ├── default.conf
│   ├── api.conf
│   ├── Dockerfile
│   └── ssl-params.conf
│
├── monitoring/
│   ├── prometheus.yml
│   ├── grafana/
│   └── alertmanager.yml
│
├── kubernetes/
│   ├── backend-deployment.yaml
│   ├── powerdns-deployment.yaml
│   ├── nginx-deployment.yaml
│   ├── postgres-statefulset.yaml
│   ├── redis-deployment.yaml
│   └── services.yaml
│
├── docker-compose.yml
├── docker-compose.prod.yml
├── Makefile
├── LICENSE
└── README.md

---

⚡ Quick Start

پیش‌نیازها

- Docker
- Docker Compose
- Git
- حداقل 2GB RAM
- پیشنهاد: 4GB تا 8GB RAM
- پورت 53
- پورت 80
- پورت 443

---

📥 دریافت پروژه

git clone https://github.com/amirhazbavi/PersonalDNS.git
cd PersonalDNS

---

⚙️ تنظیم Environment

cp backend/.env.example backend/.env

سپس Secretهای واقعی را داخل ".env" قرار دهید.

---

🐳 اجرای پروژه

docker compose up -d --build

بررسی وضعیت:

docker compose ps

مشاهده Log:

docker compose logs -f

مشاهده Log Backend:

docker compose logs -f backend

---

🌐 آدرس‌های Local

Frontend
http://localhost:3000

Backend
http://localhost:8000

FastAPI Swagger
http://localhost:8000/docs

---

🔌 API

نمونه Endpointها:

POST   /api/auth/register
POST   /api/auth/login

GET    /api/domains
POST   /api/domains

GET    /api/domains/{id}
DELETE /api/domains/{id}

GET    /api/domains/{id}/records
POST   /api/domains/{id}/records

PUT    /api/records/{id}
DELETE /api/records/{id}

GET    /api/dns/lookup

GET    /api/api-keys
POST   /api/api-keys
DELETE /api/api-keys/{id}

---

🌍 Production

برای DNS واقعی به یک سرور با IP عمومی و دسترسی مناسب به پورت 53 نیاز است.

نمونه:

ns1.example.com → SERVER_IP
ns2.example.com → SERVER_IP

سپس Nameserverها باید در Registrar دامنه تنظیم شوند.

---

🔐 Environment Variables

نمونه:

DATABASE_URL=postgresql+asyncpg://user:password@postgres:5432/personaldns

REDIS_URL=redis://redis:6379/0

JWT_SECRET=CHANGE_THIS_TO_A_LONG_RANDOM_SECRET

POWERDNS_API_URL=http://powerdns:8081/api/v1/servers/localhost

POWERDNS_API_KEY=CHANGE_THIS_KEY

CORS_ORIGINS=https://example.com

⚠️ مقادیر بالا نمونه هستند.

---

🛡️ Production Security Checklist

قبل از استفاده Production:

- [ ] تغییر تمام Passwordهای پیش‌فرض
- [ ] تغییر JWT Secret
- [ ] تغییر PowerDNS API Key
- [ ] فعال‌سازی HTTPS
- [ ] تنظیم Firewall
- [ ] محدود کردن PowerDNS API
- [ ] فعال‌سازی Rate Limiting
- [ ] فعال‌سازی Backup
- [ ] فعال‌سازی Monitoring
- [ ] بررسی DNSSEC
- [ ] تست Disaster Recovery
- [ ] اجرای Security Audit

---

📈 Monitoring

در محیط Production می‌توان از این سرویس‌ها استفاده کرد:

Prometheus
Grafana
Alertmanager

---

🐛 گزارش خطا

برای گزارش Bug یا درخواست Feature از GitHub Issues استفاده کنید:

https://github.com/amirhazbavi/PersonalDNS/issues

---

💻 Repository

⭐ GitHub

https://github.com/amirhazbavi/PersonalDNS

---

🤝 Contributing

Pull Request و پیشنهادهای توسعه پروژه پذیرفته می‌شود.

git clone https://github.com/amirhazbavi/PersonalDNS.git

cd PersonalDNS

git checkout -b feature/my-feature

بعد از اعمال تغییرات:

git add .
git commit -m "Add new feature"
git push origin feature/my-feature

سپس Pull Request ایجاد کنید.

---

📄 License

این پروژه تحت مجوز MIT منتشر شده است.

---

🇮🇷 PersonalDNS

مدیریت DNS شخصی، سریع، امن و قابل توسعه.

🌐 GitHub:

https://github.com/amirhazbavi/PersonalDNS

🐛 Issues:

https://github.com/amirhazbavi/PersonalDNS/issues

---

PersonalDNS © 2026
