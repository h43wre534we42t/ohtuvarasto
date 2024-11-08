from varasto import Varasto

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}\n")

    print(f"Olut getterit:\nsaldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"npaljonko_mahtuu = {olutta.paljonko_mahtuu()}\n")

    part2(part1(mehua, olutta))
def part1(mehua, olutta):
    print("Mehu setterit:")
    mehua.lisaa_varastoon(50.7)
    print(f"Lisätään 50.7\nMehuvarasto: {mehua}")
    mehua.ota_varastosta(3.14)
    print(f"Otetaan 3.14\nMehuvarasto: {mehua}\n")

    print("Virhetilanteita:")
    print(f"Varasto(-100.0):\n{Varasto(-100.0)}")
    print(f"Varasto(100.0, -50.7):\n{Varasto(100.0, -50.7)}\n")
    tupl = (mehua, olutta)
    return tupl

def part2(tupl):
    mehua = tupl[0]
    olutta = tupl[1]
    olutta.lisaa_varastoon(1000.0)
    print(f"Lisätään 1000.0 olueen\nOlutvarasto: {olutta}\n")

    mehua.lisaa_varastoon(-666.0)
    print(f"Lisätään -666.0 mehuun\nMehuvarasto: {mehua}\n")

    saatiin = olutta.ota_varastosta(1000.0)
    print(f"Otetaan 1000.0 oluesta\nsaatiin {saatiin}\nOlutvarasto: {olutta}\n")

    saatiin = mehua.ota_varastosta(-32.9)
    print(f"Otetaan -32.9 mehusta\nsaatiin {saatiin}\nMehuvarasto: {mehua}")

if __name__ == "__main__":
    main()
