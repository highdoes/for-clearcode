
def hack_calculator(hack):
    try:
        if str(hack).isalpha():
            hack_calc_string(hack)
        else:
            print("Please provide letters only")
    except:
        print("Please provide proper input")

def hack_calc_string(hack):
    code=hack
    code=code.lower()
    a_count=0
    b_count=0
    c_count=0
    for x in code:
        if x=="a" or x=='b' or x=="c":
            if x=="a":
                a_count+=1
            if x == "b":
                b_count += 1
            if x == "c":
                c_count += 1
        else:
            print ("You used letter '{}' in your hack. Only 'a', 'b' and 'c' are accepted.".format(x))
            return 0
    resa=0
    while (a_count>0):
        resa=resa+1*a_count
        a_count-=1
    resb=0
    while (b_count>0):
        resb=resb+2*b_count
        b_count-=1
    resc=0
    while (c_count>0):
        resc=resc+3*c_count
        c_count-=1
    result=resa+resb+resc
    if "baa" in code:
        how_many_baa= code.count("baa")
        code = code.replace("baa","")
        result=result+20*how_many_baa
    if "ba" in code:
        how_many_ba= code.count("ba")
        code = code.replace("ba","")
        result=result+10*how_many_ba

    print("Result is {}".format(result))
    return(result)

