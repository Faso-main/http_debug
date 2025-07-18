import json, os, re


# Конфигурация
FILE_PATH = os.path.join('src', 'httpdata.json')

with open(FILE_PATH, 'r', encoding='cp1251') as f:  content = f.read()
fixed_content = re.sub(r'(\d),(\d)', r'\1.\2', content)

try:
    data = json.loads(fixed_content)
    print(data[0])
except KeyboardInterrupt: print(f'Остановлено вручную...........')
except json.JSONDecodeError as e:
    print(f"Ошибка вида: {e}")
    print("---->:", fixed_content[max(0, e.pos-50):e.pos+50])