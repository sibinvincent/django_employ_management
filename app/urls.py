#import details as details
#import login as login
from django.urls import path

from .views import EmpView, Login, Logout, CreateEmp, Details, Delete, Update, Exp, Index, ChangePassword

urlpatterns = [
         path('emp/', EmpView.as_view(), name='employee'),
         path('login/', Login.as_view(), name='login'),
         path('change-password/', ChangePassword.as_view(), name='change-password'),
         path('', Index.as_view(), name='index'),
         path('logout/', Logout.as_view(), name='logout'),
         path('create/', CreateEmp.as_view(), name='create'),
         path('details/<int:pk>/', Details.as_view(), name='details'),
         path('delete/<int:pk>/', Delete.as_view(), name='delete'),
         path('update/<int:pk>/', Update.as_view(), name='update'),
         path('exp/<int:pk>/', Exp.as_view(), name='exp'),
]
