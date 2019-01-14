blacklisted_tokens = []

class RevokedTokenModel(object):
    """ Model class for revoked tokens """

    def add(self, jti):
        """ add token to blacklist """
        blacklisted_tokens.append(jti)

    def inBlacklist(self, jti):
        """ check if token is blacklisted"""
        return bool(jti in blacklisted_tokens)