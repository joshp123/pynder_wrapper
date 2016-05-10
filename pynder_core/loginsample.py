import urlparse
import requests


def get_token():
    headers = {
        'accept-encoding': 'gzip, deflate, sdch',
        'accept-language': 'en-GB,en;q=0.8,nl;q=0.6',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',  # noqa
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',   # noqa
        'authority': 'www.facebook.com',
        'cookie': 'datr=dafds; '
                  'c_user=12345612; '
                  'xs=iburnedmyselfintheshower; '
                  'act=pyramidguy1010; '
        }

    r = requests.get('https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token',
                     headers=headers,
                     allow_redirects=False)
    print(r.status_code)
    print(r.text)
    print(r.headers.keys())
    loc = r.headers.get('Location')
    print(loc)
    parsed_frags = urlparse.parse_qs(urlparse.urlparse(loc).fragment)
    print(parsed_frags)
    print("Expires in: {}".format(parsed_frags.get('expires_in')[0]))

    token = parsed_frags.get('access_token')[0]
    return token

if __name__ == '__main__':
    get_token()
