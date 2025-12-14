# API v2 Update Checklist

## Pre-Update Checklist

Before updating your bot, make sure you have:

- [ ] Hiddify Panel v2.x or higher installed
- [ ] Current admin panel URL in new format: `https://domain.com/proxy_path/admin_uuid/`
- [ ] Backup of database: `Database/hidyBot.db`
- [ ] Access to server (SSH)
- [ ] Bot is currently working (to compare after update)

## Update Process Checklist

### 1. Backup Phase
- [ ] Stop the bot: `pkill -f "python3 hiddifyTelegramBot.py"`
- [ ] Backup database: `cp Database/hidyBot.db Database/hidyBot.db.backup.$(date +%Y%m%d)`
- [ ] Backup config (optional): `cp config.py config.py.backup`
- [ ] Note current panel URL from database
- [ ] Take screenshot of working bot in Telegram

### 2. Update Code
- [ ] Navigate to bot directory: `cd /opt/Hiddify-Telegram-Bot`
- [ ] Stash local changes (if any): `git stash`
- [ ] Pull latest code: `git pull origin main`
- [ ] Verify files updated:
  - [ ] `Utils/api.py` has `parse_panel_url()` function
  - [ ] `config.py` has new `panel_url_validator()` function
  - [ ] `test_api_v2.py` exists

### 3. Configuration Update
- [ ] Run config: `python3 config.py`
- [ ] When asked "Do you want to change config?", answer: `y`
- [ ] Enter new panel URL format:
  ```
  https://your-domain.com/proxy_path/admin_uuid/
  ```
- [ ] Verify URL validation passes
- [ ] Config saved successfully

### 4. Testing Phase
- [ ] Run API test: `python3 test_api_v2.py "your-panel-url"`
- [ ] All 4 tests pass:
  - [ ] URL format validation ✅
  - [ ] Ping endpoint ✅
  - [ ] User list retrieval ✅
  - [ ] Subscription link format ✅

### 5. Restart Bot
- [ ] Start bot: `./restart.sh`
- [ ] Wait 5 seconds
- [ ] Check process: `ps aux | grep hiddifyTelegramBot.py`
- [ ] Process is running ✅

### 6. Telegram Testing
- [ ] Open bot in Telegram
- [ ] Send `/start` command
- [ ] Bot responds with menu ✅
- [ ] Click "Users List"
- [ ] Users are displayed ✅
- [ ] Try creating test user:
  - [ ] User created successfully
  - [ ] UUID generated
  - [ ] Subscription link works
- [ ] Try editing user:
  - [ ] Name update works
  - [ ] Usage update works
  - [ ] Days update works
- [ ] Try searching user:
  - [ ] By name works
  - [ ] By UUID works
  - [ ] By config works

### 7. Verify Subscription Links
- [ ] Get subscription link for test user
- [ ] Link format is: `https://domain.com/proxy_path/user_uuid/all.txt` ✅
- [ ] Copy link and test in browser
- [ ] Configs are returned ✅
- [ ] Test with v2ray/clash client
- [ ] Connection works ✅

### 8. Check Logs
- [ ] View logs: `tail -50 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log`
- [ ] No error messages ✅
- [ ] API requests showing "/api/v2/admin/user/" ✅
- [ ] No "404" or "401" errors ✅

## Post-Update Verification

### Functionality Check
- [ ] Bot commands work:
  - [ ] `/start` - Shows menu
  - [ ] Users list - Displays users
  - [ ] Add user - Creates user
  - [ ] Edit user - Updates user
  - [ ] Search user - Finds users
  - [ ] User info - Shows details
  - [ ] System status - Shows stats
  - [ ] Backup - Creates backup

### User Panel Check (if using client bot)
- [ ] Client bot responds
- [ ] Users can see their info
- [ ] Users can get subscription links
- [ ] Payment system works (if enabled)
- [ ] Test subscription works

### Admin Features
- [ ] Server management works
- [ ] Multiple servers work (if using)
- [ ] Backup system works
- [ ] Statistics accurate
- [ ] Expired users detected correctly

### Integration Check
- [ ] Cron jobs still working:
  ```bash
  crontab -l
  ```
- [ ] Backup job scheduled ✅
- [ ] Reminder job scheduled ✅
- [ ] Reboot job scheduled ✅

## Troubleshooting Checklist

