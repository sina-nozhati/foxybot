# Quick Reference: Hiddify API v2

## URL Format
```
Admin Panel: https://domain.com/{proxy_path}/{admin_uuid}/
User Panel:  https://domain.com/{proxy_path}/{user_uuid}/
```

## API Endpoints

### Authentication
```python
headers = {
    'Hiddify-API-Key': admin_uuid,
    'Accept': 'application/json',
    'Content-Type': 'application/json'  # For POST/PATCH
}
```

### User Management

#### List All Users
```python
GET /{proxy_path}/api/v2/admin/user/

Response: [
    {
        "uuid": "string",
        "name": "string",
        "usage_limit_GB": 50.0,
        "current_usage_GB": 10.5,
        "package_days": 30,
        ...
    }
]
```

#### Get User Details
```python
GET /{proxy_path}/api/v2/admin/user/{uuid}/

Response: {
    "uuid": "string",
    "name": "string",
    ...
}
```

#### Create User
```python
POST /{proxy_path}/api/v2/admin/user/

Body: {
    "uuid": "string",  # Optional, auto-generated if empty
    "name": "string",  # Required
    "usage_limit_GB": 50.0,
    "package_days": 30,
    "mode": "no_reset",  # no_reset|monthly|weekly|daily
    "enable": true,
    "is_active": true
}

Response: {
    "uuid": "created-uuid",
    ...
}
```

#### Update User
```python
PATCH /{proxy_path}/api/v2/admin/user/{uuid}/

Body: {
    "name": "new-name",  # Any fields to update
    "usage_limit_GB": 100.0
}

Response: {
    "uuid": "uuid",
    ...
}
```

#### Delete User
```python
DELETE /{proxy_path}/api/v2/admin/user/{uuid}/

Response: {
    "msg": "success",
    "status": 200
}
```

### System Endpoints

#### Ping Test
```python
GET /{proxy_path}/api/v2/panel/ping/

Response: {
    "msg": "pong"
}
```

#### Panel Info
```python
GET /{proxy_path}/api/v2/panel/info/

Response: {
    "version": "2.2.0"
}
```

#### Server Status
```python
GET /{proxy_path}/api/v2/admin/server_status/

Response: {
    "stats": {...},
    "usage_history": {...}
}
```

## User Subscription Links

### Config Formats
```
All Configs:     https://domain.com/{proxy_path}/{user_uuid}/all.txt
Base64:          https://domain.com/{proxy_path}/{user_uuid}/all.txt?base64=True
Clash:           https://domain.com/{proxy_path}/{user_uuid}/clash/all.yml
Clash Meta:      https://domain.com/{proxy_path}/{user_uuid}/clash/meta/all.yml
Sing-box:        https://domain.com/{proxy_path}/{user_uuid}/singbox.json
Sing-box Full:   https://domain.com/{proxy_path}/{user_uuid}/full-singbox.json
Auto Subscribe:  https://domain.com/{proxy_path}/{user_uuid}/sub/?asn=unknown
```

### Deep Links
```
Clash:       clash://install-config?url={encoded_url}
Clash Meta:  clashmeta://install-config?url={encoded_url}
```

## Python Examples

### Using api.py Functions

```python
from Utils import api
from config import API_PATH

# Panel URL format
url = "https://domain.com/proxy_path/admin_uuid/"
api_url = url + API_PATH  # Adds /api/v2/admin

# List all users
users = api.select(api_url)

# Find specific user
user = api.find(api_url, uuid="user-uuid-here")

# Create new user
uuid = api.insert(
    api_url,
    name="Test User",
    usage_limit_GB=50,
    package_days=30,
    mode="no_reset",
    telegram_id=123456789,
    comment="Test account"
)

# Update user
api.update(api_url, uuid, 
    usage_limit_GB=100,
    package_days=60
)

# Delete user
api.delete(api_url, uuid)
```

### Direct API Calls

```python
import requests
from urllib.parse import urlparse

# Parse panel URL
url = "https://domain.com/proxy_path/admin_uuid/"
parsed = urlparse(url)
path_parts = [p for p in parsed.path.split('/') if p]

proxy_path = path_parts[0]
admin_uuid = path_parts[1]
base_url = f"{parsed.scheme}://{parsed.netloc}"

# Setup headers
headers = {
    'Hiddify-API-Key': admin_uuid,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# List users
api_url = f"{base_url}/{proxy_path}/api/v2/admin/user/"
response = requests.get(api_url, headers=headers)
users = response.json()

# Create user
data = {
    "name": "New User",
    "usage_limit_GB": 50,
    "package_days": 30,
    "enable": True,
    "is_active": True
}
response = requests.post(api_url, json=data, headers=headers)
new_user = response.json()

# Update user
user_url = f"{api_url}{new_user['uuid']}/"
update_data = {"usage_limit_GB": 100}
response = requests.patch(user_url, json=update_data, headers=headers)

# Delete user
response = requests.delete(user_url, headers=headers)
```

