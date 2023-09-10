from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Post, Group, Follow


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        read_only=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['user', 'following']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                {'Вы не можете подписаться на самого себя'}
            )
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        source='author.username',
        default=serializers.CurrentUserDefault(),
        read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('post', )
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        source='author.username',
        read_only=True,
        default=serializers.CurrentUserDefault(),)

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date')
        model = Post
