class power:
    def __init__(self,base,exp):
        self.base=base
        self.exp=exp
    def execute(self):
        return(self.base**self.exp)