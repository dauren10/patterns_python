Singleton (одиночка)

Один из самых известных и, пожалуй, самых спорных паттернов.
Представьте, что в городе требуется организовать связь между жителями. С одной стороны мы можем связать всех жителей между собой протянув между ними кабели телефонных линий, но полагаю вы понимаете насколько такая система неверна. Например, как затратно будет добавить еще одного жителя в связи (протянуть по еще одной линии к каждому жителю). Чтобы этого избежать, мы создаем телефонную станцию, которая и будет нашим «одиночкой». Она одна, всегда, и если кому-то потребуется связаться с кем-то, то он может это сделать через данную телефонную станцию, потому что все обращаются только к ней. Соответственно для добавления нового жителя нужно будет изменить только записи на самой телефонной станции. Один раз создав телефонную станцию все могут пользоваться ей и только ей одной, в свою очередь эта станция помнит всё что с ней происходило с момента ее создания и каждый может воспользоваться этой информацией, даже если он только приехал в город.
Основной смысл «одиночки» в том, чтобы когда вы говорите «Мне нужна телефонная станция», вам бы говорили «Она уже построена там-то», а не «Давай ее сделаем заново». «Одиночка» всегда один.

Примечание:
Несмотря на удобство применения данного паттерна, он является одним из самых спорных при разработке и рекомендуется его применять только если нет никакого другого способа решения, потому как это создает значительные сложности при тестировании кода, однако это уже отдельная тема.

Registry (реестр, журнал записей)

Как следует из названия, данный паттерн предназначен для хранения записей которые в него помещают и соответственно возвращения этих записей (по имени) если они потребуются. В примере с телефонной станцией, она является реестром по отношению к телефонным номерам жителей.

Паттерны «одиночка» и «реестр» постоянно встречаются нам в повседневной жизни. Например бухгалтерия в фирме является «одиночкой», потому как она всегда одна и помнит что с ней происходило с момента ее начала работы. Фирма не создает каждый раз новую бухгалтерию когда ей требуется выдать зарплату. В свою очередь бухгалтерия является и «реестром», потому как в ней есть записи о каждом работнике фирмы.

Примечание:
«Реестр» нередко является «одиночкой», однако это не всегда должно быть именно так. Например мы можем заводить в бухгалтерии несколько журналов, в одном работники от «А» до «М», в другом от «Н» до «Я». Каждый такой журнал будет «реестром», но не «одиночкой», потому как журналов уже 2. Хотя нередко «реестр» служит именно для хранения «одиночек».
Сам паттерн «реестр» не являтся «порождающим паттерном» в полном смысле этого термина, однако его удобно рассматривать именно во взаимосвязи с ними.

Multiton (пул «одиночек»)

Как понятно из названия паттерна, это по своей сути «реестр» содержащий несколько «одиночек», каждый из которых имеет своё «имя» по которому к нему можно получить доступ.

Object pool (пул объектов)

По аналогии с «пулом одиночек» данный паттерн также позволяет хранить уже готовые объекты, однако они не обязаны быть «одиночками».

Factory (фабрика)

Суть паттерна практически полностью описывается его названием. Когда вам требуется получать какие-то объекты, например пакеты сока, вам совершенно не нужно знать как их делают на фабрике. Вы просто говорите «сделайте мне пакет апельсинового сока», а «фабрика» возвращает вам требуемый пакет. Как? Всё это решает сама фабрика, например «копирует» уже существующий эталон. Основное предназначение «фабрики» в том, чтобы можно было при необходимости изменять процесс «появления» пакета сока, а самому потребителю ничего об этом не нужно было сообщать, чтобы он запрашивал его как и прежде.
Как правило, одна фабрика занимается «производством» только одного рода «продуктов». Не рекомендуется «фабрику соков» создавать с учетом производства автомобильных покрышек. Как и в жизни, паттерн «фабрика» часто создается «одиночкой».

Builder (строитель)

