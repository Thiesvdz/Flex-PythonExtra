from PIL import Image, ImageFont, ImageDraw


# Laad de achtergrond afeebdling in de variabele: achtergrond
achtergrond = Image.open("Obamium.jpg")

# Afmetingen opslaan in eigen variabelen
breedte = achtergrond.width
hoogte = achtergrond.height

# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 40)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Obama"
tekengebied.multiline_text((260,7), tekst, font=lettertype, fill=(0,0,0))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))
