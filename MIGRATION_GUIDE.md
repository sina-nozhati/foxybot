# Migration Guide: API v1 to API v2

## Quick Migration Steps

### Step 1: Backup Your Data
```bash
cd /opt/Hiddify-Telegram-Bot
cp Database/hidyBot.db Database/hidyBot.db.backup.$(date +%Y%m%d)
```

### Step 2: Stop the Bot
```bash
pkill -f "python3 hiddifyTelegramBot.py"
```

### Step 3: Update the Code
```bash
cd /opt/Hiddify-Telegram-Bot
git stash  # Save any local changes
git pull origin main
```

### Step 4: Update Panel URL

Run the configuration script:
```bash
python3 config.py
```

When prompted, enter your new panel URL in this format:
```
https://your-domain.com/proxy_path/admin_uuid/
```

**Example:**
```
https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/
```

### Step 5: Test the API Connection
```bash
python3 test_api_v2.py "https://your-domain.com/proxy_path/admin_uuid/"
```

If all tests pass, proceed to the next step.

### Step 6: Restart the Bot
```bash
./restart.sh
```

### Step 7: Verify Bot is Running
```bash
ps aux | grep hiddifyTelegramBot.py
```

You should see the bot process running.

### Step 8: Test in Telegram
1. Send `/start` to your admin bot
2. Try listing users
3. Try creating a test user
4. Verify subscription links work

## Understanding URL Changes

### Old URL Format (API v1)
```
https://panel.example.com/7frgemkvtE0/78854985-68dp-425c-989b-7ap0c6kr9bd4/

Panel accessed at:
https://panel.example.com/7frgemkvtE0/78854985-68dp-425c-989b-7ap0c6kr9bd4/admin/
```

### New URL Format (API v2)
```
https://panel.example.com/7frgemkvtE0/78854985-68dp-425c-989b-7ap0c6kr9bd4/
                          └─ proxy_path ─┘└──────────── admin_uuid ───────────┘

Admin Panel:
https://panel.example.com/7frgemkvtE0/78854985-68dp-425c-989b-7ap0c6kr9bd4/

API Endpoints:
https://panel.example.com/7frgemkvtE0/api/v2/admin/user/
                          └─ proxy_path ─┘
```

## Finding Your Panel URL

### Method 1: From Browser
1. Open your Hiddify admin panel in browser
2. Copy the URL from address bar
3. Make sure it includes both proxy_path and admin_uuid
4. Example: `https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/`

### Method 2: Check Current Configuration
```bash
cd /opt/Hiddify-Telegram-Bot
python3 -c "from Database.dbManager import UserDBManager; db = UserDBManager('Database/hidyBot.db'); servers = db.select_servers(); print('Current URL:', servers[0]['url'] if servers else 'None'); db.close()"
```

## Common Issues and Solutions

### Issue 1: "URL format is invalid"
**Solution:** Make sure your URL:
- Starts with `https://` or `http://`
- Has exactly 2 parts after domain: `proxy_path` and `admin_uuid`
- Ends with a trailing slash `/`

**Correct:** `https://domain.com/abc123/uuid-here/`
**Wrong:** `https://domain.com/abc123/uuid-here` (missing trailing slash)
**Wrong:** `https://domain.com/uuid-here/` (missing proxy_path)

### Issue 2: "API returned status code: 401"
**Cause:** Authentication failed
**Solution:** 
- Verify your admin UUID is correct
- Check that the UUID has admin privileges in the panel
- Try accessing the panel directly in browser to confirm URL

### Issue 3: "Connection timeout"
**Cause:** Cannot reach the server
**Solution:**
- Check if panel domain is accessible: `ping your-domain.com`
- Verify firewall allows outbound connections
- Test API manually:
  ```bash
  curl -v https://your-domain.com/proxy_path/api/v2/panel/ping/ \
    -H "Hiddify-API-Key: your-admin-uuid" \
    -H "Accept: application/json"
  ```

### Issue 4: Bot starts but crashes when listing users
**Cause:** API endpoint mismatch
**Solution:**
- Run the test script: `python3 test_api_v2.py "your-panel-url"`
- Check logs: `tail -f /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log`
- Verify Hiddify panel is running version 2.x or higher

### Issue 5: Subscription links not working
**Cause:** Wrong URL format in links
**Solution:**
- Subscription links should be: `https://domain.com/proxy_path/user_uuid/all.txt`
- Not: `https://domain.com/admin_uuid/user_uuid/all.txt`
- The bot automatically generates correct links after migration

## Verifying Migration Success

### 1. Check Bot Status
```bash
systemctl status hiddify-bot  # If using systemd
# OR
ps aux | grep hiddifyTelegramBot.py
```

### 2. Check Logs
```bash
tail -f /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
```

Look for:
- ✅ "GET Request to panel.private.com/api/v2/admin/user/"
- ❌ "API error: Status 401" or "API error: Status 404"

### 3. Test in Telegram
Send these commands to your bot:
1. `/start` - Should show main menu
2. Click "Users List" - Should show your users
3. Try creating a user - Should succeed
4. Get subscription link - Link should work

### 4. Test User Panel
For an existing user, try accessing:
```
https://your-domain.com/proxy_path/user_uuid/
```
Should show user panel with configs.

## Rolling Back (If Needed)

If something goes wrong:

```bash
# Stop the bot
pkill -f "python3 hiddifyTelegramBot.py"

# Restore database backup
cd /opt/Hiddify-Telegram-Bot
cp Database/hidyBot.db.backup.YYYYMMDD Database/hidyBot.db

# Revert code changes
git stash
git checkout HEAD~1  # Go back to previous version

# Restart bot
./restart.sh
```

## Post-Migration Checklist

- [ ] Bot starts without errors
- [ ] Can list users successfully
- [ ] Can create new users
- [ ] User subscription links work
- [ ] User panel pages load correctly
- [ ] Backup job still works
- [ ] Payment system works (if using client bot)
- [ ] All existing users can connect

## Getting Help

If you need assistance:

1. **Check logs first:**
   ```bash
   tail -100 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log
   tail -100 /opt/Hiddify-Telegram-Bot/bot.log
   ```

2. **Run diagnostic test:**
   ```bash
   python3 test_api_v2.py "your-panel-url"
   ```

3. **Join support group:** @HidyBotGroup

4. **When asking for help, provide:**
   - Output of test script
   - Relevant log entries
   - Your Hiddify panel version
   - Steps that led to the issue

## Important Notes

- ⚠️ User UUIDs don't change - existing users keep working
- ⚠️ Subscription links are automatically updated
- ⚠️ No need to regenerate configs for users
- ⚠️ Multiple servers? Update URL for each in bot settings
- ✅ User data is preserved during migration
- ✅ Bot settings (admins, tokens) are preserved
- ✅ Payment history is preserved (if using client bot)

## Migration Complete!

Once all tests pass and the bot is working:
1. Update any documentation with new URL format
2. Inform other admins about the changes
3. Monitor logs for the first few hours
4. Keep the database backup for at least 7 days

Your bot is now running on Hiddify API v2! 🎉
