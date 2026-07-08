import csv
import json
import sqlite3
from typing import List, Tuple, Optional

def export_to_json(data: List[Tuple], filepath: str) -> bool:
    keys = ['id', 'bill_amount', 'tax_percent', 'tip_percent', 'people_count', 'total_sum', 'per_person', 'created_at']
    serializable_data = [dict(zip(keys, row)) for row in data]
    
    try:
        with open(filepath, 'w', encoding='utf-8-sig') as f:
            json.dump(serializable_data, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Ошибка записи JSON: {e}")
        return False

def import_from_json(filepath: str) -> Optional[List]:
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        
        rows = []
        for entry in data:
            rows.append((
                entry['id'], 
                entry['bill_amount'],
                entry['tax_percent'],
                entry['tip_percent'],
                entry['people_count'],
                entry['total_sum'],
                entry['per_person'],
                entry['created_at']
            ))
        return rows
    except (IOError, json.JSONDecodeError, KeyError) as e:
        print(f"Ошибка чтения JSON: {e}")
        return None

def export_to_csv(data: List[Tuple], filepath: str) -> bool:
    headers = [
        'ID', 'Сумма счета', 'Налог (%)', 'Чаевые (%)', 'Гостей', 
        'Общая сумма', 'На человека', 'Дата'
    ]
    try:
        with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for row in data:
                formatted_row = list(row[:7]) + [row[7].split('T')[0] + ' ' + row[7].split('T')[1][:5]]
                writer.writerow(formatted_row)
        return True
    except IOError as e:
        print(f"Ошибка записи CSV: {e}")
        return False