from import_export import resources
from .models import User
  
class UserName(resources.ModelResource):
    
    class Meta:
        model = User
        fields = ('title', 'first', 'last')