'''Обеспечивает унифицированный интерфейс для интерфейсов в подсистеме. 
Front Controller определяет высокоуровневый интерфейс, упрощающий использование подсистемы.'''
class TeacherView
{
	public void display()
	{
		System.out.println("Teacher View");
	}
}

class StudentView
{
	public void display()
	{
		System.out.println("Student View");
	}
}

class Dispatching
{
	private StudentView studentView;
	private TeacherView teacherView;
	
	public Dispatching()
	{
		studentView = new StudentView();
		teacherView = new TeacherView();
	}

	public void dispatch(String request)
	{
		if(request.equalsIgnoreCase("Student"))
		{
			studentView.display();
		}
		else
		{
			teacherView.display();
		}	
	}
}

class FrontController
{
	private Dispatching Dispatching;

	public FrontController()
	{
		Dispatching = new Dispatching();
	}

	private boolean isAuthenticUser()
	{
		System.out.println("Authentication successful.");
		return true;
	}

	private void trackRequest(String request)
	{
		System.out.println("Requested View: " + request);
	}

	public void dispatchRequest(String request)
	{
		trackRequest(request);
		
		if(isAuthenticUser())
		{
			Dispatching.dispatch(request);
		}	
	}
}

class FrontControllerPattern
{
	public static void main(String[] args)
	{
		FrontController frontController = new FrontController();
		frontController.dispatchRequest("Teacher");
		frontController.dispatchRequest("Student");
	}
}
