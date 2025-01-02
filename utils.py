import os
import datetime
import re
import json
from typing import Any, Dict, List, Optional, Union

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def format_date(date: datetime.datetime, format_str: str = "%Y-%m-%d") -> str:
    """Format datetime object to string."""
    return date.strftime(format_str)

def parse_date(date_str: str, format_str: str = "%Y-%m-%d") -> datetime.datetime:
    """Parse date string to datetime object."""
    return datetime.datetime.strptime(date_str, format_str)

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Read and parse JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(data: Dict[str, Any], file_path: str) -> None:
    """Write data to JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def ensure_directory_exists(directory_path: str) -> None:
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of specified size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def safe_get(obj: Dict[str, Any], key_path: str, default: Any = None) -> Any:
    """Safely get nested dictionary value using dot notation."""
    keys = key_path.split('.')
    current = obj
    
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        else:
            return default
    return current

def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Remove duplicates from a list while preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to specified length with optional suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def is_valid_url(url: str) -> bool:
    """Validate URL format."""
    pattern = r'^https?:\/\/([\w\d-]+\.)*[\w-]+\.[a-zA-Z]{2,}(?:\/.*)?$'
    return bool(re.match(pattern, url))

def sanitize_filename(filename: str) -> str:
    """Remove invalid characters from filename."""
    invalid_chars = r'[<>:"/\\|?*]'
    return re.sub(invalid_chars, '', filename)

def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def parse_bool(value: Union[str, bool]) -> bool:
    """Parse string to boolean value."""
    if isinstance(value, bool):
        return value
    return value.lower() in ('true', '1', 'yes', 'y', 'on')

def subtract_numbers(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Subtract two numbers and return the result."""
    return num1 - num2