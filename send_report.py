import sys
sys.path.insert(0, r'C:\Users\Administrator\.openclaw\workspace\skills\feishu-send-file\scripts')
from send_image import send_file_to_feishu

file_path = r'C:\Users\Administrator\Documents\WPS\美客多简报_2026-05-06.xlsx'
open_id = 'ou_21ff06ffa3f93234461308e06a89f3af'
app_id = 'cli_a94880223db81cc6'
app_secret = 'Pu678ngxjEfBgUmbn8MyHciFsnmjZQur'

result = send_file_to_feishu(file_path, open_id, app_id, app_secret)
print(result)
