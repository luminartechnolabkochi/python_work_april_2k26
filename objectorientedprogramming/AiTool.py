

class AItool:

    name:str
    vendor:str
    model:str

    def set_attributes(self,name,vendor,model):

        self.name =name

        self.vendor = vendor

        self.model = model



    def chat(self):

        print("ai model chatting.....")

    def image_generation(self):

        print("ai model image generation....")


gpt = AItool()


claude = AItool()

claude.set_attributes("claude","anthropic","anthropic-5")





