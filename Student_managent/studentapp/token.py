from rest_framework_simplejwt.tokens import RefreshToken

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refres" : str(refresh),
        "access" : str(refresh.access_token)
    }
