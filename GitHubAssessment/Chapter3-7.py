def sort(x):
    ascend = sorted(x, key = lambda x : x[1])
    descend = sorted(x, key = lambda x : x[1], reverse=True)
    print("Low to High: ",ascend)
    print("High to Low", x)


marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
sort(marks)