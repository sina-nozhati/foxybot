# Hiddify-Telegram-Bot - API v2 Update

## 🎉 What's New

This update migrates the bot from Hiddify API v1 to API v2, bringing:

- ✅ Modern RESTful API architecture
- ✅ Header-based authentication for better security
- ✅ Proper HTTP methods (GET, POST, PATCH, DELETE)
- ✅ Improved error handling and logging
- ✅ Better URL structure and validation
- ✅ Full compatibility with Hiddify Panel v2.x

## 📋 Quick Start

### For New Users

1. **Install the bot:**
   ```bash
   bash <(curl -Ls https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)
   ```

2. **Enter your panel URL when prompted:**
   ```
   Format: https://your-domain.com/proxy_path/admin_uuid/
   Example: https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/
   ```

3. **Test the connection:**
   ```bash
   cd /opt/Hiddify-Telegram-Bot
   python3 test_api_v2.py "your-panel-url"
   ```

### For Existing Users

See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed migration steps.

**Quick migration:**
```bash
cd /opt/Hiddify-Telegram-Bot
cp Database/hidyBot.db Database/hidyBot.db.backup
pkill -f "python3 hiddifyTelegramBot.py"
git pull origin main
python3 config.py  # Enter new URL format
./restart.sh
```

## 📖 Documentation

- **[UPDATE_SUMMARY.md](UPDATE_SUMMARY.md)** - Overview of all changes
- **[API_V2_UPDATE_GUIDE.md](API_V2_UPDATE_GUIDE.md)** - Comprehensive technical guide
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - Step-by-step migration instructions
- **[API_QUICK_REFERENCE.md](API_QUICK_REFERENCE.md)** - Developer quick reference
- **[test_api_v2.py](test_api_v2.py)** - API connectivity test script

## 🔧 Key Changes

### URL Format

**Before (API v1):**
```
https://panel.example.com/proxy_path/admin_uuid/admin/
```

**After (API v2):**
```
https://panel.example.com/proxy_path/admin_uuid/
```

### Authentication

**Before:** URL-based
```python
url = "https://domain.com/proxy_path/admin_uuid/"
requests.get(url + "/admin/")
```

**After:** Header-based
```python
headers = {'Hiddify-API-Key': 'admin_uuid'}
requests.get(api_url, headers=headers)
```

### API Endpoints

**Before:**
```
GET/POST /api/v1/user/
```

**After:**
```
GET    /{proxy_path}/api/v2/admin/user/          # List users
POST   /{proxy_path}/api/v2/admin/user/          # Create user
GET    /{proxy_path}/api/v2/admin/user/{uuid}/   # Get user
PATCH  /{proxy_path}/api/v2/admin/user/{uuid}/   # Update user
DELETE /{proxy_path}/api/v2/admin/user/{uuid}/   # Delete user
```

## 🧪 Testing

Run the test script to verify everything works:

```bash
python3 test_api_v2.py "https://your-domain.com/proxy_path/admin_uuid/"
```

Expected output:
```
============================================================
Testing Hiddify API v2 Connection
============================================================

1. Testing URL: https://your-domain.com/...
   Base URL: https://your-domain.com
   Proxy Path: M5nZyVggd71SDkFeK0dZJ
   Admin UUID: c801ed73-24c6-4a72-a6d3-7258799c18d9

2. Testing /api/v2/panel/ping/ endpoint...
   ✅ Ping successful! Response: {'msg': 'pong'}

3. Testing /api/v2/admin/user/ endpoint...
   ✅ Successfully retrieved user list!
   Total users: 5
   First user: Test User (UUID: ...)

4. Testing user subscription link format...
   Sample subscription link: https://your-domain.com/.../all.txt
   ✅ Link format is correct

============================================================
✅ ALL TESTS PASSED!
============================================================
```

## 📝 Files Modified

- `Utils/api.py` - Complete rewrite for API v2
- `config.py` - Updated URL validator and admin UUID extraction
- `Utils/utils.py` - Fixed subscription links and URL parsing

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| "URL format is invalid" | Use format: `https://domain.com/proxy_path/admin_uuid/` |
| "API returned 401" | Verify admin UUID is correct |
| "Connection timeout" | Check domain is accessible |
| Links not working | Run test script, verify proxy_path |

For detailed solutions, see [API_V2_UPDATE_GUIDE.md](API_V2_UPDATE_GUIDE.md#troubleshooting).

## 📊 Compatibility

- ✅ **Hiddify Panel:** v2.x and above
- ✅ **Python:** 3.7+
- ✅ **Linux:** Ubuntu 20.04+, Debian 10+, CentOS 7+
- ✅ **Existing Data:** Fully preserved

## 🔄 What's Preserved

Your existing data is safe:
- ✅ All user accounts and UUIDs
- ✅ Usage statistics
- ✅ Payment history (if using client bot)
- ✅ Bot configuration
- ✅ Admin settings

## 📦 What's Updated

- ✅ API endpoints
- ✅ Authentication method
- ✅ Subscription link format
- ✅ URL structure

## 🆘 Getting Help

1. **Read the docs:**
   - [Migration Guide](MIGRATION_GUIDE.md)
   - [Update Guide](API_V2_UPDATE_GUIDE.md)
   - [Quick Reference](API_QUICK_REFERENCE.md)

2. **Check logs:**
   ```bash
   tail -100 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
   ```

3. **Run diagnostics:**
   ```bash
   python3 test_api_v2.py "your-panel-url"
   ```

4. **Join support:**
   - Telegram: @HidyBotGroup
   - GitHub: [Issues](https://github.com/sina-nozhati/foxybot/issues)

## 📚 Additional Resources

### For Users
- [Migration Guide](MIGRATION_GUIDE.md) - How to upgrade
- [Update Summary](UPDATE_SUMMARY.md) - What changed

### For Developers
- [API Quick Reference](API_QUICK_REFERENCE.md) - Code examples
- [Update Guide](API_V2_UPDATE_GUIDE.md) - Technical details
- [Test Script](test_api_v2.py) - API testing

### For Admins
- Panel URL format requirements
- Backup procedures
- Rollback instructions

## 🎯 Quick Commands

```bash
# Install bot
bash <(curl -Ls https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)

# Test API
python3 test_api_v2.py "your-panel-url"

# Update bot
cd /opt/Hiddify-Telegram-Bot && git pull && ./restart.sh

# View logs
tail -f /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log

# Check status
ps aux | grep hiddifyTelegramBot.py
```

## 🔐 Security Notes

- Panel URL contains admin UUID - keep it secure
- Use HTTPS for all connections
- Regularly backup your database
- Update panel and bot regularly

## 📈 Performance

API v2 improvements:
- Faster response times
- Better error handling
- More reliable connections
- Cleaner code structure

## 🎊 Success Stories

After successful migration:
- ✅ Bot responds faster
- ✅ More reliable user management
- ✅ Better error messages
- ✅ Easier troubleshooting

## 📝 License

Same as before - see main repository for details.

## 🙏 Credits

- Original Bot: @B3H1Z
- API v2 Update: Community contribution
- Hiddify Panel: Hiddify Team

## 📮 Feedback

Found an issue? Have a suggestion?
- Open an issue on GitHub
- Join @HidyBotGroup on Telegram
- Contribute improvements via PR

---

**Ready to upgrade?** Start with [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)

**Need help?** Check [API_V2_UPDATE_GUIDE.md](API_V2_UPDATE_GUIDE.md)

**Developer?** See [API_QUICK_REFERENCE.md](API_QUICK_REFERENCE.md)
