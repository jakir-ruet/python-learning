class carDesign:
    def __init__(self, brand, name, model):
        self.Brand = brand
        self.Name = name
        self.Model = model
        self.Wheel = 4

    def show(self):
        print(
            "Brand name",
            self.Brand,
            "Car name",
            self.Name,
            "Model",
            self.Model,
            "Total wheel",
            self.Wheel,
        )


carObj1 = carDesign("Toyata", "GreenDown", "HG903")
carObj1.show()
