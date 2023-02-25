# kolay kullanım 
    # import qrcode
    # code = qrcode.make("https://www.youtube.com")
    # code.save("abcd.png")

# daha geniş kapsamlı kullanımı 

    # import qrcode

    # code = qrcode.QRCode(
    #     version=1,
    #     error_correction = qrcode.ERROR_CORRECT_L,
    #     box_size=50,
    #     border=2
    # )

    # code.add_data("mertçal")
    # image = code.make_image()
    # image.save("deneme.png")


import qrcode
while True:

    veri = input("lütfen qr koda eklemek istediğiniz url yada metni giriniz.\nçıkmak için exit yazın lütfen\n")

    if (veri != "exit"):
        code = qrcode.make(veri)
        isim = input("qr kod dosya ismi :  ")
        uzantı = input("qr kod uzantınızı seçiniz.\n1-)jpg\n2-)png\n")# seçenekler çoğaltılabilir.
        if(uzantı == "1"):
            code.save(isim+".jpg")
            print("programın olduğu konuma jpg dosyanız başarıyla oluştu.")
        elif(uzantı == "2"):
            code.save(isim+".png")
            print("programın olduğu konuma png dosyanız başarıyla oluştu.")
        else:
            print("lütfen geçerli bir değer giriniz.")
            
    else:
        break


