import gspread

service_account = gspread.service_account(filename="crawlertutorial/credentials.json")
sheet = service_account.open("Schneiders List")
worksheet = sheet.worksheet("List Data")

csvFilePath = "crawlertutorial/test.csv"  # Please set your CSV file path.
spreadsheet_id = sheet.id  # Please set your Spreadsheet ID
sheetId = worksheet.id  # Please set your sheet ID.
spreadsheet = service_account.open_by_key(spreadsheet_id)

with open(csvFilePath, "r" , newline="", encoding='utf-8') as f:
    csvContents = f.read()
body = {
    "requests": [
        {
            "pasteData": {
                "coordinate": {
                    "sheetId": sheetId,
                },
                "data": csvContents,
                "type": "PASTE_NORMAL",
                "delimiter": ",",
            }
        },
    ]
}
spreadsheet.batch_update(body)