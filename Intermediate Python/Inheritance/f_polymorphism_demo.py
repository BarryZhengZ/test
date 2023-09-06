# This program demonstrates polymorphism.


import f_animals as animals

def main():
   # Create a Mammal object, a Dog object, and
   # a Cat object.
   mammal = animals.Mammal('regular animal')
   dog = animals.Dog()
   cat = animals.Cat()


  
   # Display information about each one.
   print('Here are some animals and')
   print('the sounds they make.')
   print('--------------------------')
   show_mammal_info(mammal)
   show_mammal_info(dog)
   show_mammal_info(cat)
   '''
   mammal.show_species()
   mammal.make_sound()


   print()


   dog.show_species()
   dog.make_sound()


   print()


   cat.show_species()
   cat.make_sound()
   '''
def show_mammal_info(creature):
   if isinstance(creature, animals.Mammal):
       creature.show_species()
       creature.make_sound()
   else:
       print(f"{creature} does not belong  to the Mammal class object")
# Call the main function.
main()



