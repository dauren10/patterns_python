'''
Это пустой интерфейс (без полей или методов). Примерами интерфейса маркера являются сериализуемый, клонируемый и удаленный интерфейс. Все эти интерфейсы являются пустыми интерфейсами.
Клонируемый интерфейс: Клонируемый интерфейс присутствует в пакете java.lang. В классе Object есть метод clone(). Класс, который реализует интерфейс Cloneable, указывает, что для метода clone() допустимо создание полевой копии экземпляров этого класса.
Вызов метода clone объекта Object для экземпляра класса, который не реализует интерфейс Cloneable, приводит к возникновению исключения CloneNotSupportedException. По соглашению классы, реализующие этот интерфейс, должны переопределять метод Object.clone().'''


// Java program to illustrate Cloneable interface
import java.lang.Cloneable;

// By implementing Cloneable interface
// we make sure that instances of class A
// can be cloned.
class A implements Cloneable
{
	int i;
	String s;

	// A class constructor
	public A(int i,String s)
	{
		this.i = i;
		this.s = s;
	}

	// Overriding clone() method
	// by simply calling Object class
	// clone() method.
	@Override
	protected Object clone()
	throws CloneNotSupportedException
	{
		return super.clone();
	}
}

public class Test
{
	public static void main(String[] args)
		throws CloneNotSupportedException
	{
		A a = new A(20, "GeeksForGeeks");

		// cloning 'a' and holding
		// new cloned object reference in b

		// down-casting as clone() return type is Object
		A b = (A)a.clone();

		System.out.println(b.i);
		System.out.println(b.s);
	}
}
