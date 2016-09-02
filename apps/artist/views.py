from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.artist.models import Artist
from apps.artist.serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

