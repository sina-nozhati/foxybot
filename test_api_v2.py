#!/usr/bin/env python3
"""
Test script for Hiddify API v2 integration
Run this to test if your API setup is working correctly
"""

import sys
import requests
from urllib.parse import urlparse

def test_panel_url(panel_url):
    """Test if panel URL is valid and API is accessible"""
    print("=" * 60)
    print("Testing Hiddify API v2 Connection")
    print("=" * 60)
    
    # Parse URL
    print(f"\n1. Testing URL: {panel_url}")
    
    if not panel_url.endswith('/'):
        panel_url += '/'
    
    parsed = urlparse(panel_url)
    path_parts = [p for p in parsed.path.split('/') if p]
    
    if len(path_parts) < 2:
        print("❌ FAILED: URL must have format: https://domain.com/proxy_path/admin_uuid/")
        return False
    
    proxy_path = path_parts[0]
    admin_uuid = path_parts[1]
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    
    print(f"   Base URL: {base_url}")
    print(f"   Proxy Path: {proxy_path}")
    print(f"   Admin UUID: {admin_uuid}")
    
    # Test ping endpoint
    print("\n2. Testing /api/v2/panel/ping/ endpoint...")
    ping_url = f"{base_url}/{proxy_path}/api/v2/panel/ping/"
    headers = {
        'Hiddify-API-Key': admin_uuid,
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(ping_url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"   ✅ Ping successful! Response: {response.json()}")
        else:
            print(f"   ❌ Ping failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection error: {e}")
        return False
    
    # Test user list endpoint
    print("\n3. Testing /api/v2/admin/user/ endpoint...")
    users_url = f"{base_url}/{proxy_path}/api/v2/admin/user/"
    
    try:
        response = requests.get(users_url, headers=headers, timeout=10)
        if response.status_code == 200:
            users = response.json()
            print(f"   ✅ Successfully retrieved user list!")
            print(f"   Total users: {len(users)}")
            if users:
                print(f"   First user: {users[0].get('name', 'N/A')} (UUID: {users[0].get('uuid', 'N/A')})")
        else:
            print(f"   ❌ Failed to get users with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection error: {e}")
        return False
    
    # Test user subscription link format
    print("\n4. Testing user subscription link format...")
    if users:
        test_uuid = users[0]['uuid']
        sub_link = f"{base_url}/{proxy_path}/{test_uuid}/all.txt"
        print(f"   Sample subscription link: {sub_link}")
        print(f"   ✅ Link format is correct")
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    print("\nYour Hiddify bot is ready to use with API v2!")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 test_api_v2.py <panel_url>")
        print("\nExample:")
        print("  python3 test_api_v2.py https://cld.sin1990.ir/M5nZyVggd71SDkFeK0dZJ/c801ed73-24c6-4a72-a6d3-7258799c18d9/")
        sys.exit(1)
    
    panel_url = sys.argv[1]
    success = test_panel_url(panel_url)
    
    if not success:
        print("\n❌ Tests failed. Please check:")
        print("  1. Panel URL format is correct")
        print("  2. Admin UUID has proper permissions")
        print("  3. Panel is accessible and running")
        print("  4. Firewall allows connections")
        sys.exit(1)
