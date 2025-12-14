# from config import *
# from Utils.utils import *
import json
import logging
from urllib.parse import urlparse
import datetime
import requests
from config import API_PATH
import Utils


# Document: https://github.com/hiddify/Hiddify-Manager/blob/main/hiddifypanel/panel/commercial/restapi/v2/admin/api_admin.py
# Updated for Hiddify API v2


def parse_panel_url(url):
    """
    Parse panel URL to extract components for API v2
    URL format: https://domain.com/proxy_path/admin_uuid/
    Returns: (base_url, proxy_path, admin_uuid)
    """
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split('/') if p]
    
    if len(path_parts) >= 2:
        proxy_path = path_parts[0]
        admin_uuid = path_parts[1]
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        return base_url, proxy_path, admin_uuid
    else:
        logging.error(f"Invalid panel URL format: {url}")
        return None, None, None


def select(url, endpoint="/user/"):
    """Get all users from the panel"""
    try:
        base_url, proxy_path, admin_uuid = parse_panel_url(url)
        if not base_url:
            return None
        
        # API v2 endpoint: /{proxy_path}/api/v2/admin/user/
        api_url = f"{base_url}/{proxy_path}/api/v2/admin/user/"
        
        headers = {
            'Hiddify-API-Key': admin_uuid,
            'Accept': 'application/json'
        }
        
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            users = response.json()
            res = Utils.utils.dict_process(url, Utils.utils.users_to_dict(users))
            return res
        else:
            logging.error(f"API error: Status {response.status_code}, Response: {response.text}")
            return None
            
    except Exception as e:
        logging.error("API error: %s" % e)
        return None


def find(url, uuid, endpoint="/user/"):
    """Find a specific user by UUID"""
    try:
        base_url, proxy_path, admin_uuid = parse_panel_url(url)
        if not base_url:
            return None
        
        # API v2 endpoint: /{proxy_path}/api/v2/admin/user/{uuid}/
        api_url = f"{base_url}/{proxy_path}/api/v2/admin/user/{uuid}/"
        
        headers = {
            'Hiddify-API-Key': admin_uuid,
            'Accept': 'application/json'
        }
        
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"API error: Status {response.status_code}, Response: {response.text}")
            return None
            
    except Exception as e:
        logging.error("API error: %s" % e)
        return None


def insert(url, name, usage_limit_GB, package_days, last_reset_time=None, added_by_uuid=None, mode="no_reset",
            last_online="1-01-01 00:00:00", telegram_id=None,
            comment=None, current_usage_GB=0, start_date=None, endpoint="/user/"):
    """Create a new user"""
    import uuid as uuid_lib
    
    try:
        base_url, proxy_path, admin_uuid = parse_panel_url(url)
        if not base_url:
            return None
        
        uuid = str(uuid_lib.uuid4())
        
        # Set default values
        if not added_by_uuid:
            added_by_uuid = admin_uuid
        if not last_reset_time:
            last_reset_time = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # API v2 endpoint: /{proxy_path}/api/v2/admin/user/
        api_url = f"{base_url}/{proxy_path}/api/v2/admin/user/"
        
        headers = {
            'Hiddify-API-Key': admin_uuid,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Build payload according to PostUser schema
        data = {
            "uuid": uuid,
            "name": name,
            "usage_limit_GB": usage_limit_GB,
            "package_days": package_days,
            "mode": mode,
            "enable": True,
            "is_active": True,
            "current_usage_GB": current_usage_GB,
        }
        
        # Add optional fields
        if added_by_uuid:
            data["added_by_uuid"] = added_by_uuid
        if last_reset_time:
            data["last_reset_time"] = last_reset_time
        if telegram_id:
            data["telegram_id"] = telegram_id
        if comment:
            data["comment"] = comment
        if start_date:
            data["start_date"] = start_date
        if last_online:
            data["last_online"] = last_online
            
        response = requests.post(api_url, json=data, headers=headers)
        
        if response.status_code == 200:
            return uuid
        else:
            logging.error(f"API error: Status {response.status_code}, Response: {response.text}")
            return None
            
    except Exception as e:
        logging.error("API error: %s" % e)
        return None


def update(url, uuid, endpoint="/user/", **kwargs):
    """Update user information"""
    try:
        base_url, proxy_path, admin_uuid = parse_panel_url(url)
        if not base_url:
            return None
        
        # API v2 endpoint: /{proxy_path}/api/v2/admin/user/{uuid}/
        api_url = f"{base_url}/{proxy_path}/api/v2/admin/user/{uuid}/"
        
        headers = {
            'Hiddify-API-Key': admin_uuid,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Use PATCH method for partial updates
        response = requests.patch(api_url, json=kwargs, headers=headers)
        
        if response.status_code == 200:
            return uuid
        else:
            logging.error(f"API error: Status {response.status_code}, Response: {response.text}")
            return None
            
    except Exception as e:
        logging.error("API error: %s" % e)
        return None


def delete(url, uuid, endpoint="/user/"):
    """Delete a user"""
    try:
        base_url, proxy_path, admin_uuid = parse_panel_url(url)
        if not base_url:
            return None
        
        # API v2 endpoint: /{proxy_path}/api/v2/admin/user/{uuid}/
        api_url = f"{base_url}/{proxy_path}/api/v2/admin/user/{uuid}/"
        
        headers = {
            'Hiddify-API-Key': admin_uuid,
            'Accept': 'application/json'
        }
        
        response = requests.delete(api_url, headers=headers)
        
        if response.status_code == 200:
            return True
        else:
            logging.error(f"API error: Status {response.status_code}, Response: {response.text}")
            return None
            
    except Exception as e:
        logging.error("API error: %s" % e)
        return None
