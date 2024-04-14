from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artist.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserProfileViewset, UserPasswordResetView, UserProfileUploadImageView

router = DefaultRouter()
router.register('user-profile', UserProfileViewset, basename='user-profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('my-profile/', UserProfileViewset.as_view({'get': 'retrieve', 'put': 'update'}), name='profile'),
    # path('profile/update/', UserProfileUploadImageView.as_view(), name='profile_update'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('password-reset-email/', SendPasswordResetEmailView.as_view(), name='password-reset-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]