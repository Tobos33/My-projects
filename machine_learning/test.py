import  cv2 
import numpy as np
image_path = "c:/Users/pawko/OneDrive/Pulpit/python/machine_learning/jeden.png"

image = cv2.imread(image_path)[:,:,0]

print("Kształt macierzy:", image.shape)
# Sprawdź, czy obraz został wczytany poprawnie
if image is None:
    print("Nie udało się wczytać obrazu.")
else:
    # Wyświetl obraz
    cv2.imshow("Wczytany obraz", image)

    # Czekaj na dowolny klawisz, aby zamknąć okno
    cv2.waitKey(0)

    # Zamknij wszystkie otwarte okna
    cv2.destroyAllWindows()
