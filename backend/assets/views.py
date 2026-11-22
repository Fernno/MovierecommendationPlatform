from rest_framework import viewsets

from .models import Asset
from .serializers import AssetSerializer
from rest_framework import filters


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Asset


@api_view(['GET'])
def dashboard(request):

    total_assets = Asset.objects.count()

    return Response({
        "total_assets": total_assets
    })

class AssetViewSet(viewsets.ModelViewSet):

    queryset = Asset.objects.all()

    serializer_class = AssetSerializer


    filter_backends = [filters.SearchFilter]

    search_fields = ['name', 'category']

    