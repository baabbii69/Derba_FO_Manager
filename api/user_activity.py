# # from django.middleware.common import MiddlewareMixin
# # from django.utils.functional import cached_property
import logging


#
#
# # from django.contrib.auth.decorators import login_required
# # from .models import UserActivity
# #
# #
# # class UserActivityMiddleware(MiddlewareMixin):
# #     @cached_property
# #     def user_activity_model(self):
# #         return UserActivity
# #
# #     def process_request(self, request):
# #         if request.user.is_authenticated:
# #             user_activity = self.user_activity_model.objects.create(
# #                 user=request.user
# #             )
# #             request.user_activity = user_activity
# #
# #     def process_response(self, request, response):
# #         user_activity = request.user_activity
# #         user_activity.url = request.META['PATH_INFO']
# #         user_activity.method = request.META['REQUEST_METHOD']
# #         user_activity.save()
# #
# #
# def log_user_activity(level, message, user=None, url=None):
#     logger = logging.getLogger('user_activity')
#     logger.log(level, message, extra={
#         'user': user,
#         'url': url,
#     })

# # def record_user_activity(action):
# #     def decorator(view_func):
# #         @login_required
# #         def wrapper(request, *args, **kwargs):
# #             view_func(request, *args, **kwargs)
# #
# #             if request.user.is_authenticated:
# #                 user_activity = request.user_activity
# #                 user_activity.activity_type = action
# #                 user_activity.save()
# #
# #         return wrapper
# #
# #     return decorator
