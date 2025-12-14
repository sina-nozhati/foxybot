# Hiddify-Telegram-Bot API v2 Update Guide

## Overview
This document describes the updates made to the Hiddify-Telegram-Bot to support the new Hiddify-Manager API v2 system.

## What Changed in Hiddify API v2

### 1. URL Structure
**Old (API v1):**
```
https://domain.com/proxy_path/admin_uuid/
Panel accessed at: https://domain.com/proxy_path/admin_uuid/admin/
```

**New (API v2):**
```
Admin Panel: https://domain.com/proxy_path/admin_uuid/
User Panel: https://domain.com/proxy_path/user_uuid/
```

### 2. Authentication Method
**Old:** URL-based authentication (UUID in URL path)
**New:** Header-based authentication using `Hiddify-API-Key` header

### 3. API Endpoints
**Old (v1):**
```
GET  /api/v1/user/                    # List users
POST /api/v1/user/                    # Create/Update user
```

**New (v2):**
```
GET    /{proxy_path}/api/v2/admin/user/              # List all users
POST   /{proxy_path}/api/v2/admin/user/              # Create user
GET    /{proxy_path}/api/v2/admin/user/{uuid}/       # Get user details
PATCH  /{proxy_path}/api/v2/admin/user/{uuid}/       # Update user
DELETE /{proxy_path}/api/v2/admin/user/{uuid}/       # Delete user
```

### 4. Request Format
**Old:** Mixed GET/POST with data in body
**New:** RESTful with proper HTTP methods (GET, POST, PATCH, DELETE)

## Files Modified

### 1. Utils/api.py (Complete Rewrite)
**Key Changes:**
- Added `parse_panel_url()` function to extract base_url, proxy_path, and admin_uuid
- Updated all functions to use API v2 endpoints
- Implemented proper HTTP headers with `Hiddify-API-Key`
- Changed request methods (GET, POST, PATCH, DELETE)
- Added proper error logging

**New Functions:**
```python
parse_panel_url(url)  # Extracts components from panel URL
select(url)           # GET /{proxy_path}/api/v2/admin/user/
find(url, uuid)       # GET /{proxy_path}/api/v2/admin/user/{uuid}/
insert(url, ...)      # POST /{proxy_path}/api/v2/admin/user/
update(url, uuid, **kwargs)  # PATCH /{proxy_path}/api/v2/admin/user/{uuid}/
delete(url, uuid)     # DELETE /{proxy_path}/api/v2/admin/user/{uuid}/
```

### 2. config.py
**Changes:**
- Updated `API_PATH` constant from `/api/v1` to `/api/v2/admin`
- Completely rewrote `panel_url_validator()` function:
  - Now validates API v2 URL structure
  - Tests connectivity using `/api/v2/panel/ping/` endpoint
  - Properly extracts and validates proxy_path and admin_uuid
- Updated `set_config_variables()` to correctly extract admin UUID from new URL format
- Updated example URL in user prompts

### 3. Utils/utils.py
**Changes:**
- Updated `dict_process()` to properly extract proxy_path for user links
- Updated `sub_links()` to generate correct subscription links using proxy_path
- Updated `backup_panel()` to work with new URL structure

## Testing Your Installation

### 1. Test URL Format
Your admin panel URL should look like:
```
https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/
                      └─── proxy_path ──┘└──────────── admin_uuid ────────────┘
```

### 2. Test API Connectivity
You can test the API manually:

```bash
# Test ping endpoint
curl --request GET \
  --url https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/api/v2/panel/ping/ \
  --header 'Accept: application/json' \
  --header 'Hiddify-API-Key: c801ed73-24c6-4a72-a6d3-7258799c18d9'

# List all users
curl --request GET \
  --url https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/api/v2/admin/user/ \
  --header 'Accept: application/json' \
  --header 'Hiddify-API-Key: c801ed73-24c6-4a72-a6d3-7258799c18d9'

# Get specific user
curl --request GET \
  --url https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/api/v2/admin/user/USER-UUID-HERE/ \
  --header 'Accept: application/json' \
  --header 'Hiddify-API-Key: c801ed73-24c6-4a72-a6d3-7258799c18d9'
```

