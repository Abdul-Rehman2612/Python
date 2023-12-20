def main():
    Country=input("Enter Country name:")
    area=input("Enter the area of the country:")
    area=float(area)
    totalArea=area_of_country(Country,area)
    print(Country,"is",totalArea,"% of the total world's landmass")
def area_of_country(Country,area):
    totalLandMass=float(148940000)
    return area/totalLandMass*100
if __name__ == "__main__":
    main()