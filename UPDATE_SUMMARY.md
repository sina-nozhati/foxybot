# Hiddify-Telegram-Bot API v2 Update - Summary

## Changes Overview

This update migrates the Hiddify-Telegram-Bot from API v1 to API v2, implementing the new RESTful API structure with header-based authentication.

## Modified Files

### 1. **Utils/api.py** (Complete Rewrite)
   - **Lines:** ~216 lines
   - **Changes:**
     - Added `parse_panel_url()` function to extract URL components
     - Updated `select()` for GET requests to list users
     - Updated `find()` for GET requests to get specific user
     - Updated `insert()` for POST requests to create users
     - Updated `update()` for PATCH requests to update users
     - Added `delete()` for DELETE requests to remove users
     - All functions now use `Hiddify-API-Key` header authentication
     - Changed endpoint format from `/api/v1/user/` to `/{proxy_path}/api/v2/admin/user/`

### 2. **config.py**
   - **Changes:**
     - Line 23: Changed `API_PATH = "/api/v1"` to `API_PATH = "/api/v2/admin"`
     - Lines 117-163: Completely rewrote `panel_url_validator()`:
       - Now validates API v2 URL structure
       - Tests connectivity using `/api/v2/panel/ping/` endpoint
       - Uses header-based authentication
       - Better error messages
     - Lines 87-104: Updated `set_config_variables()`:
       - Fixed admin UUID extraction from new URL format
       - Properly parses URL structure
     - Line 259: Updated example URL in user prompt

### 3. **Utils/utils.py**
   - **Changes:**
     - Lines 145-173: Updated `sub_links()`:
       - Properly extracts proxy_path from URL
       - Generates correct subscription links
     - Lines 108-141: Updated `dict_process()`:
       - Extracts proxy_path for user panel links
       - Generates correct user page URLs
     - Lines 194-223: Updated `backup_panel()`:
       - Parses new URL structure
       - Updated backup endpoint path

## New Files Created

### 4. **test_api_v2.py** (NEW)
   - **Purpose:** Test script to verify API v2 connectivity
   - **Usage:** `python3 test_api_v2.py <panel_url>`
   - **Tests:**
     - URL format validation
     - Ping endpoint connectivity
     - User list retrieval
     - Subscription link format

### 5. **API_V2_UPDATE_GUIDE.md** (NEW)
   - **Purpose:** Comprehensive documentation of API v2 changes
   - **Contents:**
     - Overview of API changes
     - Detailed change log for each file
     - Testing procedures
     - Troubleshooting guide
     - API schema reference

### 6. **MIGRATION_GUIDE.md** (NEW)
   - **Purpose:** Step-by-step migration guide for existing users
   - **Contents:**
     - Quick migration steps
     - URL format explanations
     - Common issues and solutions
     - Rollback procedures
     - Post-migration checklist

## Key API Changes

### URL Structure
**Before:**
```
https://domain.com/proxy_path/admin_uuid/admin/
```

**After:**
```
https://domain.com/proxy_path/admin_uuid/
```

### Authentication
**Before:** URL-based (UUID in path)
**After:** Header-based (`Hiddify-API-Key` header)

### Endpoints
**Before:**
```
GET/POST /api/v1/user/
```

**After:**
```
GET    /{proxy_path}/api/v2/admin/user/
POST   /{proxy_path}/api/v2/admin/user/
GET    /{proxy_path}/api/v2/admin/user/{uuid}/
PATCH  /{proxy_path}/api/v2/admin/user/{uuid}/
DELETE /{proxy_path}/api/v2/admin/user/{uuid}/
```

### User Subscription Links
**Before:**
```
https://domain.com/admin_uuid/user_uuid/all.txt
```

**After:**
```
https://domain.com/proxy_path/user_uuid/all.txt
```

## Testing Procedure

1. **Test URL Validation:**
   ```bash
   python3 test_api_v2.py "https://your-domain.com/proxy_path/admin_uuid/"
   ```

