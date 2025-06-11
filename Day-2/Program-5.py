class CompConfig:
    def __init__(self,processor,ram,rom,gpu):
        self.processor = processor
        self.ram = ram
        self.rom = rom
        self.gpu = gpu
    def display(self):
        print("Processor:",self.processor)
        print("RAM:",self.ram)
        print("ROM:",self.rom)
        print("GPU:",self.gpu)

n1 = CompConfig("Intel i3","16gb","512gb","nVidia")
n2 = CompConfig("Amd 5","16gb","1 Tb","nVidia")
n1.display()
n2.display()