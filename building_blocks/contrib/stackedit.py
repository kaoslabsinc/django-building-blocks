from dj_kaos_utils.admin.utils import render_element
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from django.utils.html import format_html

from building_blocks.admin import AdminBlock
from building_blocks.consts.field_names import NOTES


class StackEditJSMedia:
    css = {
        'all': (
            'stackedit/stackedit.css',
        )
    }
    js = (
        'https://unpkg.com/stackedit-js@1.0.7/docs/lib/stackedit.min.js',
        'stackedit/stackedit.js',
    )


class StackEditMarkdownTextarea(AdminTextareaWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Media(StackEditJSMedia):
        pass

    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)

        button_html = render_element('button', format_html("<sup>⇱</sup><sub>⇲</sub>"), attrs={
            'type': 'button',
            'onclick': f'runStackEditCode(`id_{name}`, `{name}`)',
            'class': 'open-stackedit-btn',
        })
        span_html = render_element('span', input_html + button_html, attrs={'class': 'stackedit-wrapper'})

        return span_html


class HasNotesAdminBlock(AdminBlock):
    readonly_fields = (
        # 'notes_display',
    )
    the_notes_fieldset = ("Notes", {'fields': (
        NOTES,
        # 'notes_display',
    ), 'classes': ('collapse', 'collapsed',)})


class HasMarkdownNotesAdmin(admin.ModelAdmin):
    markdown_editor = StackEditMarkdownTextarea
    fieldsets = (
        HasNotesAdminBlock.the_notes_fieldset,
    )
    readonly_fields = HasNotesAdminBlock.readonly_fields

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # Check if the field is the "notes" field
        if db_field.name == 'notes':
            # Use the DarkModeSimpleMDEField widget for the "notes" field
            kwargs['widget'] = self.markdown_editor()

        # Return the form field
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    @admin.display(description="rendered notes")
    def notes_display(self, obj):
        pass
        # html = markdown2.markdown(obj.notes)
        # return render_element('iframe', "", attrs={'srcdoc': format_html(html)})


__all__ = (
    'HasMarkdownNotesAdmin',
)
