"""
Program 9.
W cukierni jest 20 paczek cukierków, a w każdej z nich jest od 1 do 50 cukierków.
Napisz program, który po podaniu liczby cukierków w każdej z paczek,
obliczy ile najwięcej cukierków można otrzymać wybierając 4 paczki.
"""

"""
A - przechwoujemy namnjesze pudeklo 
B - przechowujemy 3 pudelka (posortowane)
C - licznik 
D - do wczytywania 
example:
A = 00 00 19
B = 35 29 21

jezeli wczytamy mniej <= 19 to wyrzucamy bo nam nie potrzebne
jezeli wczytamy > 19 to wyrzucamy 19 i mamy 3 przypadki 
 a. 20 => B = 35 29 21 A = 00 00 20
 b. 22 => B = 35 29 22 A = 00 00 21 
 c. 30 => B = 35 30 29 A = 00 00 21
 c. 36 => B = 36 35 29 A = 00 00 21
"""

TESTS =  {
    "scenario1" :{ "result" : 105, "data" : [35, 21, 29, 19, 20] },
    "scenario2" :{ "result" : 125, "data" : [29, 35, 25, 36] },
    "test01_OK": {"result": 181,  "data": [22,15,47,25,46,7,40,43,22,3,45,12,22,30,11,17,15,14,19,12] },
    "test02___": { "result": 173, "data": [30,11,25,3,48,29,27,28,14,21,25,7,32,5,13,49,22,15,27,44] },
    "test03___": { "result": 179, "data": [26,17,43,36,24,19,30,29,15,42,31,15,44,36,50,35,17,21,41,31] },
    "test04_OK": { "result": 175, "data": [44,40,26,38,4,26,46,45,36,27,27,14,10,35,36,37,28,27,4,36] },
    "test05___": { "result": 179, "data": [14,13,18,34,22,24,40,7,1,28,16,13,37,49,26,43,15,1,47,17] },
    "test06_OK": { "result": 164, "data": [1,14,19,18,29,14,1,28,43,42,20,22,9,45,23,6,15,31,34,2] },
    "test07_OK": { "result": 152, "data": [19,11,7,18,38,38,12,13,35,1,5,11,12,30,9,12,38,28,21,38] },
    "test08___": { "result": 178, "data": [45,42,17,25,4,23,48,18,24,26,43,3,16,13,6,5,38,19,21,10] },
    "test09_OK": { "result": 94, "data": [20,10,9,9,4,14,21,5,23,3,19,21,2,7,25,20,25,10,8,17] },
    "test10_OK": { "result": 37, "data": [5,6,1,6,7,6,9,4,9,9,3,1,1,4,4,5,6,7,10,3] },
    "test11_OK": { "result": 74, "data": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] },
    "test12___": { "result": 194, "data": [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50] },
    "my__02???": { "result": 194, "data": [51,24,38,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31] },
}

KROKOW = 0

SUMMARY = []

def oblicz1(test_name, data, expected_result):
    # Use a breakpoint in the code line below to debug your script.
    krokow = 0
    ilosc_pudelek = len(data)
    n = 0
    C = ilosc_pudelek
    A = 0
    B = 0
    BB = [0, 0, 0]
    krokow += 1
    while C > 0:
        krokow += 1
        D = data[n]
        krokow += 1
        n = n + 1
        print(n, "D =", D)
        C = C - 1
        krokow += 1
        if D<=A:
            krokow += 1
            print(f"odrzucam D = {D} bo D  <=  A = {A}")
            print(f"A = {A} B = {BB} C= {C} D = {D}")
            krokow += 1
            continue
        A = D
        D = 0
        krokow += 2
        krokow += 1
        for i in range(3):
            krokow += 1
            D = BB[i]
            krokow += D*4 + 1
            if D < A:
                krokow += 1
                krokow += 1
                krokow += BB[0]*4 + BB[1]*4 + BB[2]*4  + 3
                BB[i] = A
                A = D
                krokow += 1
        print(f"END A = {A} B = {BB} C= {C} D = {D}")

    print(f"FINAL A = {A} B = {BB} C= {C} D = {D}" )
    result = A + BB[0] + BB[1] + BB[2];
    krokow += BB[0]*4 + BB[1]*4 + 1
    print(f"result = {result}")
    krokow += 1
    s = f'{"PASS" if result==expected_result else "FAIL"} LICZ_1 krokow={krokow} Test {test_name}, actual={result} , expected={expected_result}, data={data}'
    SUMMARY.append(s)
    print(s)  # Press Ctrl+F8 to toggle the breakpoint.


