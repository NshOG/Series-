# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։
#

class Serial:
    def __init__(self, name, platform, episode, your_episode, cast, rate=None):
        if self.isvalid_string(name) and self.isvalid_string(platform) and self.isvalid_digit(your_episode) and \
                self.isvalid_digit(episode) and self.isvalid_cast(cast) and self.isvalid_rate(rate):
            self.__name = name
            self.__platform = platform
            self.__episode = episode
            self.__your_episode = your_episode
            self.__cast = cast
            self.__rate = rate
            print("series created")
        else:
            raise ValueError("invalid input")

    def add_cast(self):
        actor = input("actor to add | ")
        self.__cast.append(actor)
        return f"{actor} is added to cast"

    def del_cast(self):
        actor = input("actor to delete | ")
        if actor in self.__cast:
            self.__cast.remove(actor)
            return f"{actor} is removed from cast"
        else:
            return f"{actor} is not in cast"

    def getinfo(self):
        info = open("InfoBB.txt", "r+")
        return info.read()

    @staticmethod
    def isvalid_string(name):
        return type(name) is str

    @staticmethod
    def isvalid_digit(digit):
        return type(digit) is int

    @staticmethod
    def isvalid_rate(digit):
        return type(digit) is int and 0 <= digit <= 10

    @staticmethod
    def isvalid_cast(lst):
        return type(lst) is list

    @property
    def name(self):
        return self.__name

    @property
    def platform(self):
        return self.__platform

    @property
    def episode(self):
        return self.__episode

    @property
    def your_episode(self):
        return self.__your_episode

    @property
    def cast(self):
        return self.__cast

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def set_rate(self, rate):
        if not self.isvalid_rate(rate):
            return "invalid input"
        else:
            self.__rate = rate

    @your_episode.setter
    def setepisode(self, episode):
        if not self.isvalid_digit(episode):
            return "Invalid input"
        else:
            self.__your_episode = episode





myseries = Serial("Breaking Bad", "Stremio", 2008, 5,
                  ["Bryan Cranston", "Aaron Paul", "Anna Gunn", "Dean Norris", "RJ Mitte"], 10)

# print(myseries.add_cast())
# print(myseries.del_cast())

print(myseries.getinfo())
print(myseries.set_rate(rate=5))