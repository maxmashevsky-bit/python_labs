f = input("ФИО: ")
fio = f.strip()
c = fio.split()
с1 = sum(len(w) for w in c)
i = "".join(p[0].upper() for p in c) + "."
print("Инициалы:", i)
print("Длина (символов):", с1 + 2)
# БИВТ - 25 - 2 Машевский Максим