If something doesn't work:

### Bot Won't Start
- [ ] Check logs: `tail -100 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log`
- [ ] Check database exists: `ls -la Database/hidyBot.db`
- [ ] Check config: `python3 -c "from config import PANEL_URL; print(PANEL_URL)"`
- [ ] Try manual start: `python3 hiddifyTelegramBot.py`
- [ ] Check Python version: `python3 --version` (should be 3.7+)

### API Errors
- [ ] Test API manually:
  ```bash
  curl -X GET "https://domain.com/proxy_path/api/v2/panel/ping/" \
    -H "Hiddify-API-Key: admin-uuid"
  ```
- [ ] Check panel is running and accessible
- [ ] Verify URL has correct proxy_path and admin_uuid
- [ ] Test from panel directly: visit `https://domain.com/proxy_path/admin_uuid/`

### Users Not Loading
- [ ] Run test script: `python3 test_api_v2.py "panel-url"`
- [ ] Check if old API_PATH is still set
- [ ] Verify headers include `Hiddify-API-Key`
- [ ] Check panel version is v2.x

### Subscription Links Broken
- [ ] Check link format: should be `https://domain.com/proxy_path/user_uuid/...`
- [ ] Not: `https://domain.com/admin_uuid/user_uuid/...`
- [ ] Test link in browser
- [ ] Check proxy_path is correct

## Rollback Checklist

If you need to rollback:

- [ ] Stop bot: `pkill -f "python3 hiddifyTelegramBot.py"`
- [ ] Restore database: `cp Database/hidyBot.db.backup.YYYYMMDD Database/hidyBot.db`
- [ ] Revert code: `git stash && git checkout HEAD~1`
- [ ] Restore config (if backed up): `cp config.py.backup config.py`
- [ ] Restart: `./restart.sh`
- [ ] Verify old version works

## Success Indicators

You know the update is successful when:

✅ **All tests pass:**
- Test script shows all green checkmarks
- No errors in logs
- Bot responds in Telegram

✅ **Core functions work:**
- List users
- Create user
- Edit user
- Get subscription links
- Links work in clients

✅ **No errors for 24 hours:**
- Monitor logs for first day
- Check cron jobs run successfully
- Verify backups work

## Documentation Checklist

After successful update:

- [ ] Update any custom documentation
- [ ] Note new URL format for reference
- [ ] Save test results
- [ ] Document any custom changes
- [ ] Share success with team

## Final Verification

After 24 hours of running:

- [ ] Check logs for any errors
- [ ] Verify all scheduled tasks ran
- [ ] Test all bot features again
- [ ] Confirm user counts match
- [ ] Verify backup was created
- [ ] Delete old backup (after 7 days)

## Support Checklist

If you need help:

- [ ] Read documentation:
  - [ ] MIGRATION_GUIDE.md
  - [ ] API_V2_UPDATE_GUIDE.md
  - [ ] UPDATE_SUMMARY.md
- [ ] Run test script and save output
- [ ] Collect log files (last 100 lines)
- [ ] Note Hiddify panel version
- [ ] Prepare exact error messages
- [ ] Join @HidyBotGroup
- [ ] Provide collected information

## Maintenance Checklist

Regular maintenance after update:

### Daily
- [ ] Check logs for errors
- [ ] Verify bot is running

### Weekly  
- [ ] Review user activity
- [ ] Check system resources
- [ ] Verify backups exist

### Monthly
- [ ] Update bot if new version available
- [ ] Clean old backup files
- [ ] Review and optimize

## Notes Section

Use this space to record:

**Date Updated:** _______________

**Panel URL:** _______________

**Issues Encountered:** 
_____________________________________
_____________________________________

**Solutions Applied:**
_____________________________________
_____________________________________

**Next Review Date:** _______________

---

## Quick Status Check

Everything working? Check these:

```bash
# Bot running?
ps aux | grep hiddifyTelegramBot.py

# Recent logs
tail -20 /opt/Hiddify-Telegram-Bot/Logs/hidyBot.log

# Test API
python3 test_api_v2.py "your-panel-url"

# Check config
python3 -c "from config import PANEL_URL, API_PATH; print(f'{PANEL_URL}{API_PATH}')"
```

**All green?** ✅ You're done!

**Some red?** 🔴 Check troubleshooting section above.
