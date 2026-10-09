# Normal function 
print("Normal function") 
def button_click():
    count = 0
    count += 1
    print(count)
button_click()
button_click()
button_click()
button_click()
# count = 0
#    ↓
# count = 1
#    ↓
# print 1
#    ↓
# function finishes → count is gone

# so the function doesnot remember the previous count

# Callable object 
print("Callable object") 

class ButtonClicks:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count +=1
        print(self.count)

button_clicks = ButtonClicks()
button_clicks()
button_clicks()
button_clicks()
button_clicks()
button_clicks()
button_clicks()
button_clicks()
button_clicks()

# | Normal function | Callable object |
# |---|---|
# | `button_click()` | `button_clicks()` |
# | It is a function | It is an object |
# | Local variables usually disappear after the call | Object attributes remain |
# | Doesn't automatically remember previous calls | Can remember state |
# | `button_click()` | `button_clicks()` works because of `__call__()` |