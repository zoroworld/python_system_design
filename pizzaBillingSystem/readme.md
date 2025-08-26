Component (abstract/interface)   
   |
   └── ConcreteComponent  
   |
   └── Decorator (abstract)  
          |
          └── ConcreteDecorator(s)


# Decorator pattern

Pizza (Component - base class / interface)
   |
   └── PlainPizza (Concrete Component)
   |
   └── ToppingDecorator (Abstract Decorator)
          |
          ├── Cheese (Concrete Decorator)
          ├── Olives (Concrete Decorator)
          └── Pepperoni (Concrete Decorator)
