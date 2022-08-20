import random

class percentage:
    def __init__(self):
        self.user = ''

    def relation_percentage(self):
        percentage = ['0%', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%', '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%']
        
        get_percentage = random.choice(percentage)
        
        if get_percentage == '0%':
            return '**{}** Not at all, you are not compatible at all, I think that even friends would not work'.format(get_percentage)
        elif get_percentage == '5%':
            return '**{}** They are not compatible at all, I think with luck they could make a friend'.format(get_percentage)
        elif get_percentage == '10%':
            return '**{}** They are not compatible in but if they know each other it is possible that they have a "friendship"'.format(get_percentage)
        elif get_percentage == '15%':
            return '**{}** They are fairly compatible, it is possible that they will become friends in the future'.format(get_percentage)
        elif get_percentage == '20%':
            return '**{}** They are fairly compatible, it is possible that they will become friends in the future'.format(get_percentage)
        elif get_percentage == '25%':
            return '**{}** They are fairly compatible, it is possible that they will become friends in the future'.format(get_percentage)
        elif get_percentage == '30%':
            return '**{}** They are moderately compatible although they can make friends easily'.format(get_percentage)
        elif get_percentage == '35%':
            return '**{}** They are moderately compatible although they can make friends easily'.format(get_percentage)
        elif get_percentage == '40%':
            return '**{}** They are compatible, its just getting to know each other so they can be friends.'.format(get_percentage)
        elif get_percentage == '45%':
            return '**{}** They are compatible, its just getting to know each other so they can be friends.'.format(get_percentage)
        elif get_percentage == '50%':
            return '**{}** They are compatible and it is possible that they can make a very good friendship'.format(get_percentage)
        elif get_percentage == '55%':
            return '**{}** They are compatible and it is possible that they can make a very good friendship'.format(get_percentage)
        elif get_percentage == '60%':
            return '**{}** They are very compatible and can easily be best friends.'.format(get_percentage)
        elif get_percentage == '65%':
            return '**{}** They are very compatible and can easily be best friends.'.format(get_percentage)
        elif get_percentage == '70%':
            return '**{}** They are very compatible and can easily be best friends.'.format(get_percentage)
        elif get_percentage == '75%':
            return '**{}** They are so compatible I dont know what they do but they can be best friends right now!'.format(get_percentage)
        elif get_percentage == '80%':
            return '**{}** They are so compatible I dont know what they do but they can be best friends right now!'.format(get_percentage)
        elif get_percentage == '85%':
            return '**{}** Well, they are very compatible, they can make a nice couple if you are lucky.'.format(get_percentage)
        elif get_percentage == '90%':
            return '**{}** Well, they are very compatible and they can be a couple if they want one day.'.format(get_percentage)
        elif get_percentage == '95%':
            return '**{}** Well, they are very compatible and they can be a couple if they want one day.'.format(get_percentage)
        elif get_percentage == '100%':
            return '**{}** This is very serious, you can form a marriage right now if you wish, since you are made for each other.'.format(get_percentage)
