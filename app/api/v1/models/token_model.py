blacklisted_tokens = []

class RevokedTokenModel(object):
    """ Model class for revoked tokens """

    def add(self, jti):
        """ Function to save token identifier """
        blacklisted_tokens.append(jti)

    def inBlacklist(self, jti):
        """ Function to check if token identifier is blacklisted """
        return bool(jti in blacklisted_tokens)