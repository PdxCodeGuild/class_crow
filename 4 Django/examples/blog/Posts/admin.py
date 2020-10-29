from django.contrib import admin

from Posts.models import Joke

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    list_display = ('category', 'punchline')