## write a code that generate the first n fibbonacci numbers Fn:

def fibbo(n):
    first_seq = [0, 1]
    for i in range(2, n):            # from 2 to nth terms
            first_seq.append(first_seq[i - 1] + first_seq[i - 2]) 
            
            return first_seq[:n]


## test it
n = 10
print(fibbo(n))
