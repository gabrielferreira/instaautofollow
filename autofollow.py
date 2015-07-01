client_id = ""
client_secret = ""
# user_id = "294380188"
import urllib
import urllib2
import requests


# payload = { "ACCESS_TOKEN" : "",
#              "action" : "follow"}
print requests.get(r'https://api.instagram.com/v1/tags/nofilter/media/recent?client_id=')
# r = requests.post(r'https://api.instagram.com/v1/users/'+ user_id +'/relationship?access_token=Your_Instagram_API_Token_HERe',data=payload)
# print r.text


# from instagram.client import InstagramAPI
# import pdb; pdb.set_trace()
# api = InstagramAPI(client_id=client_id, client_secret=client_secret)
# popular_media = api.media_popular(count=20)
# for media in popular_media:
# import pdb; pdb.set_trace()
# print media.images['standard_resolution'].url

# auth_token = ""

# currently_following = set([])
# def parse_following(next_url=None):
#     import pdb; pdb.set_trace()
#     if next_url == None:
#         urlUserMedia = "https://api.instagram.com/v1/users/self/follows?access_token=%s" % (auth_token)
#     else:
#         urlUserMedia = next_url
#     values = {
#               'client_id' : client_id}
#     try:
#         data = urllib.urlencode(values)
#         req = urllib2.Request(urlUserMedia,None,headers)
#         response = urllib2.urlopen(req)
#         result = response.read()
#         dataObj = json.loads(result)
#         next_url = None
#         if dataObj.get('pagination') is not None:
#             next_url = dataObj.get('pagination').get('next_url')
#             currently_following.update(user['id'] for user in dataObj['data'])
#         if next_url is not None:
#             parse_following(next_url)
#
#     except Exception as e:
#         print e
# parse_following()
