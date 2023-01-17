from email import header
import gspread
import json
import requests
import pandas as pd


#Credenciales Spread

gscred = {
  "type": "service_account",
  "project_id": "acoustic-art-351008",
  "private_key_id": "dd6bac60d6b3ea9e7cd95968f853a0f53f72b17c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCw6TPH6nRdj6nl\nmt7dP5FZLCAy1mu7znsXmrUX8X7uCwhCJyhIXxb+mnftVgl5mydKL0E13Q+Q1Qw7\nDHr7jwQN+fuxxugUmetdiMICDSvYIp417FnAulyApNxXedrnNvI/0wjqs9Z0IKrK\n2xubE2Snozv/rGgVOoH9AQN9aJ9EQIADJtBsgT232goEc7B1Wz2GidkYWzkFstOg\nYhQwvlfW34YwR0IgJWrzH6qbLR/cTdESTQPr+aQUe6JI4g+i3ouZ4vRX0Vn22K5X\nsZN0+8K2rV93JpwTUn6+FDuJxnnVH9vjyplxY0Mlf+XAx4R8/5L5pI2DJiJ9VFYD\nAs3ioBoJAgMBAAECggEAMH6sqBeX8HHKQ9txTjr3r/cNmIH4pFHUokLRc4/KmJxD\nlka/nx8Z4Y8cYt3b2Q7z9T0A5jAD7VLJeIJSUBUDKoWlPjVlNwh+YXR0ojVUGHpc\n3jE85Tzw0H7gu8X2gL0qKN7DqfrERa8SwmrPpXHqfJ2de9eZ7H/OVDlr6Hu+dOm3\n0jAadVvfJwhWyVN98YL0m+5PrP63eJObMDWzFcCj6zEb6Iw0kXDMlAoY2HFl1ebS\nvGoYdbVJpO8Z3v4ywia6ID6pXlgh/BkzKHFSOvWi8EZUvebGBBvClheqEoqgxS+g\nXM4KZ5SaIUsSDMJ9DmbD/KhSIBgL3WKjOUsj71vdtQKBgQDxe7TCq6mxmUSer9IQ\n3hOTP3AqA172muhfRagTVa9Sr4kDry92aPdom3i/HF6R5+jG3k4dgwqt0Pd+cjeA\nI2+f45u8pzi22HUX3052v4N5CHa0oJG0NqnldkJXsVcbSAcmgg+OtLM9scJFarfR\ntzzoo0/a4nXTsBb0IyGXsPIcUwKBgQC7i8OrCZVKyO9A3t2u2kGM2m52XOYxpAvD\n6hUc+obEWO1i+VxZvEL/wE7irmJHkesUcgcuWKnjNVr5h3bSlNu3C3BVh3MVfEAs\nTJN3gWNmHEMM39ncv6nFh1euJhZRLFHQfkR6wtuSvd2ysUgdzif6EuVSyn7cdEGM\nguTMpucEswKBgQCjI7K7rWNIA0aTei6NjKpm2P26tGpMadzAuHtTDJkUYFhNL+X9\nte4nMpmBavYM1kKxT3Awid4GDV2WhC0wmUAJIaiN697p0BRTG16T5NA6TVh8sNme\niSuARMOPINS7Lo7+GfHOtA8/h766TN2Aha1VcTc6pbF6YMUxDCbepwD51wKBgCHd\nePWXg2e/pMQ3+huquY9vmeaxm7d3AdDcofdbnZ4y2Jq4oF5rykVYOmZgSsrVpHdK\np9VMmVC3v7ezKFeaHZqN7DjlfnhwuT3GjhJUQNidXdYjTbm4ujU63TBLHFiIAjX9\ntuvb5741nqS3smf/Y+SaKOKsQgAY1gVDVYFG2gxVAoGBALCZ+3Zjc3NA9eN4c7SW\nMFVV8mDYViGItmaupB4nKX2TXI1YxDtAAFVsQUWUXLdmsQCrg34Bi2XADDPs0lpu\nMUO934b2bOMeJS7/aYX0d7TDno37+eSy6q7EC2Yx1OLi/20crHyGo8FyDDIF64XD\nOlq5q739aZRMdAZ5R2pMB0vI\n-----END PRIVATE KEY-----\n",
  "client_email": "test-python@acoustic-art-351008.iam.gserviceaccount.com",
  "client_id": "104970499416562480147",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-python%40acoustic-art-351008.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(gscred)

# def readITEMS():
""" Traer un pandas con una lectura para actualizar items """

sh = gc.open_by_key("1LB-L7Jbux8GjE7s_W9OPA38zf_xjvBdL6dPoEuXaM30")
wh = sh.worksheet("crear proyecto")
df = pd.DataFrame(wh.get_all_values())
header_row = 0
df.columns = df.iloc[header_row]
df = df.drop(header_row)
dfdict = df.to_dict()
 

# l_items = []
# l_wstr = []
# l_wend = []
# l_analize = []
# l_creat = []
# l_rev = []
# l_num = []
# l_hestim = []
# l_hfact = []


# for i in df['Item']:
#         l_items.append(i)
# for i in df['semana inicio']:
#         l_wstr.append(str(i))
# for i in df['semana fin']:
#         l_wend.append(str(i))
# for i in df['Análisis']:
#         l_analize.append(str(i))


# print(litems)

#print(df)

#     return dff

#Creating a new item with column values populated

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE1MzE0NjI4MywidWlkIjoyNTUxMTc1NywiaWFkIjoiMjAyMi0wMy0yOVQxMjo1NDo0OS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTAyNTQxODcsInJnbiI6InVzZTEifQ.mSURvxP1wuL5tHinWC0gqGSHyt3iueQuxsOqvurjxnc"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

for i, row in df.iterrows():
    name = df['Item'][i]
    board = 2698880960
    group_id = "topics"
    column_data = {"person" : {"id" : 25511757}, "status" : df['Análisis'][i], "status9" : df['Creación'][i], "status7" : "Trabajando en ello",
    "n_meros" : str(df['semana inicio'][i]), "numbers" : str(df['semana fin'][i]), "numbers1" : "40", "numbers4" : "46", 
    "timeline" : {"from":"2022-07-10","to":"2022-07-18"}}

    data = {"query" : "mutation($name: String!, $board: Int!, $columns: JSON!, $group: String!)\
        {create_item(item_name:$name, group_id: $group , board_id:$board, column_values:$columns) \
        {name id column_values {id value}}\
        }",
        "variables" : {"name" : name, "board" : board, "group": group_id , "columns" : json.dumps(column_data)}} # enviamos valores de columnas como variables

    r = requests.post(url=apiUrl, json=data, headers=headers)
    res = r.json()
    print("INFO :: " + r.text)


#________________________________________________________________________
#     ind += 1

#     if l_items[ind] != "":
#       name = l_items[ind]
#       board = 2698880960
#       group_id = "topics"
#       column_data = {"person" : {"id" : 25511757}, "status" : l_analize[ind], "status9" : "Interrumpido", "status7" : "Trabajando en ello","n_meros" : str(l_wstr[ind]), "numbers" : str(l_wend[ind]), "numbers1" : "40", "numbers4" : "46", "timeline" : {"from":"2022-06-10","to":"2022-06-18"}}

#       data = {"query" : "mutation($name: String!, $board: Int!, $columns: JSON!, $group: String!)\
#           {create_item(item_name:$name, group_id: $group , board_id:$board, column_values:$columns) \
#           {name id column_values {id value}}\
#           }",
#           "variables" : {"name" : name, "board" : board, "group": group_id , "columns" : json.dumps(column_data)}} # enviamos valores de columnas como variables

#       r = requests.post(url=apiUrl, json=data, headers=headers)
#       res = r.json()
#       print("INFO :: " + r.text)

#API call para traer dict con info de tableros

# query = '{ boards (ids:2698880960) {name id description groups (ids: "topics") { title items (ids:2698881146) {name id  column_values {id value}} } } }'
# data = {'query' : query}

# r = requests.post(url=apiUrl, json=data, headers=headers) # make request
# res = r.json()
# dfm = pd.DataFrame.from_dict(res)
# dfm.reset_index(level=0, inplace=True)
# print(dfm)
















# #Creating a new item with column values populated

# def crearProyecto():
    
    
#     headers = {"Authorization" : cr.apiKey}
#     murl = cr.board
#     group_id = "topics"

#     column_data = {"person" : {"id" : 25511757}, "status" : data["analisis"], "status9" : data['creacion'], "status7" : data['revision'],"n_meros" : "10", "numbers" : "30", "numbers1" : "40", "numbers4" : "46", "timeline" : {"from":"2022-06-03","to":"2022-06-07"}}
    

#     data = {"query" : "mutation($name: String!, $board: Int!, $columns: JSON!, $group: String!)\
#     {create_item(item_name:$name, group_id: $group , board_id:$board, column_values:$columns) \
#     {name id column_values {id value}}\
#     }",
#     "variables" : {"name" : data['items'], "board" : cr.board, "group": group_id , "columns" : json.dumps(column_data)}} # enviamos valores de columnas como variables

#     r = requests.post(url=murl, json=data, headers=headers)
#     res = r.json()
#     print("INFO :: " + r.text)

#     try:
#             id = res["data"]["create_item"]["id"]
#             print("INFO :: Se ha creado el item en Monday con el ID " + id)
#     except:
#             id = "Error"
#             print("ERROR :: No se ha podido crear la tarea item en Monday")
#             print("RESPONSE :: " + r.text)
    
#     return id