## User Object Schema

```python
{
    # Identity
    "uuid": "string",                    # Unique identifier
    "name": "string",                    # Display name
    "telegram_id": int | None,           # Telegram user ID
    
    # Usage
    "usage_limit_GB": float | None,      # Data limit in GB
    "current_usage_GB": float | None,    # Current usage in GB
    "package_days": int | None,          # Validity period in days
    "start_date": "YYYY-MM-DD" | None,   # Start date
    "last_reset_time": "YYYY-MM-DD HH:MM:SS" | None,
    
    # Status
    "mode": "no_reset|monthly|weekly|daily" | None,
    "enable": bool,                      # Account enabled
    "is_active": bool,                   # Currently active
    "last_online": "YYYY-MM-DD HH:MM:SS" | None,
    
    # Metadata
    "comment": str | None,               # Notes
    "added_by_uuid": str | None,         # Admin who created
    
    # Keys (auto-generated if empty)
    "ed25519_private_key": str | None,
    "ed25519_public_key": str | None,
    "wg_pk": str | None,                 # WireGuard private key
    "wg_pub": str | None,                # WireGuard public key
    "wg_psk": str | None                 # WireGuard preshared key
}
```

## Response Status Codes

```
200 - Success
401 - Unauthorized (invalid API key)
404 - Not Found (user/endpoint doesn't exist)
422 - Validation Error (invalid data)
500 - Server Error
```

## Testing Commands

```bash
# Test ping
curl -X GET \
  "https://domain.com/proxy_path/api/v2/panel/ping/" \
  -H "Hiddify-API-Key: admin-uuid" \
  -H "Accept: application/json"

# List users
curl -X GET \
  "https://domain.com/proxy_path/api/v2/admin/user/" \
  -H "Hiddify-API-Key: admin-uuid" \
  -H "Accept: application/json"

# Get user
curl -X GET \
  "https://domain.com/proxy_path/api/v2/admin/user/user-uuid/" \
  -H "Hiddify-API-Key: admin-uuid" \
  -H "Accept: application/json"

# Create user
curl -X POST \
  "https://domain.com/proxy_path/api/v2/admin/user/" \
  -H "Hiddify-API-Key: admin-uuid" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "usage_limit_GB": 50,
    "package_days": 30,
    "enable": true,
    "is_active": true
  }'

# Update user
curl -X PATCH \
  "https://domain.com/proxy_path/api/v2/admin/user/user-uuid/" \
  -H "Hiddify-API-Key: admin-uuid" \
  -H "Content-Type: application/json" \
  -d '{"usage_limit_GB": 100}'

# Delete user
curl -X DELETE \
  "https://domain.com/proxy_path/api/v2/admin/user/user-uuid/" \
  -H "Hiddify-API-Key: admin-uuid"
```

## Common Patterns

### Get User Info with Subscription Links
```python
from Utils import api, utils

url = "https://domain.com/proxy_path/admin_uuid/"
api_url = url + API_PATH

# Get user
user = api.find(api_url, uuid="user-uuid")

# Get subscription links
links = utils.sub_links(user['uuid'], url)

# Full user info
user_info = utils.user_info(url, user['uuid'])
```

### Search Users
```python
# By name
users = utils.search_user_by_name(url, "username")

# By UUID
user = utils.search_user_by_uuid(url, "uuid")

# By config
user = utils.search_user_by_config(url, "vmess://...")
```

### Process User Data
```python
users = api.select(api_url)
users_dict = utils.users_to_dict(users)
processed = utils.dict_process(url, users_dict)

# Each user now has:
# - name, uuid
# - usage (limit, current, remaining)
# - remaining_day
# - last_connection
# - link (user panel URL)
```

## Environment Variables

```python
# From config.py
PANEL_URL       # Panel URL with proxy_path and admin_uuid
API_PATH        # Always "/api/v2/admin"
PANEL_ADMIN_ID  # Extracted admin UUID
```

## Error Handling

```python
try:
    users = api.select(api_url)
    if not users:
        print("No users found or API error")
except Exception as e:
    logging.error(f"API error: {e}")
```

## Best Practices

1. ✅ Always use `parse_panel_url()` to extract URL components
2. ✅ Include proper headers in all requests
3. ✅ Use try-except for error handling
4. ✅ Log API errors for debugging
5. ✅ Validate user input before API calls
6. ✅ Use PATCH for partial updates (not POST)
7. ✅ Check response status codes
8. ❌ Don't store API keys in code
9. ❌ Don't make API calls without error handling
10. ❌ Don't use GET with body data

---

**Quick Test:**
```bash
python3 test_api_v2.py "https://your-domain.com/proxy_path/admin_uuid/"
```
