from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer


@api_view(['GET'])
def hotel_list(request):
    """List all active (non-deleted) hotels."""
    hotels = Hotel.objects.filter(is_deleted=False)
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def hotel_detail(request, pk):
    """Retrieve a single active hotel by ID."""
    hotel = get_object_or_404(Hotel, pk=pk, is_deleted=False)
    serializer = HotelSerializer(hotel)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def hotel_create(request):
    """Create a new hotel entry."""
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def hotel_update(request, pk):
    """Update an existing active hotel."""
    hotel = get_object_or_404(Hotel, pk=pk, is_deleted=False)
    serializer = HotelSerializer(hotel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def hotel_delete(request, pk):
    """Soft delete a hotel (mark as deleted)."""
    hotel = get_object_or_404(Hotel, pk=pk, is_deleted=False)
    hotel.is_deleted = True
    hotel.save()
    return Response({"message": "Hotel soft deleted."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def hotel_history(request):
    """View all soft-deleted hotels."""
    deleted_hotels = Hotel.objects.filter(is_deleted=True)
    serializer = HotelSerializer(deleted_hotels, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def hotel_restore(request, pk):
    """Restore a soft-deleted hotel."""
    hotel = get_object_or_404(Hotel, pk=pk, is_deleted=True)
    hotel.is_deleted = False
    hotel.save()
    return Response({"message": "Hotel restored successfully."}, status=status.HTTP_200_OK)


'''

| Method | Endpoint                    | Description             |
| ------ | --------------------------- | ----------------------- |
| GET    | `/api/hotels/`              | List all active hotels  |
| POST   | `/api/hotels/create/`       | Create a hotel          |
| GET    | `/api/hotels/<id>/`         | Get hotel details       |
| PUT    | `/api/hotels/<id>/update/`  | Update a hotel          |
| DELETE | `/api/hotels/<id>/delete/`  | Soft delete a hotel     |
| GET    | `/api/hotels/history/`      | View deleted hotels     |
| POST   | `/api/hotels/<id>/restore/` | Restore a deleted hotel |

'''