Данный паттерн очень тесно переплетается с паттерном «фабрики». Основное различие заключается в том, что «строитель» внутри себя, как правило, содержит все сложные операции по созданию объекта (пакета сока). Вы говорите «хочу сока», а строитель запускает уже целую цепочку различных операций (создание пакета, печать на нем изображений, заправка в него сока, учет того сколько пакетов было создано и т.п.). Если вам потребуется другой сок, например ананасовый, вы точно также говорите только то, что вам нужно, а «строитель» уже позаботится обо всем остальном (какие-то процессы повторит, какие-то сделает заново и т.п.). В свою очередь процессы в «строителе» можно легко менять (например изменить рисунок на упаковке), однако потребителю сока этого знать не требуется, он также будет легко получать требуемый ему пакет сока по тому же запросу.

Примечание:
Чтобы лучше понять разницу между фабрикой и строителем, можно использовать следующую метафору.
«Фабрика» — это автомат по продаже напитков, в нем уже есть всё готовое (или «осталось разогреть»), а вы только говорите что вам нужно (нажимаете кнопку). «Строитель» — это завод, который производит эти напитки и содержит в себе все сложные операции и может собирать сложные объекты из более простых (упаковка, этикетка, вода, ароматизаторы и т.п.) в зависимости от запроса.

Prototype (прототип)

Данный паттерн чем-то напоминает «фабрику», он также служит для создания объектов, однако с немного другим подходом. Представьте что у вас есть пустой пакет (из под сока), а вам нужен полный с апельсиновым соком. Вы «говорите» пакету «Хочу пакет апельсинового сока», он в свою очередь создает свою копию и заполняет ее соком, который вы попросили. Немного «сказочный пример», но в программировании часто так и бывает. В данном случае пустой пакет и является «прототипом», и в зависимости от того что вам требуется, он создает на своей основе требуемые вами объекты (пакеты сока).
Клонирование не обязательно должно производится на самом «пакете», это может быть и какой-то другой «объект», главное лишь что данный «прототип» позволяет получать его экземпляры.

Factory method (фабричный метод)

Данный паттерн довольно сложно объяснить в метафорах, но всё же попробую.
Ключевой сложностью объяснения данного паттерна является то, что это «метод», поэтому метафора метода будет использовано как действие, то есть например слово «Хочу!». Соответственно, паттерн описывает то, как должно выполнятся это «Хочу!».
Допустим ваша фабрика производит пакеты с разными соками. Теоретически мы можем на каждый вид сока делать свою производственную линию, но это не эффективно. Удобнее сделать одну линию по производству пакетов-основ, а разделение ввести только на этапе заливки сока, который мы можем определять просто по названию сока. Однако откуда взять название?
Для этого мы создаем основной отдел по производству пакетов-основ и предупреждаем все под-отделы, что они должны производить нужный пакет с соком про простому «Хочу!» (т.е. каждый под-отдел должен реализовать паттерн «фабричный метод»). Поэтому каждый под-отдел заведует только своим типом сока и реагирует на слово «Хочу!».
Таким образом если нам потребуется пакет апельсинового сока, то мы просто скажем отделу по производству апельсинового сока «Хочу!», а он в свою очередь скажет основному отделу по созданию пакетов сока, «Сделай ка свой обычный пакет и вот сок, который туда нужно залить».

Примечание:
Как вы могли уже заметить, «фабричный метод» является как бы основой для «фабрики», «строителя» и «прототипа». В разработке часто именно так и получается, сперва реализуют фабричный метод, а по мере усложнения кода выбирают во что именно его преобразовать, в какой из перечисленных паттернов. При использовании «фабричного метода» каждый объект как бы сам является «фабрикой».

Lazy initialization (отложенная инициализация)

