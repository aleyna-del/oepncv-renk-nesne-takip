import cv2
import numpy as np
 
kamera = cv2.VideoCapture(0)
 
while True:
    ret,kare = kamera.read()
#gri'ye çeviririiz görüntüyü çünkü tek renk olursa sadece 0-255 arası tarama yapar ve işler kolaylaşır
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    nesne = cv2.imread("örnnesne.jpg",0)
# "0" diyerek gri rengini aramasını sağlyoruz
    w,h = nesne.shape
    #ilk degeri genişlik ikinci yükseklik
    res = cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED) #bu tarama nın yapıldğı komut
    esik_degeri = 0.8
    loc = np.where(res>esik_degeri)
    for n in zip(*loc[::-1]):
         cv2.rectangle(kare,n,(n[0]+h,n[1]+w),(0,255,0),2) #burada benim nesnemi buldugu yerleri kare içine alıyor
 
    cv2.imshow("ekran",kare)
 
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
 
kamera.release()
cv2.destroyWindow()
