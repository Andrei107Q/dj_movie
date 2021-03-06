from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',  widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.StackedInline):    # добавляем отзывы к фильмам
    model = Reviews
    extra = 1  # колличество дополнительных полей
    readonly_fields = ('name', 'email')


class MovieShortsInline(admin.TabularInline): # TabularInline выводит в одну строку
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_display_links = ('title',)     # ссылка
    list_filter = ('category', 'year')  # фильтр
    search_fields = ('title', 'category__name',)  # поиск
    inlines = [MovieShortsInline, ReviewInline]    # добавляем отзывы к фильмам и кадры из фильма
    save_on_top = True  # перенос кнопки сохранить вверх
    save_as = True  # при сохранении дкопирует старый обьект
    list_editable = ('draft',)  # редактирование не переходятя в детали
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    readonly_fields = ('get_image',)    # для отображения постера
    # fields = (('actors', 'directors', 'genres'), )   # кортеж для вывода в одну строку для редактирования
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline',), )
        }),
        (None, {
            'fields': (('description', 'poster',),  'get_image')
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

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    def unpublish(self, request, queryset):
        # снять с публикации
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запистьобновлена'
        else:
            message_bit = f'{row_update} записей обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        # опубликовать
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 записть обновлена'
        else:
            message_bit = f'{row_update} записей обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')     # заперить редактирование


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")


admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'


# admin.site.register(MovieShots)
#admin.site.register(Actor)
#admin.site.register(RatingStar)
#admin.site.register(Rating)
#admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Reviews)