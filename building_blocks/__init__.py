__version__ = '0.0.2-dev3'
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace('-', '.', 1).split('.')
    ]
)
