<p align="center">
  <a href="https://github.com/sina-nozhati/foxybot" target="_blank" rel="noopener noreferrer">
    <img width="200" height="200" src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/icon.png?raw=True" alt="Hidy Bot">
  </a>
</p>

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README-FA.md">فارسی</a>
<br>
  <a href="https://t.me/HidyBotGroup">Telegram Group</a>

</p>
<h1 align="center">Foxy Bot</h1>

Foxy Bot is a Telegram bot that allows you to manage your Hiddify panel directly from Telegram.

## ⚠️ Important: API v2 Update

This bot has been updated to support **Hiddify Panel API v2**. If you're upgrading from an older version, please read the [Migration Guide](MIGRATION_GUIDE.md).

### New Panel URL Format
```
https://your-domain.com/proxy_path/admin_uuid/

Example:
https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/
```

## Features
- [x] Multi panel support
- [x] Sell config
- [x] Add users
- [x] Remove users
- [x] Edit user details
- [x] View users list
- [x] Search users (by name, configuration, UUID)
- [x] Show user information (name, traffic, date, etc.)
- [x] Display user configs and subscription links
- [x] Get a backup of your panel + Auto send
- [x] View server status (RAM, CPU, disk)
- [x] Multi language (English, Persian)
- [x] Client bot
- [x] **NEW: API v2 support with header-based authentication**
- [x] and more...

## Installation

To install the bot, run the following command:

```bash
sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
```
<br>

Make sure you have the following information ready:

1. `Admin Telegram Number ID` : Get it from [User info bot](https://t.me/userinfobot) (Example: `123456789`)
2. `Admin Telegram Bot Token` : Get it from [BotFather](https://t.me/BotFather) (
   Example: `1234567890:ABCdEfGhIjKlMnOpQrStUvWxYz`)
3. `Client Telegram Bot Token` : Get it from [BotFather](https://t.me/BotFather) (
   Example: `1234567890:ABCdEfGhIjKlMnOpQrStUvWxYz`)
4. `Hiddify Panel URL` : The url of your Hiddify panel (
   Example: `https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/`)
5. `Bot Language` : Options are `en` and `fa` [default is `fa`]


Now you can use the bot in Telegram by sending the `/start` command.

## Testing Your Installation

After installation, test the API connection:

```bash
cd /opt/Hiddify-Telegram-Bot/
python3 test_api_v2.py "https://your-domain.com/proxy_path/admin_uuid/"
```

All tests should pass ✅

## Commands

- ### Update bot
```bash
cd /opt/Hiddify-Telegram-Bot/ && curl -fsSL -o /opt/Hiddify-Telegram-Bot/update.sh https://raw.githubusercontent.com/sina-nozhati/foxybot/main/update.sh && chmod +x /opt/Hiddify-Telegram-Bot/update.sh && bash /opt/Hiddify-Telegram-Bot/update.sh
```
- ### Restart bot
```bash
cd /opt/Hiddify-Telegram-Bot/ && chmod +x restart.sh && ./restart.sh
```
- ### Stop bot
```bash
pkill -9 -f hiddifyTelegramBot.py
```
- ### Get bot logs
```bash
cat /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
```
- ### Edit bot configs
```bash
cd /opt/Hiddify-Telegram-Bot/ && python3 config.py && chmod +x restart.sh && ./restart.sh
```
- ### Reinstall bot
```bash
cd /opt/ && rm -rf /opt/Hiddify-Telegram-Bot/ && sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
```
- ### Uninstall bot
```bash
cd /opt/Hiddify-Telegram-Bot/ && chmod +x uninstall.sh && ./uninstall.sh
```

## Documentation

- **[README_API_V2.md](README_API_V2.md)** - Quick start guide for API v2
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - Step-by-step migration from API v1
- **[API_QUICK_REFERENCE.md](API_QUICK_REFERENCE.md)** - Developer reference
- **[UPDATE_CHECKLIST.md](UPDATE_CHECKLIST.md)** - Verification checklist

## Requirements

- Hiddify Panel v2.x or higher
- Python 3.7+
- Linux server (Ubuntu 20.04+, Debian 10+, CentOS 7+)

## Troubleshooting

If you encounter issues:

1. **Check logs:**
   ```bash
   tail -100 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
   ```

2. **Test API connection:**
   ```bash
   python3 test_api_v2.py "your-panel-url"
   ```

3. **Read documentation:**
   - [API v2 Update Guide](API_V2_UPDATE_GUIDE.md)
   - [Migration Guide](MIGRATION_GUIDE.md)

4. **Join support group:** [@HidyBotGroup](https://t.me/HidyBotGroup)

## Screenshots
#### Users Bot
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-1.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-2.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-3.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-u-4.jpg?raw=True" width=35% height=35%>
#### Admin Bot
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-1.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-2.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-6.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-8.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-5.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-3.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-4.jpg?raw=True" width=35% height=35%>
- <img src="https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/scr-a-7.jpg?raw=True" width=35% height=35%>

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source. See the LICENSE file for details.

## Support

- **Telegram Group:** [@HidyBotGroup](https://t.me/HidyBotGroup)
- **Issues:** [GitHub Issues](https://github.com/sina-nozhati/foxybot/issues)
- **Documentation:** See the [docs](.) in this repository
