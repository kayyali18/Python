## TV
## What? TV is just fine!

class TV (object):
    """A Television Set"""
    def __init__ (self, channel = 1, volume = 0):
        self.channel = channel
        self.volume = volume


    # define a property for what is being watched and how loud it is

    @property
    def watch (self):
        channel_num = self.channel
        if channel_num == 1:
            c = "You are watching the news. To read the news go to \
                \nhttp//:www.reauters.com"
        elif channel_num == 2:
            c = "GOOOOOOAAAAAAALLLLL!!!\
            \n\n\n......If you haven't guessed, you're watching sports!"
        elif channel_num == 3 :
            c = """\t\t\t\tParental Lock Activated:
                    Please Enter Passcode to unlock:
                    _____________
                    | 1 | 2 | 3 |
                    | 4 | 5 | 6 |
                    | 7 | 8 | 9 |
                    |   | 0 |   |
                    _____________
                    """
        elif channel_num == 4:
            c = """Say hello to my little friend.....TATATATATATAAAA!
            That was Scarface by the way"""
        elif channel_num == 5:
            c = "You are now watching C-Span, I recommend changing channels"

        else:
            c = "*Static*"
        return c

    @property
    def hear (self):
        volume_level = self.volume

        if volume_level == 0:
            v = "Mute"
        else:
            v =  "Volume: ", volume_level
        return v


    def change_volume (self):
        print ("Volume up, down or mute? (u,d,m)")
        change = input ("")
        if change == "u":
            self.volume += 1
        elif change == "d":
            self.volume -= 1
        elif change == "m":
            self.volume = 0
        else:
            print ("Invalid choice")
        if self.volume < 0:
            self.volume = 0
        
            
    def change_channel (self):
        print ("Channel up or down? (u or d)")
        change = input ("")
        if change == "u":
            self.channel += 1
        elif change == "d":
            self.channel -= 1
        else:
            print ("Invalid Choice")


    def display_channel (self):
        print (self.watch)
        print ("Channel number is:\t", self.channel)

    def display_volume (self):
        print (self.hear)
        print ("Volume level is:\t", self.volume)





def main ():
    tele = TV ()

    choice = None
    while choice != "0":
        print \
              ("""
            TV WITH 5 CHANNELS

            0 - Quit
            1 - Channel Change
            2 - Volume Change
            3 - View Current Channel and Volume

            """)

        choice = input ("Choice:\t")
        print ()

        if choice == "0":
            print ("Good-bye!")
        elif choice == "1":
            tele.change_channel ()
            tele.display_channel ()
        elif choice == "2":
            tele.change_volume ()
            tele.display_volume ()
        elif choice == "3":
            tele.display_volume ()
            tele.display_channel ()
        else:
            print ("Invalid Choice")

main ()
        
                
