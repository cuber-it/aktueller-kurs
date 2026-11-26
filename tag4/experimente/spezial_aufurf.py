def funktion_a(n):
   print("A:", n)
   if n > 0:
       funktion_b(n - 1)
       
def funktion_b(n):
   print("B:", n)
   if n > 0:
       funktion_a(n - 1)
funktion_a(4)
