a=[1,2,3,4,5]
e=' '.join(map(str, a))+"\n"
print(e)

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

data = [5, 8, 10, 15, 3]  # Liste de données

# Fonction à appeler lorsque le bouton est pressé
def on_button_clicked(event):
    moyenne = sum(data) / len(data)
    plt.text(0.5, 0.5, f"Moyenne : {moyenne:.2f}", ha='center', va='center', fontsize=12)
    plt.draw()

# Création de la figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Ajuster l'espace en bas pour le bouton

# Position du bouton
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])  # [left, bottom, width, height]

# Création du bouton
button = Button(button_ax, 'Afficher Moyenne')

# Lier la fonction à l'événement "click"
button.on_clicked(on_button_clicked)

plt.show()