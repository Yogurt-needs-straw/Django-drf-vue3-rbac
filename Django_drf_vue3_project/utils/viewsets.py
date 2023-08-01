from  rest_framework.viewsets import GenericViewSet as DrfGenericViewSet
from rest_framework import mixins


class GenericViewSet(DrfGenericViewSet):
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if response.exception:
            return response

        response.data = {'code': 0, 'data': response.data}
        return response

class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    pass

