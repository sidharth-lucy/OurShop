from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm , UserPasswordChangeForm ,UserPasswordResetForm,UserSetPasswordResetForm

urlpatterns = [
    path('',views.ProductView.as_view() , name ='home'),
    path('product-detail/<int:id>', views.ProductDetailView.as_view(), name='product-detail'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    path('bottomwere/', views.bottomWear, name='bottomWear'),
    path('bottomwere/<slug:data>', views.bottomWear, name='bottomWeardata'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html' ,authentication_form=UserLoginForm), name='login'),
    path('logout/' , auth_views.LogoutView.as_view(next_page='login') , name='logout'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html' ,
        form_class=UserPasswordChangeForm ,success_url='/profile/'), name='changepassword'),
    
    path('password-reset/' , auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',
        form_class=UserPasswordResetForm  ) , name= 'password_reset'),
    path('password-reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html',
        ) , name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class= UserSetPasswordResetForm) ,
         name= 'password_reset_confirm'),
    path('password-reset-complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_completed.html',
        ) , name= 'password_reset_complete'),
    

    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('delete-address/' , views.deleteAddress , name='delete-address'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('show-cart/', views.showcart, name='showcart'),
    path('pluscart/' , views.plus_cart , name='pluscart'),
    path('minuscart/' , views.minus_cart , name='minuscart'),
    path('removecart-item/' , views.remove_cart , name= 'removecart-item'),

    path('orders-continue/', views.orders_continue, name='orders-continue'),
    path('orders/', views.orders, name='orders'),
    
    path('buy/', views.buy_now, name='buy-now'),
    path('checkout/', views.checkout, name='checkout'),

    # path('profile/', views.profile, name='profile'),
    # path('passwordchangedone/' , auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html',
    #         ) , name= "passwordchangedone"),

    # path('changepassword/', views.change_password, name='changepassword'),
    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    # path('', views.home),
    # path('product-detail/<int:id>', views.product_detail, name='product-detail'),
    
]
