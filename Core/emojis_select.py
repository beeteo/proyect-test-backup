import random

class Emojiselect:
    def __init__(self):
        self.parser = []
        self.kiss_emoji = ['😍','🥰','😘','💞']

    def get_emoji(self, category):
        if 'kiss' in category:
            get = random.choice(self.kiss_emoji)
            return get