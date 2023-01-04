import requests
import omletarcade

class Public: 

    def __init__(self, user):
        self.username = user

    def get_followers_count(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowersCount/?username={self.username}&token=default")
        
        json_load = response.json()

        self.followers = json_load["result"]

    def get_follows_count(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowsCount/?username={self.username}&token=default")
        
        json_load = response.json()

        self.follows = json_load["result"]

    def get_avatar(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getAvatar/?username={self.username}&token=default")
        json_load = response.json()

        self.avatar = json_load["result"]

    def get_level(self, user, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getLevel/?username={self.username}&token=default")
        json_load = response.json()

        self.level = json_load["result"]

    def get_stream_hotness(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamHotness/?username={self.username}&token=default")
        json_load = response.json()

        self.hotness = json_load["result"]

    def is_live(self, user, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/isLive/?username={self.username}&token=default")
        json_load = response.json()

        self.live = json_load["result"]

    def is_verified(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/isVerified/?username={self.username}&token=default")
        json_load = response.json()

        self.verified = json_load["result"]

class Private(Public):

    def __init__(self, user, token):
        self.token = token
        self.username = user
    
    def get_followers_list(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowersList/?username={self.username}&token={self.token}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    def get_follows_list(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowsList/?username={self.username}&token={self.token}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    def is_has_omlet_creator(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/isHasOmletCreator/?username={self.username}&token={self.username}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    def is_has_omlet_plus(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/isHasOmletPlus/?username={self.username}&token={self.token}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    def get_stream_viewers(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamViewers/?username={self.username}&token={self.token}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    def get_stream_sessionID(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamSessionID/?username={self.username}&token={self.token}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    def get_stream_viewers_list(self, stime=None):

        if (stime == None):
            pass
        else:
            omletarcade.set_timeout(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamViewersList/?username={self.username}&token={self.token}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

class TokenError(Exception):
    pass

class ConnectionError(Exception):
    pass