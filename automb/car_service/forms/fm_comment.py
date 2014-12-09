from django.core.exceptions import ValidationError
from django.forms import ModelForm
from ..models import UserComment


class CommentForm(ModelForm):

    class Meta:
        model=UserComment
        fields=['stars_service','stars_treatment','stars_cost','comment_content']


