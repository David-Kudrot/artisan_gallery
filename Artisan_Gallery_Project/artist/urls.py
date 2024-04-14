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
    # path('profile/update/', UserProfileUploadImageView.as_view(), name='profile_update'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]