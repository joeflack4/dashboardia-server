"""ViewModel."""
from .model import UI, ModuleSection, ModuleDashboard


class ViewModel:
    """View model."""
    ignorable_sqlalchemy_attrs = ('query', 'query_class', 'metadata')
    ignorable_base_attrs = ('created_on', 'updated_on', 'metadata_store')
    ignorable_vm_fields = ()
    child_models = ()

    @staticmethod
    def ignorable_attrs():
        """Ignorable attributes."""
        return tuple(attr for attr in dir(ViewModel)) + \
            ViewModel.ignorable_sqlalchemy_attrs + \
            ViewModel.ignorable_base_attrs

    @classmethod
    def ignore(cls, attr):
        """Ignore attr?"""
        if attr.startswith('_') or attr in cls.ignorable_attrs() \
                or hasattr(cls, 'ignorable_vm_fields') \
                and attr in cls.ignorable_vm_fields:
            return True
        return False

    @classmethod
    def set_attr(cls, obj, attr):
        """Set attribute."""
        attribute = getattr(obj, attr)
        if attr not in cls.child_models:
            return attribute
        else:
            return cls.child_models[attr]['view_model'](obj)

    # noinspection PyUnresolvedReferences
    @classmethod
    def instances(cls, models=None, headered=False):
        """Set attributes."""
        models = models if models else cls.query.all()

        if headered:
            return {
                instance.name: {
                    attr: cls.set_attr(obj=instance, attr=attr)
                    for attr in dir(instance)
                    if not cls.ignore(attr)
                }
                for instance in [i for i in models]
            }

        return [
            {
                attr: cls.set_attr(obj=instance, attr=attr)
                for attr in dir(instance)
                if not cls.ignore(attr)
            }
            for instance in [i for i in models]
        ]


class UiViewModel(UI, ViewModel):
    """UI view model."""


# from operator import itemgetter

class ModuleSectionViewModel(ModuleSection, ViewModel):
    """Module section view model."""

    child_models = {
        'children_dashboards': {
            'view_model': lambda x:
            ModuleDashboardViewModel.instances(models=x.children_dashboards)
        }
    }


class ModuleDashboardViewModel(ModuleDashboard, ViewModel):
    """UI view model."""
    ignorable_vm_fields = ('parent_section', 'parent_section_name', 'section')


store = {
    'ui': UiViewModel.instances(headered=True),
    # 'module_section': [[x.name for x in i.children_dashboards]
    'sections': ModuleSectionViewModel.instances(headered=True)
}
