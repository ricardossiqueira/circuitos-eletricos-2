from components.Current import Current
from components.Resistor import Resistor


# parse each component to it's own class
def new_component(arr):
    if 'R' in arr[0]:
        return Resistor(arr)
    elif 'I' in arr[0]:
        return Current(arr)
