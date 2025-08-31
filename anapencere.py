def anamenu():
    print ("anamenu")

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║ English Learning    ║")
    print("║ Asistant            ║")
    print("║  1-Words            ║")
    print("║  2-Grammer çalışması║")
    print("║  3-Quiz             ║")
    print("║  4-İlerleme raporu  ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  8-                 ║")
    print("║  10-Çıkış           ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")


    secim = input("Seçiminizi yapınız (1-7):")
    if secim=="1":
        import moduller.words
        moduller.words.wordsmenu()  
    if secim=="2":
        import moduller.grammer_çalışması
        moduller.grammer_çalışması.grammer_çalışmasımenu()  
    if secim == "3":
        import moduller.quiz
        moduller.quiz.quizmenu()
    if secim == "4":
        import moduller.ilerleme raporu
        moduller.ilerleme raporu.ilerlemeraporumenu()
    if secim == "5":
        import moduller.
        moduller..menu()
    if secim == "6":
        import moduller.
        moduller..menu()
    if secim == "7":
        print("Çıkış")
        exit()

    else:
     print("Geçersiz seçim! Lütfen tekrar deneyin.")    

anamenu()
    
    