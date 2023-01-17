import gspread

# Monday
apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE1MzE0NjI4MywidWlkIjoyNTUxMTc1NywiaWFkIjoiMjAyMi0wMy0yOVQxMjo1NDo0OS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTAyNTQxODcsInJnbiI6InVzZTEifQ.mSURvxP1wuL5tHinWC0gqGSHyt3iueQuxsOqvurjxnc"
board = 2698880960

# Spreadsheet

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
