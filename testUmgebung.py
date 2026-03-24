
def steuer(brutto, steuersatz):

    steuerwert = brutto * (steuersatz/100)
    print(f"{brutto:.2f} €, {steuersatz:.2f} %, {steuerwert:.2f} €")

steuer(float(input("Brutto: ")), float(input("Steuersatz: ")))
    