2. **Test API Manually:**
   ```bash
   # Ping test
   curl --request GET \
     --url https://your-domain.com/proxy_path/api/v2/panel/ping/ \
     --header 'Hiddify-API-Key: admin-uuid' \
     --header 'Accept: application/json'

   # List users
   curl --request GET \
     --url https://your-domain.com/proxy_path/api/v2/admin/user/ \
     --header 'Hiddify-API-Key: admin-uuid' \
     --header 'Accept: application/json'
   ```

3. **Test in Bot:**
   - Send `/start` command
   - List users
   - Create a test user
   - Get subscription link
   - Verify user can connect

## Installation Instructions

### New Installation:
```bash
# Clone repository
git clone https://github.com/B3H1Z/Hiddify-Telegram-Bot.git /opt/Hiddify-Telegram-Bot
cd /opt/Hiddify-Telegram-Bot

# Run installation
./install.sh

# When prompted, enter panel URL in new format:
# https://your-domain.com/proxy_path/admin_uuid/
```

### Update Existing Installation:
```bash
# Backup database
cd /opt/Hiddify-Telegram-Bot
cp Database/hidyBot.db Database/hidyBot.db.backup

# Stop bot
pkill -f "python3 hiddifyTelegramBot.py"

# Update code
git pull origin main

# Update configuration
python3 config.py

# Test API
python3 test_api_v2.py "your-panel-url"

# Restart bot
./restart.sh
```

## Compatibility

- ✅ **Hiddify Panel:** v2.x and above
- ✅ **Python:** 3.7+
- ✅ **Existing Users:** All user data preserved
- ✅ **Subscription Links:** Automatically updated
- ⚠️ **Old API:** No longer supported

## Breaking Changes

1. **Panel URL format must include proxy_path**
   - Old: May have worked without clear structure
   - New: Must be `https://domain.com/proxy_path/admin_uuid/`

2. **API Path constant changed**
   - Old: `API_PATH = "/api/v1"`
   - New: `API_PATH = "/api/v2/admin"`

3. **Authentication method changed**
   - Old: URL-based authentication
   - New: Header-based with `Hiddify-API-Key`

4. **HTTP methods changed**
   - Old: Mixed GET/POST
   - New: RESTful (GET, POST, PATCH, DELETE)

## No Breaking Changes For

- ✅ User UUIDs (remain the same)
- ✅ Database structure (unchanged)
- ✅ User credentials (preserved)
- ✅ Bot commands (same as before)
- ✅ Payment system (if using client bot)

## Support & Resources

- **Documentation:** See `API_V2_UPDATE_GUIDE.md` for detailed information
- **Migration:** See `MIGRATION_GUIDE.md` for step-by-step instructions
- **Testing:** Use `test_api_v2.py` to verify your setup
- **Support Group:** @HidyBotGroup
- **Logs:** `/opt/Hiddify-Telegram-Bot/Logs/hidyBot.log`

## Troubleshooting Quick Reference

| Error | Cause | Solution |
|-------|-------|----------|
| "URL format is invalid" | Wrong URL structure | Use format: `https://domain.com/proxy_path/admin_uuid/` |
| "API returned 401" | Auth failed | Check admin UUID is correct |
| "API returned 404" | Wrong endpoint | Verify panel is v2.x, check proxy_path |
| "Connection timeout" | Cannot reach server | Check domain, firewall, network |
| "User links not working" | Wrong link format | Links auto-updated, check proxy_path |

## Version Information

- **Bot Version:** 2.0 (API v2)
- **API Version:** v2
- **Last Updated:** December 14, 2025
- **Compatibility:** Hiddify Panel v2.x+

## Contributors

This update brings the bot inline with Hiddify Panel's new API architecture, ensuring long-term compatibility and better performance.

---

**Important:** Always backup your database before updating!
