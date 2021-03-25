import java.rmi.*;
import java.rmi.registry.*;
public class MyServer
{
public static void main(String args[]) //Main Method
{
try
{
AdderInt stub=new AdderRemote(); //object creation & calling
Naming.rebind("rmi://localhost:/abc",stub);
}
catch(Exception e)
{
System.out.println(e);
}
}
}
