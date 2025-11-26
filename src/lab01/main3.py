price = float(input("Введите цену: ").replace(",", "."))
discount = float(input("Введите скидку: ").replace(",", "."))
vat = float(input("Введите НДС: ").replace(",", "."))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base}")
print(f"НДС:               {vat_amount}")
print(f"Итого к оплате:    {total}")

# БИВТ - 25 - 2 Машевский Максим
