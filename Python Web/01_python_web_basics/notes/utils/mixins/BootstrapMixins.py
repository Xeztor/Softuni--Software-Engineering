class DisableFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_all_fields()

    def _disable_all_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = ''
