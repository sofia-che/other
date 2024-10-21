from enum import Enum

token = '6365072837:AAFuJTLwpM3ghQu9OMnbktkwriOOTHJcBzA'
db_file = 'database.vdb'


class States(Enum):
    S_START = '0'
    S_ENTER_SEX = '1'
    S_ENTER_AGE = '2'
    S_ENTER_LANGUAGE = '3'
    S_ENTER_CITY = '4'
    S_ENTER_AUDIO = '5'
