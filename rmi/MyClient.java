import java.rmi.*;
public class MyClient
{
public static void main(String args[]){
try
{
AdderInt stub=(AdderInt)Naming.lookup("rmi://localhost:/abc");
System.out.println("Addition of two numbers :"+stub.add(4,1));
}
catch(Exception e)
{
}
}
}