def oblicz2(test_name, data, expected_result):
    print("")
    krokow = 0
    ilosc_pudelek = len(data)
    n = 0
    C = ilosc_pudelek
    A = 0
    B = 0
    BB = [0, 0, 0]
    krokow += 1
    while C > 0:
        D = data[n]
        krokow += 2
        n = n + 1
        print(n, "D =", D)
        C = C - 1
        krokow += 1
        if D<=A:
            print(f"odrzucam D = {D} bo D  <=  A = {A}")
            print(f"END A = {A} B = {BB} C= {C} D = {D}")
            krokow += 1
            continue
        A = D
        D = 0
        krokow += 3
        D = BB[0]
        krokow += BB[0]*4
        if A > D:
            print("shift 3")
            krokow += 1
            BB[0] = A
            krokow += A
            A = BB[2]
            krokow += A*4
            BB[2] = BB[1]
            krokow += BB[1] * 4
            BB[1] = D
            krokow += D * 4
            print(f"END A = {A} B = {BB} C= {C} D = {D}")
            continue
        D = BB[1]
        krokow += BB[1] * 4
        if A > D:
            print("shift 2")
            krokow += 1
            BB[1] = A
            krokow += A * 4
            A = BB[2]
            krokow += BB[2] * 4
            BB[2] = D
            krokow += D * 4
            print(f"END A = {A} B = {BB} C= {C} D = {D}")
            continue
        D = BB[2]
        krokow += BB[2] * 4
        if A > D:
            print("shift 1")
            krokow += 1
            BB[2] = A
            krokow += A * 4
            A = D
            print(f"END A = {A} B = {BB} C= {C} D = {D}")
            continue
        print(f"END A = {A} B = {BB} C= {C} D = {D}")

    print(f"FINAL A = {A} B = {BB} C= {C} D = {D}" )
    result = A + BB[0] + BB[1] + BB[2];
    krokow += BB[0] * 4
    krokow += BB[1] * 4
    krokow += 1
    print(f"result = {result}")
    krokow += 1
    s = f'{"PASS" if result==expected_result else "FAIL"} LICZ_2 krokow={krokow} Test {test_name}, actual={result} , expected={expected_result}, data={data}'
    SUMMARY.append(s)
    print(s)  # Press Ctrl+F8 to toggle the breakpoint.

def oblicz3(test_name, data, expected_result):
    global KROKOW

    KROKOW = 0
    A = 0
    B = 0
    C = 0
    D = 0

    print("")
    ilosc_pudelek = len(data)
    n = 0
    C = ilosc_pudelek
    AA = [0, 0, 0]
    # AA = [29, 35, 25]
    # C = 1
    # n = 3

    B = 0
    while C > 0:
        pack = ""
        C = C - 1
        D = data[n]
        n = n + 1
        print(n, "D =", D)
        if D<=B:
            print(f"odrzucam D = {D} bo D  <=  B = {B}")
            print(f"END B = {B} A = {AA} C= {C} D = {D}")
            continue
        B = D
        A2 = AA[0]
        A3 = AA[1]
        A1 = AA[2]
        while A>=10000:
            A = A - 10000
            D = D + 1
        D = A2
        #C = A2
        if B<=D: #A2
            D = A3
            A = A1
            if B <= A1:
                pack = "pack4"
            else:
                pack = "pack3"
        else:
            D = A3
            A = A1
            # B <= A3
            if B <= D:
                pack = "pack2"
            else:
                pack = "pack1"

        A = 0
        if pack == "pack4":
            print(pack)
            AA = [A2, A3, A1]
            A = A1
            while A2>0:
                A2 = A2 - 1
                A = A+10000
            while A3 > 0:
                A3 = A3 - 1
                A = A + 100
        if pack == "pack3":
            print(pack)
            AA = [A2, A3, B]
            D = B
            while A2>0:
                A2 = A2 - 1
                B = B+10000
            while A3 > 0:
                A3 = A3 - 1
                B = B + 100
            A = B
            B =


        if pack == "pack2":
            print(pack)
            AA = [B, A3, A2]
            B = A1
        if pack == "pack1":
            print(pack)
            AA = [A3, B, A2]
            B = A1
        print(f"END B = {B} A = {AA} C= {C} D = {D}")

    print(f"FINAL B = {B} A = {AA} C= {C} D = {D}" )
    result = B + AA[0] + AA[1] + AA[2];
    print(f"result = {result}")
    s = f'{"PASS" if result==expected_result else "FAIL"} LICZ_3 krokow={KROKOW} Test {test_name}, actual={result} , expected={expected_result}, data={data}'
    SUMMARY.append(s)
    print(s)  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("program 9")
    test_data_name =  "scenario2"
    oblicz3(test_data_name, TESTS[test_data_name]["data"], TESTS[test_data_name]["result"])

    # for test_data_name in TESTS.keys():
    #     oblicz1(test_data_name, TESTS[test_data_name]["data"], TESTS[test_data_name]["result"])
    # SUMMARY.append("")
    # for test_data_name in TESTS.keys():
    #     oblicz2(test_data_name, TESTS[test_data_name]["data"], TESTS[test_data_name]["result"])
    #
    SUMMARY.append("")
    for test_data_name in TESTS.keys():
        oblicz3(test_data_name, TESTS[test_data_name]["data"], TESTS[test_data_name]["result"])

    print("---------- SUMMARY ------------------")
    for s in SUMMARY:
        print(s)