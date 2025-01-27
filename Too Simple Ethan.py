One = len([[]])
Five = len([[],[],[],[],[]])
Ten = Five * (One + One)

seventy_two = Ten * (Five + One + One) + One + One
one_hundred_one = Ten ** (One + One) + One
one_hundred_eight = one_hundred_one + Ten - One - One - One
one_hundred_eleven = one_hundred_one + Ten
forty_four = Ten * (Five - One) + Five - One
thirty_two = Ten * (One + One + One) + One + One
eighty_seven = Ten * (Five + One + One + One) + Five + One + One
one_hundred_fourteen = Ten ** (One + One) + Ten + Five - One
one_hundred = Ten ** (One + One)
thirty_three = thirty_two + One

print(chr(seventy_two) + chr(one_hundred_one) + chr(one_hundred_eight) + chr(one_hundred_eight) + chr(
    one_hundred_eleven) + chr(forty_four) + chr(thirty_two) + chr(eighty_seven) + chr(one_hundred_eleven) +
      chr(one_hundred_fourteen) + chr(one_hundred_eight) + chr(one_hundred) + chr(thirty_three))