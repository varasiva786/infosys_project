class Siva_to_sum_palindram_square:
  def __init__(self,a):
    self.a=a

  def display(self):
    if isinstance(self.a,tuple):
      sum=0
      for i in self.a:
          sum=sum+i
      return sum  
    elif isinstance(int,self.a):
      return self.a * self.a
    elif isinstance(str, self.a):
      return self.a=self.a[::-1]

sum=Siva_to_sum_palindram_square((1,2,3,4,5))
print(sum.display())

      
      
