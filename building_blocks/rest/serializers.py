from rest_framework import serializers

from building_blocks.consts.field_names import *


class NameSlugSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            NAME, SLUG,
        )
        lookup_field = SLUG


class HasUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            UUID,
        )
        lookup_field = UUID


class SluggedKaosModelSerializer(serializers.ModelSerializer):
    class Meta(NameSlugSerializer.Meta):
        fields = (
            *HasUUIDSerializer.Meta.fields,
            *NameSlugSerializer.Meta.fields,
            CREATED,
            MODIFIED,
        )


__all__ = [
    'NameSlugSerializer',
    'HasUUIDSerializer',
]
