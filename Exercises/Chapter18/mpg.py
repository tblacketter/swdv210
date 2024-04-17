from dataclasses import dataclass

@dataclass
class MPG():
    milesDriven:float = 0.0
    gallonsOfGasUsed:int = 0

    def calculate_mpg(self)->float:
        mpg = self.milesDriven/self.gallonsOfGasUsed
        return round(mpg, 2)