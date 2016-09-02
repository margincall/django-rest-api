from rest_framework import serializers

from apps.artist.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('nickname',)
