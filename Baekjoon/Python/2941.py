word = input()

print(len(word) - word.count("c=") - word.count("c-") - word.count("dz=") - word.count("d-") - word.count("lj") - word.count("nj") - word.count("s=") - word.count("z="))
