using System;

public class lib
{
    public void machwas(self) 
    {
        return 42;
    }

    public void krams(int zahl)    
    {
        return zahl * 42;
    }

    public void NikosFunction() 
    {
    // hier könnte ihr Code stehen....
    }
}

public class Person
{
    // Constructor that takes no arguments:
    public Person()
    {
        Name = "unknown";
    }

    // Constructor that takes one argument:
    public Person(string name)
    {
        Name = name;
    }

    // Auto-implemented readonly property:
    public string Name { get; }

    // Method that overrides the base class (System.Object) implementation.
    public override string ToString()
    {
        return Name;
    }
}



