lines = open("input.txt").read().splitlines()
dna = "".join(line[4:].replace(" ", "") for line in lines)

for name, _, seq in map(str.split, open("enzymes.txt").read().splitlines()):
    slice_index, seq = seq.find("^"), seq.replace("^", "").lower()
    index = -1
    while True:
        index = dna.find(seq, index+1)
        if index == -1:
            break
        output = "%s[%s %s]%s" % (
            dna[index-5:index],
            dna[index:index+slice_index],
            dna[index+slice_index:index+len(seq)],
            dna[index+len(seq):index+len(seq)+5]
        )
        print(name, index+slice_index, output)