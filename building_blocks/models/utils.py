class ModelFactoryParams:
    @staticmethod
    def optional_null(optional): return dict(null=True, blank=True) if optional else {}


def generate_field_kwargs(**kwargs):
    field_params = {}
    for k, v in kwargs.items():
        field_params.update(getattr(ModelFactoryParams, k)(v))
    return field_params
