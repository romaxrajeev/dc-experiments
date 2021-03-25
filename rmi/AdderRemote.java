import java.rmi.*;
import java.rmi.server.*; //packages
public class AdderRemote extends UnicastRemoteObject implements AdderInt
{
AdderRemote()throws RemoteException //constructor
{
super();
}
public int add(int x,int y)
{
return x+y;
}
}
