print("Hello")
bases = ['A', 'a', 'C', 'c', 'T', 't', 'G', 'g']
complement = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
q =list()

while True:
    seq = input("Enter a DNA sequence or type 'done'\n")
    if seq == "done":
        break
    for char in seq:
        if char not in bases:
            print("Error:",char,"is an invalid character")
    try:
        b =list()
        SEQ = seq.upper()
        SEQ_list = list(SEQ)
        SEQ_list_reverse = SEQ_list[::-1]
        for k in complement:
            for k in SEQ_list_reverse:
                b.append(complement[k])
                if len(b) == len(SEQ_list_reverse):
                    z = "".join(b)
                    if z not in q:
                        q.append(z)
                        y = ", ".join(q)
                        print (z,"has been added to the list")
                    else:
                        print("Error:",z,"entered previously")
    except:
        continue
try:
    print("Sequences:\n","\t",y)
except:
    print ("Done!")
    quit()