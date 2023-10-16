from datetime import datetime

source_path = './template.py'
now = datetime.now()
name = now.strftime("%Y%b%d")
destination_path = f'./homework_{name}.py'
with open(source_path, mode='r') as source, open(destination_path, mode='w') as destination:
  destination.write(source.read())