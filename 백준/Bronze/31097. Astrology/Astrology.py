_,M,D=map(int,input().split("-"))
t=M*30+D
print(("Capricorn","Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius")[-1*((t<50)+(t<79)+(t<111)+(t<140)+(t<171)+(t<201)+(t<233)+(t<263)+(t<293)+(t<323)+(t<353)+(t<382))])