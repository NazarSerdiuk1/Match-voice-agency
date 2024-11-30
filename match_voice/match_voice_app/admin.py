from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Tournament,Commentator,Match


@admin.register(Commentator)
class CommentatorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "username"
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("tournament",)


admin.site.register(Tournament)
