from rest_framework import serializers
from .models import ShortURL
from django.utils.timezone import now

class ShortURLSerializer(serializers.ModelSerializer):
    shortLink = serializers.SerializerMethodField()
    expiry = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['url', 'shortcode', 'validity', 'shortLink', 'expiry']

    def get_shortLink(self, obj):
        host = self.context['request'].get_host()
        return f"http://{host}/{obj.shortcode}"

    def get_expiry(self, obj):
        return obj.expiry.isoformat()