Иногда требуется что-то иметь под рукой, на всякий случай, но не всегда хочется прилагать каждый раз усилия, чтобы это каждый раз получать/создавать. Для таких случаев используется паттерн «отложенная инициализация». Допустим вы работаете в бухгалтерии и для каждого сотрудника вы должны подготавливать «отчет о выплатах». Вы можете в начале каждого месяца делать этот отчет на всех сотрудников, но некоторые отчеты могут не понадобиться, и тогда скорее всего вы примените «отложенную инициализацию», то есть вы будете подготавливать этот отчет только тогда, когда он будет запрошен начальством (вышестоящим объектом), однако начальство по сути в каждый момент времени может сказать что у него этот отчет уже есть, однако готов он уже или нет, оно не знает и знать не должно. Как вы уже поняли, данный паттерн служит для оптимизации ресурсов.

Dependency injection (внедрение зависимости)

Внедрение зависимости позволяет переложить часть ответственности за какой-то функционал на другие объекты. Например если нам требуется нанять новый персонал, то мы можем не создавать свой отдел кадров, а внедрить зависимость от компании по подбору персонала, которая свою очередь по первому нашему требованию «нам нужен человек», будет либо сама работать как отдел кадров, либо же найдет другую компанию (при помощи «локатора служб»), которая предоставит данные услуги.
«Внедрение зависимости» позволяет перекладывать и взаимозаменять отдельные части компании без потери общей функциональности.

Service Locator (локатор служб)
автор: VolCh
«Локатор служб» является методом реализации «внедрения зависимости». Он возвращает разные типы объектов (компаний) в зависимости от кода инициализации. Пускай задача стоит доставить наш пакет сока, созданный строителем, фабрикой или ещё чем, куда захотел покупатель. Мы спрашиваем у локатора «дай нам службу доставки», и он нам соединяет на со службой доставки по номеру телефона, который директор ему дал (потому что получает откат они нам дают скидку как постоянным клиентам), а мы уже просим службу доставить сок по нужному адресу. Сегодня одна служба, а завтра может быть другая. Нам без разницы какая это конкретно служба, решение принимает директор и сообщает об этом локатору служб, нам важно знать лишь что они могут доставлять то, что мы им скажем туда, куда скажем, то есть службы реализуют интерфейс «Доставить <предмет> на <адрес>».

Структурирующие паттерны

Данные паттерны помогают внести порядок и научить разные объекты более правильно взаимодействовать друг с другом.

Adapter или wrapper (адаптер, обертка)

Данный паттерн полностью соответствует своему названию. Чтобы заставить работать «советскую» вилку через евро-розетку требуется переходник. Именно это и делает «адаптер», служит промежуточным объектом между двумя другими, которые не могут работать напрямую друг с другом.

Bridge (мост)

Представим ситуацию, когда вам требуется работать на разных автомобилях, однако садясь в новый автомобиль вам уже желательно знать как им управлять. Таким образом вы сталкиваетесь с паттерном «мост». С одной стороны вы имеете множество различных автомобилей (разные модели и марки), но среди все них есть общая абстракция (интерфейс) ввиде руля, педалей, коробки передач и так далее. Таким образом мы задаем как-бы правила изготовления автомобилей по которым мы можем создавать любые их виды, но за счет сохранения общих правил взаимодействия с ними, мы можем одинаково управлять каждым из них. «Мостом» в данном случае является пара двух «объектов»: конкретного автомобиля и правил взаимодействия с этим (и любым другим) автомобилем.

Composite (компоновщик)

Довольно интересный паттерн суть которого заключается в минимизации различий в управлении как группами объектов так и индивидуальными объектами. Для примера можно рассмотреть управление солдатами в строю. Существует строевой устав, который определяет как управлять строем и согласно этого устава абсолютно не важно кому отдается приказ (например «шагом марш») одному солдату или целому взводу. Соответственно в устав (если его в чистом виде считать паттерном «компоновщик») нельзя включить команду, которую может исполнить только один солдат, но не может исполнить группа, или наоборот.

Decorator (декоратор, оформитель)

Как понятно из названия, данный паттерн чаще всего используется для расширения исходного объекта до требуемого вида. Например мы условно можем считать «декоратором» человека с кистью и красной краской. Таким образом, какой бы объект (или определенный тип объектов) мы не передали в руки «декоратору», на выходе мы будем получать красные объекты.

