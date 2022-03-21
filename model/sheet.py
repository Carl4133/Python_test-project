import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
import os
import sys

class GoogleSheet():
    def __init__(self, wks_name, wks_title=None, oauth='oauth.json'):
        scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

        try:
            JSON_PATH = os.path.join(os.getcwd(),'model', oauth)
            # cr = sac.from_json_keyfile_name(JSON_PATH, scope)
            cr = sac.from_json_keyfile_name('google_auth.json', scope)  # 請自行修改檔名
        except:
            print('無法開啟憑證檔')
            sys.exit(1)

        try: # 嘗試開啟Google試算表
            gc = gspread.authorize(cr)
            # sh = gc.open(wks_name)
            sh = gc.open('桃園房市')  # 請自行修改試算表名稱
        except Exception as e:
            print('無法開啟Google試算表', e)
            sys.exit(1)

        if wks_title is None:
            self._wks = sh.sheet1
        else:
            try:
                self._wks = sh.workssheet(wks_title)
            except:
                print('無法開啟工作表')
                sys.exit(1)
    
    @property
    def headers(self):
        return self._wks.row_values(1)
    
    def update_header(self, data, delete=True):
        if delete:
            self._wks.delete_row(1)
        self._wks.insert_row(data, 1)

    def append_row(self, data):
        self._wks.append_row(data)
    def resize(self, n=1):
        self._wks.resize(n)