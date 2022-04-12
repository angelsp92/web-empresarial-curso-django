from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') #Mostrar columnas
    ordering = ('author', 'published') #Ordenación predeterminada - Advertencia: Mínimo una coma
    search_fields = ('title', 'content', 'author__username', 'categories__name') #Campo de búsqueda de los campos pasados
    date_hierarchy = 'published' #Gerarquía de fechas
    list_filter = ('author__username','categories__name') #Campos de filtrado

    #definir un campo
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin) #Registrar la categoría y su configuración
admin.site.register(Post, PostAdmin) #Registrar la entrada y su configuración