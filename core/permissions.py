from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAutentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return