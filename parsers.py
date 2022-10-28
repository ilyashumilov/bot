import urllib.request
import requests as r
import os

class parsers():
    @classmethod
    def ig_parser(user):
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'

        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
        }

        resp = r.get(url, headers=headers, timeout=10)
        image_url = resp.json()['data']['user']['profile_pic_url']

        # Adding user_agent information
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # Image URL and Filename
        filename = "pic.jpg"

        # Get resource
        urllib.request.urlretrieve(image_url, filename)

        print(os.listdir())

    @classmethod
    def vk_parser(username):

        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
        }

        # Adding user_agent information
        opener = urllib.request.build_opener()

        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # Image URL and Filename
        filename = "pic.jpg"

        # Get resource

        print(os.listdir())

parsers.vk_parser()