Facade (фасад)

Паттерн «фасад» используется для того, чтобы делать сложные вещи простыми. Возьмем для примера автомобиль. Представьте, если бы управление автомобилем происходило немного по-другому: нажать одну кнопку чтобы подать питание с аккумулятора, другую чтобы подать питание на инжектор, третью чтобы включить генератор, четвертую чтобы зажечь ламочку на панели и так далее. Всё это было бы очень сложно. Для этого такие сложные наборы действий заменяются более простыми и комплексные как «повернуть ключ зажигания». В данном случае поворот ключа зажигания и будет тем самым «фасадом» для всего обилия внутренних действий автомобиля.

Front controller (единая точка входа)

Если проводить аналогии с реальными миром, то «единая точка входа» это то, через что вы сейчас читаете данную статью (например броузер). Она служит «единой точкой входа» для всего интернет пространства. То есть вы используете один интерфейс (броузер) для получения доступа к разным объектам большой системы (сайтам в интернете). Данный паттерн в целом сильно похож на «фасад».

Flyweight (приспособленец)

Самым лучшим примером (который я смог найти в реальной жизни) для метафорического сравнения паттерна «приспособленец» является театральная постановка. Представьте что нам требуется поставить пьесу. Однако по сценарию в этой пьесе задействованы несколько десятков людей, которые по своей сути выполняют одинаковые действия, например участвуют в массовках различных сцен в разные промежутки времени, но между ними всё же есть какие-то различия (например костюмы). Нам бы стоило огромных денег нанимать для каждой роли отдельного актера, поэтому мы используем паттерн «приспособленец». Мы создадим все нужные нам костюмы, но для каждой массовки будем переодевать небольшую группу актеров в требуемые для этой сцены костюмы. В результате мы имеем возможность ценой малых ресурсов создавать видимость управления большим количеством казалось бы разных объектов.

Proxy или surrogate (прокси, заместитель, суррогат)

Данный паттерн позволяет создавать какие-либо специальные механизмы доступа к объекту, что чаще всего направлено именно на улучшение производительности отдельных частей программы. В реальной жизни можно привести следующий пример: сотрудникам одного из подразделений фирмы регулярно требуется получать информацию о том, какого числа бухгалтерия планирует выплатить зарплату. С одной стороны каждый из них может индивидуально и регулярно ездить в бухгалтерию для выяснения этого вопроса (полагаю такая ситуация нередко встречается во многих организациях). С другой стороны, при приближении планируемой даты подразделение может выбрать одного человека, который будет выяснять эту информацию у бухгалтерии, а в последствии уже все в подразделении могут выяснить эту информацию у него (что значительно быстрее). Вот именно этот человек и будет реализованным «прокси» паттерном, который будет предоставлять специальный механизм доступа к информации из бухгалтерии.

Паттерны поведения

Эта группа паттернов позволяет структурировать подходы к обработке поведения и взаимодействия объектов. Проще говоря, как должны проходить процессы в которых существует несколько вариантов протекания событий.

Chain of responsibility (цепочка обязанностей)

Самым простым примером цепочки обязанностей можно считать получение какого-либо официального документа. Например вам требуется получить справку со счета из банка. Так или иначе, вы должны эту справку получить, однако кто именно ее должен вам дать — пока не ясно. Вы приходите в местное отделение банка, вам говорят что «мы сейчас заняты, идите в другое отделение», дальше вы идете в другое, там вам отвечают «мы этим не занимаемся», вы идете в региональное отделение и там получаете нужную справку. Таким образом паттерн реализует «цепочку обязанностей» отдельные объекты которой (отделения банка) должны обработать ваш запрос. Соответственно ваш запрос может быть обработан в первом же отделении, или же в нескольких, в зависимости от самого запроса и обрабатывающих объектов.

Command или action (команда, действие)

