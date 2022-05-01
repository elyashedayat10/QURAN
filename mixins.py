from django.contrib.auth.mixins import UserPassesTestMixin


class AnonymousUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous
