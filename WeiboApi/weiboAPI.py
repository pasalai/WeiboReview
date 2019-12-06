import webbrowser
from WeiboApi import sinaweibopy3


def main():
    try:
        APP_KEY = '2047157240'
        APP_SECRET = '57a21639366669c3f92c9c1672081f10'
        REDIRECT_URL = 'http://api.weibo.com/oauth2/default.html'
        client = sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
        url = client.get_authorize_url()
        webbrowser.open_new(url)
        result = client.request_access_token(
            input("please input code : "))
        print(result)
        client.set_access_token(result.access_token, result.expires_in)
        print(client.public_timeline())
        print(client.get.statuses__public_timeline())
        print(client.get.account__get_uid())

    except ValueError:
        print('pyOauth2Error')


if __name__ == '__main__':
    main()
