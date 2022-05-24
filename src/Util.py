class Util():
    prompt = "~>"

    def getInt(self, min:int, max:int) -> int:
        ret:int = input(self.prompt)                #!may raise VE
        if ret < min or ret > max:
            raise ValueError                        #!may raise VE
        return ret #TODO test
    
    def getStr(self, min:int=0) -> str:
        ret:str = input(self.prompt)                #!may raise VE
        if len(ret) < min:
            raise ValueError                        #!may raise VE
        return ret #TODO test

    def printBadInput(self, badInput:str="") -> None:
        print("I can't believe you've done this..."
            + "({} is bad input)".format(badInput)
        )
        return #TODO