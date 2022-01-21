import gspread

from oauth2client.service_account import ServiceAccountCredentials as sac

scope = ['https://spreadsheet.google.com/feeds','https://www.googleapis.com/auth/drive']

cr = sac.from_json_keyfile_name('token.json', scope)

gs = gspread.authorize(cr)

sh= gs.open('GoogleSheet')

wks = sh.sheet1

wks = sh.worksheet('網拍價格')