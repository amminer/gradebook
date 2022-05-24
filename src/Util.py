class Util():
    prompt = "~>"

    def getInt(self, min:int, max:int) -> int:
        ret:int = input()               #!may raise VE
        if ret < min or ret > max:
            raise ValueError            #!may raise VE
        return ret #TODO test
    
    def getStr(self, min:int=0) -> str:
        return "TODO" #TODO

    def printBadInput(self, badInput:str="") -> None:
        return #TODO