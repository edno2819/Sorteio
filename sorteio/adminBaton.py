from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


BATON_SETTINGS = {
    'SITE_HEADER': 'Sorteio',
    'SITE_TITLE': 'Sorteio',
    'INDEX_TITLE': 'Site admin',
    'SUPPORT_HREF': '',
    'COPYRIGHT': '', # noqa
    'POWERED_BY': '<a href="https://www.otto.to.it">Edno Almeida</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': True,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '72261.png',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    'MENU': (
        { 'type': 'title', 'label': 'Menu', 'apps': ('auth','card' ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {
            'type': 'app',
            'name': 'card',
            'label': 'Cards',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'Card',
                    'label': 'Cards'
                },
                {
                    'name': 'Disciplina',
                    'label': 'Disciplinas'
                },
            )
        },
    ),
}