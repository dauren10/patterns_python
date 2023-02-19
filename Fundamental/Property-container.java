'''
Контейнер свойств — это класс, свойства которого можно настраивать во время выполнения без необходимости редактирования определения класса.

В этой статье есть единственный подробный пример, который я смог найти. В нем они используют пример настраиваемого класса Movie.

Базовый класс PropertyContainer предоставляет методы для добавления/удаления/извлечения свойств, хранящихся в классе. По сути, он очень похож на HashMap:
'''
'''Классическим примером использованием шаблона является приложение, используемое для хранения и классификации информации. Например, приложение заказа фильмов[1]. При разработке класса, представляющего фильм, при разработке и запуске приложения невозможно предусмотреть все возможные свойства (атрибуты), описывающие фильм. Поэтому класс фильма при необходимости в любой момент может быть расширен дополнительными свойствами. Для этого требуются предусмотреть механизм расширения свойств перед выпуском приложения.

Контейнер свойств, предоставляет механизм для динамического расширения объектов дополнительными атрибутами во время выполнения. Кроме этого, приложению могут потребоваться ещё модули, которые явным образом используют преимущества нового свойства, если оно было добавлено. 

'''
/// <summary>Реализация класса фильма, с контейнером свойств.</summary>
public class MovieImplementation
{
      private Hashtable _innerProperties = new Hashtable();

      /// <summary>Устанавливает свойство, связанного с именем.
      /// Если свойство уже существует, значение будет заменено.
      /// Если свойство не существует, оно будет добавлено со значением.
      /// </summary>
      public void SetProperty(string name, object value)
      {
          if(name == null) return;
          if(_innerProperties.ContainsKey(name))
              _innerProperties[name] = value;
          else
              _innerProperties.Add(name, value);
      }

      /// <summary>Выборка значения свойства по определенному имени.</summary>
      public object GetProperty(string name)
      {
          if(name == null || !_innerProperties.ContainsKey(name)) return null;
          return _innerProperties[name];
      }

      /// <summary>Выборка всех имеющихся свойств.</summary>
      public string[] GetPropertyNames()
      {
          return _innerProperties.Keys.Cast<string>().ToArray();
      }

      /// <summary>Удаление свойства, связанного с определенным именем.</summary>
      public void RemoveProperty(string name)
      {
          if(name == null || !_innerProperties.ContainsKey(name)) return;
          _innerProperties.Remove(name);
      }

      /// <summary>Удаление всех дополнительных свойств.</summary>
      public void RemoveProperties()
      {
          _innerProperties.Clear();
      }

      public string Id { get; set; }
      public string Title { get; set; }
      public decimal Rating { get; set; }
      public decimal Price { get; set; }
      public int Available { get; set; }
      public string Description { get; set; }
}
/// <summary>Интерфейс, описывающий взаимодействие с контейнером свойств.</summary>
public interface IPropertyContainer
{
      void SetProperty(string name, object value);
      object GetProperty(string name);
      string[] GetPropertyNames();
      void RemoveProperty(string name);
      void RemoveProperties();
}

/// <summary>Класс, реализующий контейнер свойств.</summary>
public class PropertyContainer : IPropertyContainer
{
      private Hashtable _innerProperties = new Hashtable();

      /// <summary>Устанавливает свойство, связанного с именем.
      /// Если свойство уже существует, значение будет заменено.
      /// Если свойство не существует, оно будет добавлено со значением.
      /// </summary>
      public void SetProperty(string name, object value)
      {
          if(name == null) return;
          if(_innerProperties.ContainsKey(name))
              _innerProperties[name] = value;
          else
              _innerProperties.Add(name, value);
      }

      /// <summary>Выборка значения свойства по определенному имени.</summary>
      public object GetProperty(string name)
      {
          if(name == null || !_innerProperties.ContainsKey(name)) return null;
          return _innerProperties[name];
      }

      /// <summary>Выборка всех имеющихся свойств.</summary>
      public string[] GetPropertyNames()
      {
          return _innerProperties.Keys.Cast<string>().ToArray();
      }

      /// <summary>Удаление свойства, связанного с определенным именем.</summary>
      public void RemoveProperty(string name)
      {
          if(name == null || !_innerProperties.ContainsKey(name)) return;
          _innerProperties.Remove(name);
      }

      /// <summary>Удаление всех дополнительных свойств.</summary>
      public void RemoveProperties()
      {
          _innerProperties.Clear();
      }
}
/// <summary>Интерфейс, описывающий фильм.</summary>
public interface IMovie
{
      string Id { get; set; }
      string Title { get; set; }
      decimal Rating { get; set; }
      decimal Price { get; set; }
      int Available { get; set; }
      string Description { get; set; }
}

public interface IMovieExtended: IMovie, IPropertyContainer
{

}

/// <summary>Реализация класса фильма, наследуемого от контейнера свойств.</summary>
public class MovieImplementation1 : PropertyContainer, IMovieExtended
{
      public string Id { get; set; }
      public string Title { get; set; }
      public decimal Rating { get; set; }
      public decimal Price { get; set; }
      public int Available { get; set; }
      public string Description { get; set; }
}

/// <summary>Реализация класса фильма, наследуемого от класса внешнего поставщика 
/// и содержащего контейнер свойств.</summary>
public class MovieImplementation2 : MovieByVender, IMovieExtended
{
      private PropertyContainer _propertyContainer = new _propertyContainer();

      public void SetProperty(string name, object value)
      {
          _propertyContainer.SetProperty(name, value);
      }

      public object GetProperty(string name)
      {
          return _propertyContainer.GetProperty(name);
      }

      public string[] GetPropertyNames()
      {
          return _propertyContainer.GetPropertyNames();
      }

      public void RemoveProperty(string name)
      {
          _propertyContainer.RemoveProperty(name);
      }

      public void RemoveProperties()
      {
          _propertyContainer.RemoveProperties();
      }
}
movies.Add(new MovieImplementation());

movies[i].Rating = 6.3;

movies[i].SetProperty("releasedate", new DateTime(2002, 5, 22));
