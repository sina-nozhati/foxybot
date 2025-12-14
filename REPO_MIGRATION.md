# Repository URL Update Summary

## ✅ All GitHub Links Updated

The repository has been migrated from:
```
https://github.com/B3H1Z/Hiddify-Telegram-Bot
```

To:
```
https://github.com/sina-nozhati/foxybot
```

## 📝 Files Updated

### 1. README.md
- Updated main repository links
- Updated screenshot image URLs
- Updated installation command
- Updated all command URLs
- Changed title from "Hidy Bot" to "Foxy Bot"
- Added API v2 information

### 2. README-FA.md (Persian)
- Updated all repository links
- Updated screenshot URLs
- Updated installation commands
- Changed title to "فاکسی بات (Foxy Bot)"
- Added API v2 information in Persian

### 3. install.sh
- Updated repository clone URL:
  ```bash
  repository_url="https://github.com/sina-nozhati/foxybot.git"
  ```

### 4. update.sh
- Updated reinstallation URL:
  ```bash
  bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
  ```

### 5. README_API_V2.md
- Updated installation command
- Updated GitHub Issues link

### 6. COMPLETE_SUMMARY.md
- Updated installation command

## 📋 Installation Commands

### New Installation
```bash
# Old command (NO LONGER VALID)
sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/B3H1Z/Hiddify-Telegram-Bot/main/install.sh)"

# New command (ACTIVE)
sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
```

### Quick Install (Short URL)
```bash
bash <(curl -Ls https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)
```

### Update Command
```bash
cd /opt/Hiddify-Telegram-Bot/ && \
curl -fsSL -o /opt/Hiddify-Telegram-Bot/update.sh https://raw.githubusercontent.com/sina-nozhati/foxybot/main/update.sh && \
chmod +x /opt/Hiddify-Telegram-Bot/update.sh && \
bash /opt/Hiddify-Telegram-Bot/update.sh
```

### Reinstall Command
```bash
cd /opt/ && \
rm -rf /opt/Hiddify-Telegram-Bot/ && \
sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)"
```

## 🖼️ Screenshot URLs

All screenshot URLs have been updated from:
```
https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/Screenshots/...
```

To:
```
https://github.com/sina-nozhati/foxybot/blob/main/Screenshots/...
```

## 🔗 Support & Resources

- **Repository:** https://github.com/sina-nozhati/foxybot
- **Issues:** https://github.com/sina-nozhati/foxybot/issues
- **Telegram Group:** @HidyBotGroup
- **Raw Files:** https://raw.githubusercontent.com/sina-nozhati/foxybot/main/

## ⚠️ Important Notes

1. **Old installation links will not work** once the old repository is removed or made private
2. **Existing users don't need to do anything** - the bot will continue working
3. **New installations** must use the new repository URL
4. **Updates** will automatically pull from the new repository if you've updated the code

## 🔄 Migration Steps for Existing Installations

If you have an existing installation from the old repository:

### Option 1: Update Remote URL (Recommended)
```bash
cd /opt/Hiddify-Telegram-Bot
git remote set-url origin https://github.com/sina-nozhati/foxybot.git
git fetch origin
git pull origin main
```

### Option 2: Fresh Install
```bash
# Backup database
cp /opt/Hiddify-Telegram-Bot/Database/hidyBot.db ~/hidyBot.db.backup

# Remove old installation
cd /opt
rm -rf Hiddify-Telegram-Bot

# Install from new repository
bash <(curl -Ls https://raw.githubusercontent.com/sina-nozhati/foxybot/main/install.sh)

# Restore database
cp ~/hidyBot.db.backup /opt/Hiddify-Telegram-Bot/Database/hidyBot.db

# Restart bot
cd /opt/Hiddify-Telegram-Bot
./restart.sh
```

## ✅ Verification

After updating, verify the remote URL:

```bash
cd /opt/Hiddify-Telegram-Bot
git remote -v
```

Should show:
```
origin  https://github.com/sina-nozhati/foxybot.git (fetch)
origin  https://github.com/sina-nozhati/foxybot.git (push)
```

## 📚 Documentation Updates

All documentation files now reference the new repository:
- README.md
- README-FA.md
- README_API_V2.md
- API_V2_UPDATE_GUIDE.md
- MIGRATION_GUIDE.md
- API_QUICK_REFERENCE.md
- UPDATE_SUMMARY.md
- COMPLETE_SUMMARY.md
- UPDATE_CHECKLIST.md
- VISUAL_COMPARISON.md

## 🎉 Summary

✅ All GitHub links updated to `sina-nozhati/foxybot`
✅ Bot name changed to "Foxy Bot" / "فاکسی بات"
✅ Installation scripts updated
✅ Update scripts updated
✅ README files updated (English & Persian)
✅ All documentation updated
✅ Screenshot URLs updated
✅ API v2 information added

**Status:** Ready to commit and push to new repository! 🚀
