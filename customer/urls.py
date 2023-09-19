from django.urls import path
from customer import views

urlpatterns=[
    path("register",views.SignUpView.as_view(),name="register"),
    path("",views.SignInView.as_view(),name="signin"),
    path("customers/home",views.HomeView.as_view(),name="user-home"),
    path("products/details/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/carts/<int:id>/add",views.addto_cart,name="add-cart"),
    path("carts/all",views.CartListView.as_view(),name="cart-list"),
    path("carts/all/<int:id>/remove",views.DeleteCart.as_view(),name="cart-delete"),
    path("orders/add/<int:cid>/<int:pid>",views.OrderView.as_view(),name="place-order"),
    path("orders/all",views.MyOrderView.as_view(),name="my-orders"),
    path("orders/<int:id>/remove",views.CancelOrder_View,name="order-cancel"),
    path("customers/accounts/signout",views.logout_View,name="signout"),
    path("product/myproduct",views.ProductView.as_view(),name="myproduct"),
    path("products/add",views.ProductCreateView.as_view(),name="add"),
]
