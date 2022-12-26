import requests, config

LOGIN_URL = "https://prelinker.com/index/login"
STATS_URL = "https://prelinker.com/dashboard/index/statistics"

login_payload = {
    'login': config.USERNAME,
    'pass': config.PASSWORD
}

with requests.Session() as session:
    req = session.post(LOGIN_URL, data=login_payload)
    if req.status_code == 200:
        res = session.get(STATS_URL).json()
        
        today = res[0]['data']
        yesterday = res[1]['data']
        monthly = res[2]['data']['current']['data']

        print("[PRELINKER DATA]\n")
        print(f"Today: {today}\nYesterday: {yesterday}\nThis Month: {monthly}")
    else:
        print(req.status_code)