### 3. Test User Subscription Links
User subscription links are now formatted as:
```
https://domain.com/{proxy_path}/{user_uuid}/all.txt
https://domain.com/{proxy_path}/{user_uuid}/clash/all.yml
https://domain.com/{proxy_path}/{user_uuid}/singbox.json
```

Example:
```
https://cld.sin1990.ir/4bMP90n3sh9W4sbm0Rh/7a4256c2-39ad-46a2-bd79-6ae964aff492/all.txt
```

## Installation/Update Process

### For New Installations:
1. Run the installation script as normal
2. When prompted for panel URL, use the new format:
   ```
   https://your-domain.com/proxy_path/admin_uuid/
   ```
3. The bot will validate the URL and test API connectivity

### For Existing Installations:
1. Stop the bot:
   ```bash
   pkill -f "python3 hiddifyTelegramBot.py"
   ```

2. Backup your database:
   ```bash
   cd /opt/Hiddify-Telegram-Bot
   cp Database/hidyBot.db Database/hidyBot.db.backup
   ```

3. Pull the updates:
   ```bash
   git pull origin main
   ```

4. Update your panel URL in the database:
   ```bash
   python3 config.py
   ```
   Enter the new URL format when prompted

5. Restart the bot:
   ```bash
   ./restart.sh
   ```

## Troubleshooting

### Error: "URL format is invalid"
- Ensure your URL follows the format: `https://domain.com/proxy_path/admin_uuid/`
- Make sure it ends with a trailing slash `/`
- Verify you're using the admin panel URL, not the user panel URL

### Error: "API returned status code: 401"
- Check that your admin UUID is correct
- Verify the UUID has admin privileges in the panel

### Error: "Connection timeout"
- Verify the panel domain is accessible
- Check if the proxy_path is correct
- Ensure the panel is running and accessible

### Users Not Loading
- Check the logs at `/opt/Hiddify-Telegram-Bot/Logs/hidyBot.log`
- Verify the API endpoints are responding:
  ```bash
  curl -v https://your-domain.com/proxy_path/api/v2/admin/user/ \
    -H "Hiddify-API-Key: your-admin-uuid"
  ```

## API v2 Schema Reference

### User Object (Simplified)
```json
{
  "uuid": "string",
  "name": "string",
  "usage_limit_GB": 50.0,
  "current_usage_GB": 10.5,
  "package_days": 30,
  "mode": "no_reset|monthly|weekly|daily",
  "enable": true,
  "is_active": true,
  "telegram_id": 123456789,
  "comment": "string",
  "start_date": "2025-01-01",
  "last_online": "2025-12-14 10:30:00",
  "last_reset_time": "2025-12-14 00:00:00"
}
```

## Support

If you encounter issues:
1. Check the logs in `/opt/Hiddify-Telegram-Bot/Logs/`
2. Verify your panel is running Hiddify v2.x
3. Test API connectivity manually using curl commands above
4. Join the support group: @HidyBotGroup

## Changelog

### Version 2.0 (API v2 Update)
- ✅ Updated to Hiddify-Manager API v2
- ✅ Implemented header-based authentication
- ✅ Added proper RESTful HTTP methods
- ✅ Fixed URL parsing for proxy_path extraction
- ✅ Updated subscription link generation
- ✅ Improved error handling and logging
- ✅ Updated installation script with new URL format examples

## Migration Notes

**Important:** If you're migrating from API v1:
1. Your existing user UUIDs remain the same
2. The panel URL structure changes, but user data is preserved
3. All subscription links will be automatically regenerated with the new format
4. No manual intervention needed for existing users

## Future Considerations

The bot now supports:
- Multiple servers with different API versions (if needed)
- Proper error handling for API changes
- Extensible architecture for future API updates
- Better logging for debugging API issues
