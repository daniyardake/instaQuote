from . import language

strings = {
    'no_translation': {
        'en': 'Sorry, this word is not translated yet',
        'ru': 'Извините, данный текст не переведен'
    },
    'user_not_exists': {
        'en': 'User does not exist',
        'ru': 'Пользователь не существует'
    },
    'user_exists': {
        'en': 'User already exists',
        'ru': 'Такой пользователь уже существует'
    },
    'error': {
        'en': 'Error',
        'ru': 'Ошибка'
    }
}


class StringParser:
    @staticmethod
    def get(word, language=language):
        return strings.get(word, 'no_translation')[language]
