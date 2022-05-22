import random

class saaboo:

    player_list={}
    removed_players_list={}
    joker_player=0

    def __init__(self) -> None:
        while True:
            starting_count=int(input("enter no of players : "))
            if starting_count < 3:
                print("enter 3 or more")
                continue
            else:
                break
        for i in range(1,starting_count+1):
            name=input("enter p"+str(i)+"'s name : ")
            self.player_list[i]=[name,-1]

    def count(self):
        palm_up=palm_down=0
        for i in self.player_list:
            if self.player_list[i][1] ==  1:
                palm_up+=1
            else:
                palm_down+=1
        return (palm_down,palm_up)

    def remove(self,num):
        new_list={ k:v for k, v in self.player_list.items() if v[1]==num }
        self.removed_players_list = self.removed_players_list | new_list
        print("\n{0}".format(self.player_list))
        if num == 1:
           self.player_list={ k:v for k, v in self.player_list.items() if v[1]==0}
        else:
            self.player_list={ k:v for k, v in self.player_list.items() if v[1]==1}
        print("{0}\n".format(self.player_list))

    def randPlayer(self):
        list=[]
        for key in self.removed_players_list:
            list.append(key)
        self.joker_player= random.choice(list)

    def printWinner(self):
        print("==========================================")
        print("\n")
        print("Contractulations "+list(self.player_list.values())[0][0]+" you won")
        print("\n")
        print("==========================================")

    def removePlayers(self,joker_logic=False):
        if joker_logic:
            count=1
            for value in self.player_list.values():
                if count <3:
                    if value[1] == self.player_list[self.joker_player][1]:
                        self.remove(self.player_list[self.joker_player][1])
                        break
                    count+=1
                else:
                    print("\njoker value is different from others, going for another round\n")
        else:
            (palm_down,palm_up)=self.count()
            if palm_up < palm_down:
                self.remove(1)
            elif palm_down < palm_up:
                self.remove(0)
            else:
                print("\npalm_down is equal to palm_up, going for another round\n")

    def start(self):
        # 0 = palm side down
        # 1 = palm side up
        joker_logic=False
        while len(self.player_list)>1:
            if (len(self.player_list)==2 or joker_logic):
                if not joker_logic:
                    print("\nselecting a random player")
                    self.randPlayer()
                    print(self.removed_players_list[self.joker_player][0]+" is selected as joker\n")
                    self.player_list[self.joker_player]=self.removed_players_list[self.joker_player]
                if joker_logic:
                    self.removePlayers(joker_logic)
                    if len(self.player_list) == 1:
                        self.printWinner()
                        break
                joker_logic=True
            for key in self.player_list:
                while True:
                    choice=int(input("enter your choice "+self.player_list[key][0]+" : "))
                    if (choice in (0,1)):
                        self.player_list[key][1]=choice
                        break
                    else:
                        print("please enter 0 or 1")
                        continue
            if not joker_logic:
                self.removePlayers()

if __name__ == "__main__":
    a=saaboo()
    a.start()