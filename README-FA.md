

<p align="center">
  <a href="https://github.com/sina-nozhati/foxybot" target="_blank" rel="noopener noreferrer">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/icon.png?raw=True">
      <img width="200" height="200" src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/icon.png?raw=True">
    </picture>
  </a>
</p>
<p align="center">
	<a href="./README.md">
	English
	</a>
	|
	<a href="./README-FA.md">
	فارسی
	</a>
<br>
  <a href="https://t.me/HidyBotGroup">گروه تلگرام</a>

</p>

<h1 align="center"/>فاکسی بات (Foxy Bot)</h1>

با استفاده از این ربات می‌توانید پنل هیدیفای خود را از طریق تلگرام مدیریت کنید.

## ⚠️ مهم: به‌روزرسانی API v2

این ربات برای پشتیبانی از **Hiddify Panel API v2** به‌روز شده است. اگر در حال ارتقا از نسخه قدیمی هستید، لطفاً [راهنمای مهاجرت](MIGRATION_GUIDE.md) را بخوانید.

### فرمت جدید آدرس پنل
```
https://your-domain.com/proxy_path/admin_uuid/

مثال:
https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/
```

## ویژگی‌ها
-  مدیریت چند پنل
-  فروش کانفیگ
-  افزودن کاربران
-  حذف کاربران
-  ویرایش کاربران
-  نمایش لیست کاربران
-  جستجوی کاربران (بر اساس نام، تنظیمات، UUID)
-  نمایش اطلاعات کاربران (نام، ترافیک، تاریخ و غیره)
-  نمایش پیکربندی‌ها و لینک‌های اشتراک کاربر
-  دریافت پشتیبان از پنل شما + ارسال خودکار
-  نمایش وضعیت سرور (رم، پردازنده، دیسک)
- چند زبانه (انگلیسی، فارسی)
- ربات کاربران
- **جدید: پشتیبانی از API v2 با احراز هویت مبتنی بر هدر**

## نصب 
برای نصب ربات دستور زیر را اجرا کنید:
 
```bash
sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
```
<br>

مطمئن شوید که اطلاعات زیر را آماده دارید:
1. `شناسه تلگرام ادمین` : آن را از ربات[ User Info Bot](https://t.me/userinfobot) بگیرید (مثال: `123456789`)
2. `توکن ربات ادمین` : آن را از ربات [BotFather](https://t.me/BotFather) بگیرید (
   مثال: `1234567890:ABCdEfGhIjKlMnOpQrStUvWxYz`)
3. `توکن ربات کاربران` : آن را از ربات [BotFather](https://t.me/BotFather) بگیرید (
   مثال: `1234567890:ABCdEfGhIjKlMnOpQrStUvWxYz`)
4. `آدرس پنل هیدیفای` : آدرس پنل هیدیفای خود را وارد کنید (
   مثال: `https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/`)
5. `زبان ربات` : گزینه‌ها `en` و `fa` می‌باشند [پیش‌فرض `fa`]

حالا می‌توانید با ارسال دستور `/start` از ربات در تلگرام استفاده کنید.

## تست نصب

بعد از نصب، اتصال API را تست کنید:

```bash
cd /opt/Hiddify-Telegram-Bot/
python3 test_api_v2.py "https://your-domain.com/proxy_path/admin_uuid/"
```

همه تست‌ها باید موفق باشند ✅

## دستورات

### به‌روزرسانی ربات
```bash
cd /opt/Hiddify-Telegram-Bot/ && curl -fsSL -o /opt/Hiddify-Telegram-Bot/update.sh https://raw.githubusercontent.com/sina-nozhati/foxybot/main/update.sh && chmod +x /opt/Hiddify-Telegram-Bot/update.sh && bash /opt/Hiddify-Telegram-Bot/update.sh
```

### راه‌اندازی مجدد ربات
```bash
cd /opt/Hiddify-Telegram-Bot/ && chmod +x restart.sh && ./restart.sh
```

### متوقف کردن ربات
```bash
pkill -9 -f hiddifyTelegramBot.py
```

### مشاهده لاگ‌های ربات
```bash
cat /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
```

### مشاهده و تغییر پیکربندی ربات
```bash
cd /opt/Hiddify-Telegram-Bot/ && python3 config.py && chmod +x restart.sh && ./restart.sh
```

### نصب مجدد ربات
```bash
cd /opt/ && rm -rf /opt/Hiddify-Telegram-Bot/ && sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
```

### حذف ربات
```bash
cd /opt/Hiddify-Telegram-Bot/ && chmod +x uninstall.sh && ./uninstall.sh
```

## مستندات

- **[README_API_V2.md](README_API_V2.md)** - راهنمای سریع برای API v2
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - راهنمای مرحله به مرحله مهاجرت
- **[API_QUICK_REFERENCE.md](API_QUICK_REFERENCE.md)** - مرجع توسعه‌دهنده
- **[UPDATE_CHECKLIST.md](UPDATE_CHECKLIST.md)** - چک‌لیست تأیید

## نیازمندی‌ها

- Hiddify Panel v2.x یا بالاتر
- Python 3.7+
- سرور لینوکس (Ubuntu 20.04+, Debian 10+, CentOS 7+)

## عیب‌یابی

اگر با مشکل مواجه شدید:

1. **بررسی لاگ‌ها:**
   ```bash
   tail -100 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
   ```

2. **تست اتصال API:**
   ```bash
   python3 test_api_v2.py "your-panel-url"
   ```

3. **مطالعه مستندات:**
   - [راهنمای به‌روزرسانی API v2](API_V2_UPDATE_GUIDE.md)
   - [راهنمای مهاجرت](MIGRATION_GUIDE.md)

4. **عضویت در گروه پشتیبانی:** [@HidyBotGroup](https://t.me/HidyBotGroup)

## اسکرین شات‌ها
#### ربات کاربران 
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-1.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-2.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-3.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-4.jpg?raw=True" width=35% height=35%>
#### ربات ادمین
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-1.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-2.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-6.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-8.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-5.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-3.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-4.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-7.jpg?raw=True" width=35% height=35%>

## مشارکت

مشارکت شما استقبال می‌شود! لطفاً برای ارسال Pull Request احساس راحتی کنید.

## مجوز

این پروژه متن‌باز است. برای جزئیات به فایل LICENSE مراجعه کنید.

## پشتیبانی

- **گروه تلگرام:** [@HidyBotGroup](https://t.me/HidyBotGroup)
- **مشکلات:** [GitHub Issues](https://github.com/sina-nozhati/foxybot/issues)
- **مستندات:** [مستندات](.) در این مخزن را ببینید
