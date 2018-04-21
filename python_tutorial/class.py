class Champion(object):
    # League of Legends Champion Class
    def __init__(self, hp, mp, skilltype, fun_score=None):
        self.__hp = hp
        self.__mp = mp
        self.__skilltype = skilltype
        self.__fun_score = fun_score

    def get_hp(self):
        return self.__hp

    def get_mp(self):
        return self.__mp

    def get_fun(self):
        return self.__fun_score

    def set_fun(self, score):
        if 0 < score <= 100:
            self.__fun_score = score
        else:
            raise ValueError("you can only have 100 score of fun, and you can't not having fun")

    def get_difficulty(self):
        if self.__skilltype is 'right click':
            return 'easy'
        elif self.__skilltype is 'mix':
            return 'medium'
        else:
            return 'hard'

class Annie(Champion):
