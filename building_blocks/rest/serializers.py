from rest_framework import serializers

from building_blocks.consts.field_names import *


class NameSlugSerializer(serializers.ModelSerializer):
    """Serializer for NameSlug"""
    class Meta:
        fields = (
            NAME, SLUG,
        )
        lookup_field = SLUG


class HasUUIDSerializer(serializers.ModelSerializer):
    """Serializer for HasUUID"""
    class Meta:
        fields = (
            UUID,
        )
        lookup_field = UUID


class SluggedKaosModelSerializer(serializers.ModelSerializer):
    """Serializer for SluggedKaosModel"""
    class Meta(NameSlugSerializer.Meta):
        fields = (
            *HasUUIDSerializer.Meta.fields,
            *NameSlugSerializer.Meta.fields,
            CREATED,
            MODIFIED,
        )


class CurrentProfileDefault(serializers.CurrentUserDefault):
    """
    Rest serializer field to set default value for a profile field, if the user has the profile

    Example:
        >>> class MyModelSerializer(serializers.Serializer):
        >>>     profile = UserProfileSerializer(default=CurrentProfileDefault(UserProfile))
    """
    requires_context = True

    def __init__(self, profile_cls):
        self.profile_cls = profile_cls

    def __call__(self, serializer_field):
        user = serializer_field.context['request'].user
        # If a user has access to the API, we can create a profile for them
        return self.profile_cls.objects.get_or_create(user=user)[0]


__all__ = [
    'NameSlugSerializer',
    'HasUUIDSerializer',
    'SluggedKaosModelSerializer',
    'CurrentProfileDefault',
]
