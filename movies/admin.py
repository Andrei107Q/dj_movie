from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.StackedInline):    # добавляем отзывы к фильмам
    model = Reviews
    extra = 1  # колличество дополнительных полей
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_display_links = ('title',)     # ссылка
    list_filter = ('category', 'year')  # фильтр
    search_fields = ('title', 'category__name',)  # поиск
    inlines = [ReviewInline]    # добавляем отзывы к фильмам
    save_on_top = True  # перенос кнопки сохранить вверх
    save_as = True  # при сохранении дкопирует старый обьект
    list_editable = ('draft',)  # редактирование не переходятя в детали
    # fields = (('actors', 'directors', 'genres'), )   # кортеж для вывода в одну строку для редактирования
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline',), )
        }),
        (None, {
            'fields': (('description', 'poster'),)
        }),
        (None, {
            'fields': (('year', 'word_premiere', 'country'),)
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fess_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft',),)
        }),
    )

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')     # заперить редактирование


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'ip')


# admin.site.register(MovieShots)
#admin.site.register(Actor)
#admin.site.register(RatingStar)
#admin.site.register(Rating)
#admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Reviews)