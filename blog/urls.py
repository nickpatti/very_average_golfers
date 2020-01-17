from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CompetitionListView, CompetitionDetailView, CompetitionCreateView, CompetitionUpdateView, CompetitionDeleteView, SocialListView, SocialDetailView, SocialCreateView, SocialUpdateView, SocialDeleteView, TraditionListView, TraditionDetailView, TraditionCreateView, TraditionUpdateView, TraditionDeleteView, LinksPostListView, LinksPostDetailView, LinksPostCreateView, LinksPostUpdateView, LinksPostDeleteView, RollYearListView, RollYearDetailView, RollYearCreateView, RollYearUpdateView, RollYearDeleteView, RollEventListView, RollEventDetailView, RollEventCreateView, RollEventUpdateView, RollEventDeleteView, MembersListView, MembersUpdateView, MembersDetailView, TrophyListView, TrophyDetailView, TrophyCreateView, TrophyUpdateView, TrophyDeleteView, AllTimeListView, AllTimeDetailView, AllTimeCreateView, AllTimeUpdateView, AllTimeDeleteView, ArticlesListView, RollListView
from stylechange.views import TemplateChange

urlpatterns = [
    path('', PostListView.as_view(), name='vag-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    path('members/', MembersListView.as_view(), name='members'),
    path('members/<int:pk>/', MembersDetailView.as_view(), name='members-detail'),
    path('members/<int:pk>/update/', MembersUpdateView.as_view(), name='members-update'),


    path('articles/', ArticlesListView.as_view(), name='articles'),

    path('articles/trophy/', TrophyListView.as_view(), name='trophy-room'),
    path('articles/trophy/<int:pk>/', TrophyDetailView.as_view(), name='trophy-detail'),
    path('articles/trophy/new/', TrophyCreateView.as_view(), name='trophy-create'),
    path('articles/trophy/<int:pk>/update/', TrophyUpdateView.as_view(), name='trophy-update'),
    path('articles/trophy/<int:pk>/delete/', TrophyDeleteView.as_view(), name='trophy-delete'),


    path('articles/competitions/', CompetitionListView.as_view(), name='competitions'),
    path('articles/competitions/<int:pk>/', CompetitionDetailView.as_view(), name='competitions-detail'),
    path('articles/competitions/new/', CompetitionCreateView.as_view(), name='competitions-create'),
    path('articles/competitions/<int:pk>/update/', CompetitionUpdateView.as_view(), name='competitions-update'),
    path('articles/competitions/<int:pk>/delete/', CompetitionDeleteView.as_view(), name='competitions-delete'),

    path('articles/socials/', SocialListView.as_view(), name='socials'),
    path('articles/socials/<int:pk>/', SocialDetailView.as_view(), name='socials-detail'),
    path('articles/socials/new/', SocialCreateView.as_view(), name='socials-create'),
    path('articles/socials/<int:pk>/update/', SocialUpdateView.as_view(), name='socials-update'),
    path('articles/socials/<int:pk>/delete/', SocialDeleteView.as_view(), name='socials-delete'),

    path('articles/traditions/', TraditionListView.as_view(), name='traditions'),
    path('articles/traditions/<int:pk>/', TraditionDetailView.as_view(), name='traditions-detail'),
    path('articles/traditions/new/', TraditionCreateView.as_view(), name='traditions-create'),
    path('articles/traditions/<int:pk>/update/', TraditionUpdateView.as_view(), name='traditions-update'),
    path('articles/traditions/<int:pk>/delete/', TraditionDeleteView.as_view(), name='traditions-delete'),


    path('links/', LinksPostListView.as_view(), name='links'),
    path('links/<int:pk>/', LinksPostDetailView.as_view(), name='links-detail'),
    path('links/new/', LinksPostCreateView.as_view(), name='links-create'),
    path('links/<int:pk>/update/', LinksPostUpdateView.as_view(), name='links-update'),
    path('links/<int:pk>/delete/', LinksPostDeleteView.as_view(), name='links-delete'),

    path('rollhonour/', RollListView.as_view(), name='roll'),

    path('rollhonour/year', RollYearListView.as_view(), name='roll-year'),
    path('rollhonour/year/<int:pk>/', RollYearDetailView.as_view(), name='year-detail'),
    path('rollhonour/year/new/', RollYearCreateView.as_view(), name='year-create'),
    path('rollhonour/year/<int:pk>/update/', RollYearUpdateView.as_view(), name='year-update'),
    path('rollhonour/year/<int:pk>/delete/', RollYearDeleteView.as_view(), name='year-delete'),

    path('rollhonour/event', RollEventListView.as_view(), name='roll-event'),
    path('rollhonour/event/<int:pk>/', RollEventDetailView.as_view(), name='event-detail'),
    path('rollhonour/event/new/', RollEventCreateView.as_view(), name='event-create'),
    path('rollhonour/event/<int:pk>/update/', RollEventUpdateView.as_view(), name='event-update'),
    path('rollhonour/event/<int:pk>/delete/', RollEventDeleteView.as_view(), name='event-delete'),

    path('rollhonour/alltime', AllTimeListView.as_view(), name='roll-alltime'),
    path('rollhonour/alltime/<int:pk>/', AllTimeDetailView.as_view(), name='alltime-detail'),
    path('rollhonour/alltime/new/', AllTimeCreateView.as_view(), name='alltime-create'),
    path('rollhonour/alltime/<int:pk>/update/', AllTimeUpdateView.as_view(), name='alltime-update'),
    path('rollhonour/alltime/<int:pk>/delete/', AllTimeDeleteView.as_view(), name='alltime-delete'),

    path('stylechange/<int:pk>/', TemplateChange.as_view(), name='template-change'),

]
