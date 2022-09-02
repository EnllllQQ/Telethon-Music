import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "12740957"))
    API_HASH = os.environ.get("API_HASH", "2491be54bfe2b8ad1c74f713a6e6fed1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5434335947:AAHsqST0aWCurTTcyN_9S7_VZJKzxB5K55o")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAB7_Sqb3Dazpfww6iptn2cNPhs2-LhlaOt8QViJRK12_ixVZVudD2c1GPz4u4tTVHNaDOvwGEeDg0xTQlmu_16eC_1qMss85iQxCbbsof4S1OTtF_FxO016mAc7OfEjAkWndPaMNnnhefXEVCbXlcgzoeG1KgLdwx0WIwNhVjocll6wKa7cD2Py5Am3A6_EsnEW7hda1Cw_yOAQNfXby6BP4MTVN4351-9OJzHEz5Wtx_Elj4AZJLkI5Cl-2RBbxnnuOzZVx5hmwPXR1Y-Z51Sx0nBuDIQviGCx8yvNMM3F24iJM94h1pnfuSDcmMkIsF48wfdxs0Er1DjZgPndiUBoAAAAAU49rkAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MORBIDED_BOT")
    SUPPORT = os.environ.get("SUPPORT", "MORBIDED_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "MORBIDED")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
