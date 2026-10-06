<div dir="rtl">🟣 PersonalDNS

🚀 پلتفرم مدیریت DNS شخصی، سریع و چندکاربره برای ایران 🇮🇷

PersonalDNS یک پلتفرم مدیریت DNS چندکاربره است که برای مدیریت متمرکز دامنه‌ها، Zoneها، رکوردهای DNS، کاربران، API، امنیت و مانیتورینگ طراحی شده است.

هدف پروژه این است که مدیریت DNS از طریق یک پنل مدرن، فارسی، سریع و قابل توسعه انجام شود.

</div>---

<div align="center">""GitHub" (https://img.shields.io/badge/GitHub-PersonalDNS-181717?style=for-the-badge&logo=github&logoColor=white)" (https://github.com/amirhazbavi/PersonalDNS)
""License" (https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)" (LICENSE)
""Backend" (https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)" (https://fastapi.tiangolo.com/)
""Frontend" (https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=111827)" (https://react.dev/)
""Docker" (https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)" (https://www.docker.com/)

⚡ Fast • 🔐 Secure • 🌐 Scalable • 🇮🇷 Persian / RTL

</div>---

📖 فهرست مطالب

- "PersonalDNS چیست؟" (#-personaldns-چیست)
- "این برنامه چه کاری انجام می‌دهد؟" (#-این-برنامه-چه-کاری-انجام-میدهد)
- "نحوه کار" (#-نحوه-کار)
- "امکانات" (#-امکانات)
- "رکوردهای DNS" (#-رکوردهای-dns)
- "کاربران و دسترسی‌ها" (#-کاربران-و-دسترسیها)
- "معماری" (#-معماری)
- "تکنولوژی‌ها" (#-تکنولوژیها)
- "ساختار پروژه" (#-ساختار-پروژه)
- "پیش‌نیازها" (#-پیشنیازها)
- "نصب سریع" (#-نصب-سریع)
- "نصب کامل روی VPS" (#-نصب-کامل-روی-vps)
- "تنظیم Environment" (#-تنظیم-environment)
- "اجرای Docker" (#-اجرای-docker)
- "تنظیم دامنه" (#-تنظیم-دامنه)
- "راه‌اندازی DNS واقعی" (#-راهاندازی-dns-واقعی)
- "تست DNS" (#-تست-dns)
- "API" (#-api)
- "امنیت" (#-امنیت)
- "DNSSEC" (#-dnssec)
- "Backup" (#-backup)
- "Monitoring" (#-monitoring)
- "عیب‌یابی" (#-عیبیابی)
- "Roadmap" (#-roadmap)
- "مشارکت" (#-مشارکت)
- "License" (#-license)

---

🟣 PersonalDNS چیست؟

PersonalDNS یک سیستم مدیریت DNS است که یک پنل مدیریتی را به یک DNS Authoritative Server متصل می‌کند.

در یک پروژه واقعی، ساختار کلی به این شکل است:

                     🌐 Internet
                          │
                          ▼
                  ┌────────────────┐
                  │ Domain / DNS   │
                  │    Clients     │
                  └───────┬────────┘
                          │
                          ▼
                  ┌────────────────┐
                  │   PersonalDNS  │
                  │    Dashboard   │
                  └───────┬────────┘
                          │
                          ▼
                     ┌─────────┐
                     │ FastAPI │
                     └────┬────┘
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
        PostgreSQL      Redis      PowerDNS
                                      │
                                      ▼
                                   DNS :53

---

🎯 این برنامه چه کاری انجام می‌دهد؟

فرض کنید یک دامنه دارید:

example.com

به‌جای اینکه مستقیماً فایل‌های DNS یا تنظیمات پیچیده سرور را مدیریت کنید، وارد PersonalDNS می‌شوید.

مثلاً یک رکورد ایجاد می‌کنید:

Type: A
Name: www
Value: 1.2.3.4
TTL: 3600

PersonalDNS این اطلاعات را مدیریت می‌کند و در معماری واقعی آن را به PowerDNS منتقل می‌کند.

در نتیجه:

www.example.com
       │
       ▼
    DNS Query
       │
       ▼
   PowerDNS
       │
       ▼
    1.2.3.4

بنابراین PersonalDNS فقط یک صفحه ظاهری نیست؛ در صورت اتصال صحیح به PowerDNS و زیرساخت عمومی، می‌تواند رابط مدیریت یک DNS Authoritative واقعی باشد.

---

🌐 DNS Authoritative چیست؟

DNS Authoritative سرویسی است که اطلاعات معتبر یک دامنه را نگهداری می‌کند.

مثلاً:

example.com

ممکن است رکوردهای زیر را داشته باشد:

example.com       A       1.2.3.4
www.example.com   A       1.2.3.4
mail.example.com  A       1.2.3.5
example.com       MX      mail.example.com

وقتی Resolver درخواست DNS ارسال می‌کند، Nameserverهای Authoritative می‌توانند پاسخ معتبر دامنه را ارائه کنند.

---

✨ امکانات

🌐 مدیریت دامنه

- افزودن دامنه
- حذف دامنه
- مشاهده وضعیت دامنه
- مدیریت Zone
- مدیریت Nameserver
- مدیریت رکوردها
- بررسی وضعیت DNS

---

📋 مدیریت رکوردها

پشتیبانی معماری پروژه برای رکوردهای رایج:

- "A"
- "AAAA"
- "CNAME"
- "MX"
- "TXT"
- "NS"
- "CAA"
- "SRV"

هر رکورد می‌تواند شامل مواردی مانند:

Name
Type
Content
TTL
Priority

باشد.

---

👥 سیستم چندکاربره

PersonalDNS برای استفاده توسط چند کاربر طراحی شده است.

مثلاً:

👤 Amir
├── example.com
└── amir.ir

👤 Ali
├── ali.com
└── test.net

👤 Reza
└── reza.ir

هر کاربر باید فقط به منابعی که مجوز مدیریت آن‌ها را دارد دسترسی داشته باشد.

---

👑 سیستم نقش‌ها

معماری سیستم می‌تواند نقش‌هایی مانند موارد زیر داشته باشد:

نقش| دسترسی
"User"| مدیریت منابع خودش
"Manager"| مدیریت منابع اختصاص‌یافته
"Admin"| مدیریت کاربران و سیستم
"SuperAdmin"| دسترسی کامل

---

🔐 احراز هویت

PersonalDNS برای API و پنل می‌تواند از:

- JWT
- Password Hashing
- API Keys
- Session Management
- Role-Based Access Control

استفاده کند.

---

🔑 API Keys

کاربر می‌تواند برای اتوماسیون یک API Key ایجاد کند.

مثلاً:

PersonalDNS
     │
     ▼
API Key
     │
     ▼
Automation
     │
     ▼
DNS Management

API Key واقعی نباید داخل Repository عمومی قرار بگیرد.

---

📊 داشبورد

داشبورد می‌تواند اطلاعاتی مانند:

┌─────────────────────────────────────────────┐
│             🟣 PersonalDNS                  │
├─────────────┬─────────────┬─────────────────┤
│   Domains   │   Records   │    Users        │
│     12      │     84      │      25         │
├─────────────┴─────────────┴─────────────────┤
│                                             │
│              DNS Statistics                 │
│                                             │
│       Queries     Errors     Latency        │
│         24K         12         ...          │
│                                             │
└─────────────────────────────────────────────┘

را نمایش دهد.

---

📋 رکوردهای DNS

Record| کاربرد
"A"| آدرس IPv4
"AAAA"| آدرس IPv6
"CNAME"| نام مستعار
"MX"| Mail Server
"TXT"| متن، SPF و Verification
"NS"| Nameserver
"CAA"| Certificate Authority
"SRV"| Service Discovery

---

🧠 نحوه کار سیستم

وقتی کاربر یک رکورد ایجاد می‌کند:

        👤 User
          │
          ▼
    React Dashboard
          │
          ▼
      FastAPI API
          │
          ├──────────────► PostgreSQL
          │
          ├──────────────► Redis
          │
          ▼
       PowerDNS API
          │
          ▼
       DNS Zone
          │
          ▼
       DNS :53

این جداسازی باعث می‌شود پنل مدیریت، دیتابیس و DNS Server از یکدیگر جدا باشند.

---

🏗️ معماری کامل

                           🌐 INTERNET
                                │
                ┌───────────────┴───────────────┐
                │                               │
                ▼                               ▼
          Web Browser                       DNS Clients
                │                               │
                ▼                               ▼
             HTTPS                         UDP/TCP 53
                │                               │
                ▼                               ▼
          ┌──────────┐                    ┌──────────┐
          │  Nginx   │                    │ PowerDNS │
          └────┬─────┘                    └────┬─────┘
               │                               │
          ┌────┴────┐                          │
          ▼         ▼                          │
       React     FastAPI ◄─────────────────────┘
                    │
          ┌─────────┼──────────┐
          ▼         ▼          ▼
     PostgreSQL   Redis     Monitoring
                              │
                              ▼
                         Prometheus
                              │
                              ▼
                           Grafana

---

🛠️ تکنولوژی‌ها

بخش| تکنولوژی
Frontend| React + TypeScript
Backend| FastAPI + Python
DNS| PowerDNS Authoritative
Database| PostgreSQL
Cache| Redis
Reverse Proxy| Nginx
Monitoring| Prometheus + Grafana
Container| Docker
Orchestration| Docker Compose

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

💻 پیش‌نیازها

برای اجرای کامل روی اینترنت پیشنهاد می‌شود داشته باشید:

- Linux VPS یا Server
- IPv4 عمومی
- Docker
- Docker Compose
- Git
- یک Domain
- دسترسی SSH
- امکان بازکردن پورت "53/UDP"
- امکان بازکردن پورت "53/TCP"

برای تست محلی، VPS و IP عمومی ضروری نیست.

---

🚀 نصب سریع

1. دریافت پروژه

git clone https://github.com/amirhazbavi/PersonalDNS.git
cd PersonalDNS

---

2. ساخت فایل تنظیمات

cp backend/.env.example backend/.env

---

3. ویرایش تنظیمات

nano backend/.env

نمونه:

DATABASE_URL=postgresql://personaldns:CHANGE_ME@postgres:5432/personaldns

REDIS_URL=redis://redis:6379

SECRET_KEY=CHANGE_THIS_TO_A_LONG_RANDOM_SECRET

POWERDNS_API_URL=http://powerdns:8081

POWERDNS_API_KEY=CHANGE_ME

---

🐳 اجرای پروژه با Docker

docker compose up -d --build

بررسی سرویس‌ها:

docker compose ps

مشاهده Log:

docker compose logs -f

---

🌐 آدرس‌های محلی

بعد از اجرای موفق:

Dashboard

http://localhost:3000

Backend API

http://localhost:8000

Swagger

http://localhost:8000/docs

ReDoc

http://localhost:8000/redoc

---

🖥️ نصب کامل روی VPS

1. اتصال به VPS

ssh root@SERVER_IP

به‌جای:

SERVER_IP

IP واقعی VPS را وارد کنید.

---

📦 نصب Git

برای Ubuntu/Debian:

apt update
apt install git curl -y

بررسی:

git --version

---

🐳 نصب Docker

curl -fsSL https://get.docker.com | sh

بررسی:

docker --version

بررسی Compose:

docker compose version

---

📥 دریافت PersonalDNS

git clone https://github.com/amirhazbavi/PersonalDNS.git

سپس:

cd PersonalDNS

---

⚙️ تنظیم Environment

cp backend/.env.example backend/.env
nano backend/.env

نمونه:

DATABASE_URL=postgresql://personaldns:CHANGE_ME@postgres:5432/personaldns

REDIS_URL=redis://redis:6379

SECRET_KEY=CHANGE_ME

POWERDNS_API_URL=http://powerdns:8081

POWERDNS_API_KEY=CHANGE_ME

🔒 نکته امنیتی

مقادیر زیر را عمومی نکنید:

SECRET_KEY
DATABASE_PASSWORD
POWERDNS_API_KEY
API_KEYS

و فایل ".env" را Commit نکنید.

---

🔥 تنظیم Firewall

DNS به هر دو پروتکل نیاز دارد:

UDP 53
TCP 53

اگر UFW دارید:

ufw allow 53/udp
ufw allow 53/tcp

برای SSH:

ufw allow 22/tcp

برای HTTP:

ufw allow 80/tcp

برای HTTPS:

ufw allow 443/tcp

سپس:

ufw enable

«علاوه بر UFW، Firewall پنل VPS یا Cloud Provider را نیز بررسی کنید.»

---

🌍 اتصال دامنه

فرض کنید دامنه شما:

example.com

و IP سرور:

1.2.3.4

Nameserverها:

ns1.example.com
ns2.example.com

هستند.

در Registrar باید در صورت نیاز Glue Record ایجاد شود:

ns1.example.com → 1.2.3.4
ns2.example.com → 1.2.3.4

سپس Nameserver دامنه را روی:

ns1.example.com
ns2.example.com

قرار دهید.

---

⚠️ DNS واقعی

برای اینکه PersonalDNS واقعاً DNS دامنه را سرو کند، مسیر زیر باید درست باشد:

Domain
   │
   ▼
Registrar
   │
   ▼
NS Records
   │
   ▼
Public IP
   │
   ▼
Firewall
   │
   ▼
Port 53
   │
   ▼
PowerDNS
   │
   ▼
PersonalDNS

صرفاً اجرای سایت یا GitHub Pages باعث فعال‌شدن DNS واقعی نمی‌شود.

---

🧪 تست DNS

بعد از تنظیم Nameserver:

dig example.com

یا:

dig @SERVER_IP example.com

رکورد A:

dig @SERVER_IP example.com A

رکورد MX:

dig @SERVER_IP example.com MX

رکورد TXT:

dig @SERVER_IP example.com TXT

---

🔄 مدیریت Docker

اجرا

docker compose up -d

توقف

docker compose down

Restart

docker compose restart

Build مجدد

docker compose up -d --build

مشاهده وضعیت

docker compose ps

مشاهده Log

docker compose logs -f

---

🔌 API

PersonalDNS می‌تواند API مرکزی برای مدیریت DNS داشته باشد.

Authentication

POST /api/auth/register
POST /api/auth/login

Domains

GET /api/domains
POST /api/domains
GET /api/domains/{id}
DELETE /api/domains/{id}

Records

GET /api/domains/{id}/records
POST /api/domains/{id}/records
PUT /api/records/{id}
DELETE /api/records/{id}

Health

GET /health

Swagger:

http://SERVER_IP:8000/docs

---

🔐 امنیت

برای Production موارد زیر باید رعایت شوند:

- استفاده از HTTPS
- Secretهای قوی
- Hash کردن Passwordها
- JWT امن
- API Keyهای امن
- Rate Limiting
- Validation
- RBAC
- Audit Logs
- محدودکردن دسترسی PowerDNS API
- Firewall
- Backup
- عدم قرار دادن Secret در Git
- عدم قرار دادن PostgreSQL روی اینترنت عمومی

---

🔐 PowerDNS API

PowerDNS API باید تا حد امکان فقط داخل شبکه داخلی Docker قابل دسترسی باشد.

ساختار پیشنهادی:

Internet
   │
   ├── HTTPS :443 ──► Nginx
   │
   └── DNS :53 ─────► PowerDNS
                         ▲
                         │
                    Internal API
                         │
                      FastAPI

PowerDNS API نباید بدون نیاز روی اینترنت عمومی قرار بگیرد.

---

🔐 DNSSEC

DNSSEC برای افزایش اعتبار و امنیت پاسخ‌های DNS استفاده می‌شود.

ساختار کلی:

Domain
   │
   ▼
DNSSEC
   │
   ├── DNSKEY
   ├── RRSIG
   └── DS

فعال‌سازی کامل DNSSEC به تنظیمات واقعی PowerDNS، Zoneها و Registrar وابسته است.

---

📊 Monitoring

PersonalDNS می‌تواند با Prometheus و Grafana مانیتور شود.

PersonalDNS
     │
     ├── API Metrics
     ├── Database Metrics
     ├── DNS Metrics
     └── System Metrics
              │
              ▼
         Prometheus
              │
              ▼
           Grafana

موارد قابل مانیتور:

- تعداد درخواست‌ها
- خطاها
- وضعیت API
- وضعیت DNS
- مصرف منابع
- Latency
- وضعیت Database

---

💾 Backup

برای Backup PostgreSQL:

docker compose exec postgres \
pg_dump -U personaldns personaldns > backup.sql

برای Restore:

cat backup.sql | \
docker compose exec -T postgres \
psql -U personaldns personaldns

«نام کاربر و Database باید با "docker-compose.yml" واقعی پروژه یکسان باشد.»

---

🧹 حذف پروژه

برای متوقف‌کردن سرویس‌ها:

docker compose down

برای حذف Volumeها:

docker compose down -v

«⚠️ "down -v" می‌تواند داده‌های موجود در Docker Volumeها را حذف کند. قبل از اجرای آن Backup بگیرید.»

---

🛠️ عیب‌یابی

Docker اجرا نمی‌شود

docker --version
docker compose version

سپس:

docker compose ps

---

Backend اجرا نمی‌شود

docker compose logs backend

فایل Environment را بررسی کنید:

cat backend/.env

---

Frontend باز نمی‌شود

docker compose logs frontend

و:

docker compose ps

---

PowerDNS اجرا نمی‌شود

docker compose logs powerdns

همچنین:

docker compose ps powerdns

---

DNS پاسخ نمی‌دهد

ابتدا پورت‌ها:

ufw status

سپس:

dig @SERVER_IP example.com

و Logهای PowerDNS:

docker compose logs -f powerdns

---

📱 رابط کاربری

PersonalDNS برای استفاده در:

- 💻 Desktop
- 💻 Laptop
- 📱 Mobile
- 📱 Tablet

طراحی می‌شود.

رابط فارسی:

RTL

و رابط انگلیسی:

LTR

می‌تواند پشتیبانی شود.

---

🇮🇷 تمرکز روی ایران

PersonalDNS برای کاربران فارسی‌زبان می‌تواند شامل موارد زیر باشد:

- 🇮🇷 رابط فارسی
- ↔️ RTL
- 💰 نمایش قیمت به تومان
- 📱 طراحی Mobile First
- 🌐 پشتیبانی از دامنه‌های مختلف
- 🔌 معماری قابل اتصال به Registrarهای مختلف
- 🧾 آماده توسعه سیستم Billing

«اتصال واقعی به Registrar یا Payment Gateway به API رسمی آن سرویس نیاز دارد و نباید بدون مستندات رسمی ادعا شود که اتصال فعال است.»

---

📈 کارایی و مقیاس‌پذیری

PersonalDNS با معماری جداشده طراحی شده است:

Frontend
    │
    ▼
Backend
    │
    ├── Database
    ├── Cache
    └── DNS

این ساختار امکان توسعه برای:

- چندین کاربر
- تعداد زیاد دامنه
- تعداد زیاد رکورد
- چند DNS Server
- Load Balancing
- High Availability

را فراهم می‌کند.

«⚠️ سرعت و ظرفیت واقعی به سخت‌افزار، شبکه، تنظیمات PowerDNS، Database و معماری Deployment بستگی دارد و نباید عدد عملکردی خاصی بدون Benchmark واقعی تضمین شود.»

---

🗺️ Roadmap

Phase 1

- [x] معماری اولیه
- [x] طراحی Backend
- [x] طراحی Frontend
- [x] Docker Architecture

Phase 2

- [ ] User Authentication
- [ ] Domain Management
- [ ] DNS Record Management
- [ ] PowerDNS Integration

Phase 3

- [ ] DNSSEC
- [ ] API Keys
- [ ] Audit Logs
- [ ] Advanced Permissions

Phase 4

- [ ] Monitoring
- [ ] Analytics
- [ ] Backup System
- [ ] Notifications

Phase 5

- [ ] Billing
- [ ] Subscription
- [ ] Registrar Adapters
- [ ] Multi-Server DNS

Phase 6

- [ ] High Availability
- [ ] Multiple DNS Nodes
- [ ] Automatic Failover
- [ ] Global DNS Infrastructure

---

🤝 مشارکت

برای مشارکت:

git clone https://github.com/amirhazbavi/PersonalDNS.git

cd PersonalDNS

git checkout -b feature/my-feature

پس از تغییرات:

git add .
git commit -m "Add new feature"
git push origin feature/my-feature

سپس Pull Request ایجاد کنید.

---

🐛 گزارش مشکل

اگر مشکلی پیدا کردید، در GitHub Issues گزارش دهید:

Repository:

https://github.com/amirhazbavi/PersonalDNS

Issues:

https://github.com/amirhazbavi/PersonalDNS/issues

هنگام گزارش Bug بهتر است موارد زیر را اضافه کنید:

OS:
Docker Version:
Docker Compose Version:
Browser:
Error:
Steps to Reproduce:
Logs:

---

📜 License

PersonalDNS تحت مجوز MIT منتشر شده است.

---

🔗 لینک‌های پروژه

📦 GitHub

""GitHub" (https://img.shields.io/badge/GitHub-PersonalDNS-181717?style=for-the-badge&logo=github&logoColor=white)" (https://github.com/amirhazbavi/PersonalDNS)

🐛 Issues

""Issues" (https://img.shields.io/badge/GitHub-Issues-e11d48?style=for-the-badge&logo=github&logoColor=white)" (https://github.com/amirhazbavi/PersonalDNS/issues)

---

<div align="center">🟣 PersonalDNS

Personal DNS Management Platform

⚡ Fast • 🔐 Secure • 🌐 Scalable • 🇮🇷 Persian / RTL

<br>Built for modern DNS management.

<br>PersonalDNS © 2026

</div>
