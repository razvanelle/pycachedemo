from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import prjcache
from .models import Project
from .serializers import ProjectSerializer

# @permission_classes((AllowAny,))
@api_view()
def update(request):
    time = request.query_params.get('time')
    if (time is None):
        return Response('ERROR: No time!', status.HTTP_400_BAD_REQUEST)
    print('=== CACHE REQ Time=', time)
    res = prjcache.getupdates(time)
    return Response(str(list(res)))


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer  

    def get_queryset(self): 
      queryset = Project.objects.all()

      # Query format: /projects/?id=2,5,23
      idQuery = self.request.GET.get('id', None) 
      
      if idQuery is not None and idQuery != '':
        ids = [int(x) for x in idQuery.split(',')]
        queryset = queryset.filter(id__in=ids)
        return queryset[:50]

      return queryset