Паттерн «команда» очень похож в реальной жизни на кнопки выключателей света в наших квартирах и домах. Каждый выключатель по своей сути делает одно простое действие — разъединяет или соединяет два провода, однако что стоит за этими проводами выключателю не известно. Что подключат, то и произойдет. Точно также действует и паттерн «команда». Он лишь определяет общие правила для объектов (устройств), в виде соединения двух проводов для выполнения команды, а что именно будет выполнено уже определяет само устройство (объект).
Таким образом мы можем включать одним типом выключателей как свет в комнате, так и пылесос.

Interpreter (интерпретатор)

Сравнить данный паттерн можно с тем, как вы закладываете часто используемые действия в сокращенный набор слов, чтобы сам «интерпретатор» потом превратил этот набор в более комплексные осмысленные действия. По сути каждый человек постоянно является «интерпретатором». Хотите провести жизненный эксперимент? Если из дома выходит кто-то из вашей семьи (муж, жена, ребенок), скажите ему простой набор слов «Литр молока, половинку белого, 200 грамм творога». По сути вы ничего особенного не сказали, лишь перечислили набор продуктов, однако велик шанс того, что «интерпретатор» транслирует это в команду «зайди по дороге в продуктовый магазин и купи следующее … и принеси это домой». Паттерн «интерпретатор» призван сократить часто исполняемые действия в более короткое их описание.

Iterator (итератор, указатель)

Все помнят школьное «на первый второй рассчитайся!»? Вот именно в этот момент шеренга вашего класса и являлась реализацией паттерна «итератор», хотя в программировании это конечно более функциональное понятие, но суть примерно та же. «Итератор» предоставляет правила доступа к списку каких-либо объектов независимо от того, что это за объекты. То есть не важно какой именно класс построен и из каких учеников, должны быть общие правила подсчета и обращения как каждому ученику по списку, вроде «13-ый, выйти из строя». Нередко паттерн «итератор» используется для доступа к «реестру». Ссылки, которые вы видите на многих сайтах для переходов по страницам, вроде «следующая», «предыдущая», «в начало» и т.п. по своей сути также являются доступом «итератору» который отвечает за страницы сайта.

Mediator (посредник)

Вспомним пример из паттерна «одиночка». Так вот телефонная станция в том примере по сути также являлась паттерном «посредник», то есть обеспечивала взаимодействие группы объектов без необходимости обеспечения связи каждого объекта друг с другом.
Однако дополнительной ответственность этого «паттерна» является также управление этой группой через «посредника». То есть если мы возьмем пример с армейским строем, то медиатором будет командир отделения, то есть нам нет необходимости взаимодействовать с каждым солдатом в отдельности, достаточно отдавать приказания лишь командиру отделения, а он уже сам решит какие действия должны быть выполнены внутри его отделения.

Memento (хранитель)

Никогда не просили друга с сотовым телефоном на время запомнить (записать себе) тот номер, что диктуют вам по телефону, потому что вы не можете его запомнить сами (телефон занят)? В этот момент ваш друг реализовывал паттерн «хранитель». Он служит для тех случаев, когда какому-либо объекту требуется сохранить своё состояние (состояние знания номера) в другом объекте (вашем друге), и при необходимости его потом восстановить (спросить у друга номера и тем самым восстановить состояние когда вы его знали). Также уместен аналог с тем, как в играх работает сохранение. Файл «сейва» как раз и будет тем самым паттерном «хранитель».

Observer или Listener (наблюдатель, слушатель)

Очень распространенный паттерн в реальной жизни. Например если вы подписались на какую-либо email (или смс) рассылку, то ваш email (или номер сотового телефона) начинает реализовывать паттерн «наблюдатель». Как только вы подписываетесь на событие (например новая статья или сообщение), всем кто подписан на это событие (наблюдателям) будет выслано уведомление, а они уже в свою очередь могут выбрать как на это сообщение реагировать.

Blackboard (доска объявлений)

