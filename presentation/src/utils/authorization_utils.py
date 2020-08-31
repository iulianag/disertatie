
class AuthorizationUser(object):
    active_user_token = {}

    @classmethod
    def set_online_user(cls, client_host, username, token):
        cls.active_user_token[client_host] = {
            'username': username,
            'session_token': token
        }

    @classmethod
    def logout_user(cls, client_host):
        cls.active_user_token.pop(client_host, None)

    @classmethod
    def get_token(cls, client_host):
        client_details = cls.active_user_token.get(client_host, None)
        if client_details:
            return client_details.get('session_token', None)
        return

    @classmethod
    def get_username(cls, client_host):
        client_details = cls.active_user_token.get(client_host, None)
        if client_details:
            return client_details.get('username', None)
        return

    @classmethod
    def is_authenticated(cls, client_host):
        return bool(cls.active_user_token.get(client_host, None))
