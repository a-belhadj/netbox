from django import template

from utilities.forms.rendering import InlineFields

__all__ = (
    'getfield',
    'render_custom_fields',
    'render_errors',
    'render_field',
    'render_form',
    'widget_type',
)


register = template.Library()


#
# Filters
#

@register.filter()
def getfield(form, fieldname):
    """
    Return the specified bound field of a Form.
    """
    try:
        return form[fieldname]
    except KeyError:
        return None


@register.filter(name='widget_type')
def widget_type(field):
    """
    Return the widget type
    """
    if hasattr(field, 'widget'):
        return field.widget.__class__.__name__.lower()
    elif hasattr(field, 'field'):
        return field.field.widget.__class__.__name__.lower()
    else:
        return None


#
# Inclusion tags
#

@register.inclusion_tag('form_helpers/render_fieldset.html')
def render_fieldset(form, fieldset, heading=None):
    """
    Render a group set of fields.
    """
    rows = []
    for item in fieldset:
        if type(item) is InlineFields:
            rows.append(
                ('inline', item.label, [form[name] for name in item.field_names])
            )
        else:
            rows.append(
                ('field', None, [form[item]])
            )

    return {
        'heading': heading,
        'rows': rows,
    }


@register.inclusion_tag('form_helpers/render_field.html')
def render_field(field, bulk_nullable=False, label=None):
    """
    Render a single form field from template
    """
    return {
        'field': field,
        'label': label or field.label,
        'bulk_nullable': bulk_nullable,
    }


@register.inclusion_tag('form_helpers/render_custom_fields.html')
def render_custom_fields(form):
    """
    Render all custom fields in a form
    """
    return {
        'form': form,
    }


@register.inclusion_tag('form_helpers/render_form.html')
def render_form(form):
    """
    Render an entire form from template
    """
    return {
        'form': form,
    }


@register.inclusion_tag('form_helpers/render_errors.html')
def render_errors(form):
    """
    Render form errors, if they exist.
    """
    return {
        "form": form
    }