Данный паттерн служит для обеспечения взаимодействия между большим количеством объектов. Он является расширением паттерна «наблюдатель» и позволяет централизованно обслуживать как «наблюдателей», так и «создателей событий». В аналогии подпиской на email уведомления, это будет сам сайт подписки, который обслуживает множество подписчиков и тех, кто для них создает информацию (сообщения).

Servant (слуга)

Как следует из названия, данный паттерн служит для предоставления группе объектов какого-либо общего функционала. Например телефонная станция является для жителей города паттерном «слуга» если речь заходит о том, как узнать точное время (набрать номер 100).

State (состояние)

В реальной жизни каждый человек может прибывать в разных состояниях. Точно также порой требуется чтобы объекты в программе вели себя по разному в зависимости от каких-либо их внутренних состояний. По аналогии с реальной жизнью можно например привести следующий пример:
Если вы устали то на фразу «Сходи в магазин» вы будете выдавать «Не пойду», если вам нужно сходить в магазин (за пивом?), то на «Сходи в магазин» вы будете выдавать «Уже бегу!». Человек (объект) один и тот же, а поведение разное. Именно для этих целей и используют паттерн «состояние».

Strategy (стратегия)

Используется для выбора различных путей получения результата. Вспомним пример с получением прав. Человек, который будет реализовывать паттерн «стратегия» будет действовать следующим образом: вы говорите ему «Хочу права, денег мало» в ответ вы получите права через длительное время и с большой тратой ресурсов. Если вы скажите ему «Хочу права, денег много», то вы получите права очень быстро. Что именно делал этот человек вы понятия не имеете, но вы задаете начальные условия, а как себя вести уже решает он сам (сам выбирает стратегию).
Соответственно внутри «стратегии» хранятся различные способы поведения, и чтобы выбрать, ему нужны определенные параметры, в данном случае это объем денежных средств. Как устроена сама «стратегия» и какие алгоритмы внутри нее вам собственно знать и требуется.

Specification (спецификация, определение)

Паттерн спецификации позволяет описывать подходит ли данный объект нам на основе каких-либо критериев. Например мы имеем несколько контейнеров для погрузки на судно. Однако чтобы определить грузить контейнер или нет на определенное судно, нам нужно выбрать метод как это определять. Реализация такого метода и является паттерном «спецификация». В самом простом случае для каждого контейнера мы можем определить в паттерне «спецификация» совпадает ли страна назначения корабля со страной назначения контейнера. Соответственно мы один раз вводим правило «сравнить две страны назначения» и применяем его ко всем контейнерам для проверки.

Subsumption (категоризация)

Данный паттерн является прямым последователем паттерна «спецификация». Он позволяет распределять объекты по категориям на основе каких-либо условий. Соответственно по аналогии с примером кораблей и контейнеров, это категоризация по тому, какие контейнеры в какие страны направляются.

Visitor (посетитель)

Данный паттерн можно сравнить с прохождением обследования в больнице. Однако «посетителем» в терминах паттернов здесь будут сами врачи. Чтобы было понятнее: у нас есть больной которого требуется обследовать и полечить, но так как за разные обследования отвечают разные врачи, то мы просто присылаем к больному врачей в качестве «посетителей». Правило взаимодействия для больного очень простое «пригласите врача (посетителя) чтобы он сделал свою работу», а врач («посетитель») приходит, обследует и делает всё необходимое. Таким образом следуя простым правилам можно использовать врачей для разных больных по одним и тем же алгоритмам. Как уже было сказано, паттерном «посетитель» в данном случае является врач, который может одинаково обслуживать разные объекты (больных) если его позовут.

Single-serving visitor (одноразовый посетитель)

Является частным случаем использования паттерна «посетитель». Если в случае с обычным «посетителем» у нас есть врач которого мы можем отправить к разным больным (и при желании по несколько раз), то в данном паттерне можно привести аналогию, что мы нанимаем врача, отправляем его к одному больному и после обследования сразу увольняем.

Hierarchical visitor (иерархический посетитель)

Тот же самый паттерн «посетитель», однако в данном случае он отправляется к не одному больному, а в целую больницу и обходит там всех больных.