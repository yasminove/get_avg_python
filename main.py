def get_avg(grades):
  first, *middle, last = grades
  avg = sum(middle) / len(middle)
  print(avg)


# get_avg([23,87,67,98,34])
get_avg([89,87,87,98])
