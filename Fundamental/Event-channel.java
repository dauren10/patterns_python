'''
Канал событий (англ. event channel) — фундаментальный шаблон проектирования, используется для создания канала связи и коммуникации через него посредством событий. Этот канал обеспечивает возможность разным издателям публиковать события и подписчикам, подписываясь на них, получать уведомления.

Этот шаблон является расширением шаблона Издатель-подписчик (Publish/Subscribe) путем добавления функций, которые присущи распределенной среде. Так канал является централизованным и подписчик может получать опубликованные события от более, чем одного объекта, даже если он зарегистрирован только на одном канале.

В общем случае шаблон Канал событий описывает интерфейс для объектов-представителей для подписки на канал событий и для объектов-представителей для публикации событий в рамках канала. Использование неких представителей позволяет взаимодействовать настоящим издателям и подписчикам вне рамках самого канала, но посредством него.

Концептуальное описание канала событий показано ниже: 
'''
public interface IEventChannel
{
    void Publish(string topic, string data);
    void Subscribe(string topic, ISubscriber subscriber);
}

public interface IPublisher
{
    void Publish(string data);
}

public interface ISubscriber
{
    void Notify(string data);
}

public class EventChannel: IEventChannel
{
    private Dictionary<string, List<ISubscriber>> _topics = 
        new Dictionary<string, List<ISubscriber>>();
    
    public void Publish(string topic, string data)
    {
        if(!_topics.ContainsKey(topic)) return;
        foreach(var subscriber in _topics[topic])
            subscriber.Notify(data);
    }

    public void Subscribe(string topic, ISubscriber subscriber)
    {
        if(_topics.ContainsKey(topic))
            _topics[topic].Add(subscriber);
        else
            _topics.Add(topic, new List<ISubscriber>() { subscriber });
    }
}

public class Publisher: IPublisher
{
    private string _topic;
    private IEventChannel _channel;
    public Publisher(string topic, IEventChannel channel)
    {
           _topic = topic;
           _channel = channel;
    }

    public void Publish(string data)
    {
           _channel.Publish(_topic, data);
    }
}

public class Subscriber: ISubscriber
{
    private string _name;
    public Subscriber(string name)
    {
           _name = name;
    }

    public void Notify(string data)
    {
           Console.Write($"Subscriber '{_name}' notify: '{data}'")
    }
}

static class Program
{
    public void Main(string[] args)
    {
           var channel = new EventChannel();
           var publisherA = new Publisher("#topic.a", channel);
           var publisherB = new Publisher("#topic.b", channel);
           var subscriberA = new Subscriber("Reader 1");
           var subscriberB = new Subscriber("Reader 2");

           channel.Subscribe("#topic.a", subscriberA);
           channel.Subscribe("#topic.a", subscriberB);
           channel.Subscribe("#topic.b", subscriberB);

           // Console write: Subscriber 'Reader 1' notify: 'Text1'
           // Console write: Subscriber 'Reader 2' notify: 'Text1'
           publisherA.Publish("Text1");

           // Console write: Subscriber 'Reader 2' notify: 'Text2'
           publisherB.Publish("Text2");
    }
}