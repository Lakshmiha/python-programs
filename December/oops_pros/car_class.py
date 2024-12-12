class Cars:
    Company=0
    Price=0
    Colour=0
    def Details(self):
        print("Company:",self.Company)
        print("Price:",self.Price)
        print("Colour:",self.Colour)
        print()
Maruti_XL6=Cars()
Maruti_XL6.Company="Maruti_Suzuki_XL6"
Maruti_XL6.Price=2000000
Maruti_XL6.Colour="Black"
print("Details of first car:")
Maruti_XL6.Details()

Ertiga=Cars()
Ertiga.Company="Maruti_Suzuki_Ertiga"
Ertiga.Price=1500000
Ertiga.Colour="White"
print("Details of second car:")
Ertiga.Details()

i10=Cars()
i10.Company="Honda_i10"
i10.Price=1300000
i10.Colour="Brown"
print("DEtails of third car:")
i10.Details()
