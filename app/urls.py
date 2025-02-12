from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aim/', views.aim, name='aim'),
    path('scope/', views.scope, name='scope'),
    path('team/', views.team, name='team'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('submission/', views.submission, name='submission'),
    # 
    path('volume/<int:journal_id>', views.journal_volume, name='journal_volume'),
    path('issue/<int:journal_id>', views.journal_issue, name='journal_issue'),
    path('paper/<int:journal_id>', views.journal_paper, name='journal_paper'),
    path('paper_view/<int:journal_id>', views.journal_paper_view, name='journal_paper_view'),
    # authentication urls
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]