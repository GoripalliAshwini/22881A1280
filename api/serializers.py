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
class ShortURLStatsSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField()
    expiresAt = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['shortcode', 'url', 'createdAt', 'expiresAt']

    def get_createdAt(self, obj):
        return obj.created_at.isoformat()

    def get_expiresAt(self, obj):
        return obj.expiry.isoformat()
