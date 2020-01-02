from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     CreateAPIView, )
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

from post.api.paginations import PostPagination
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializers, PostUpdateCreateSerializers
from post.models import Post
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,

)


class PostApiView(ListAPIView):
    serializer_class = PostSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def get_queryset(self):
        quryset = Post.objects.filter(draft=False)
        return quryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner, IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
