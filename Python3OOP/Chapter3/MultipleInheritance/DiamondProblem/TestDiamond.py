#from Diamond import Subclass
from Diamond_solved import Subclass

s = Subclass()
s.call_me()

print(
        s.num_sub_calls,
        s.num_left_calls,
        s.num_right_calls,
        s.num_base_calls)
