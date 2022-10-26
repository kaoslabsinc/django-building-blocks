from rest_framework import serializers


class NameSlugSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name', 'slug',
        )
        lookup_field = 'slug'


class HasUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'uuid',
        )
        lookup_field = 'uuid'


class SluggedKaosModelSerializer(serializers.ModelSerializer):
    class Meta(NameSlugSerializer.Meta):
        fields = (
            *HasUUIDSerializer.Meta.fields,
            *NameSlugSerializer.Meta.fields,
            'created',
            'modified',
        )


__all__ = [
    'NameSlugSerializer',
    'HasUUIDSerializer',
]
