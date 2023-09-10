from rest_framework import mixins, viewsets


class UpdateDeleteCreateViewSet(mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    pass


class ListRetrieveViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass
