"""
Something Good as Indicated
"""
from mz_welcome_message import welcome_message
from mz_class import Hero 


    
def main():
   welcome_message()

   eevee = Hero("Eevee", 8, "Fire", 100, 20, 50)
   print(eevee.name)


if __name__ == "__main__":
    main()
    
main()
