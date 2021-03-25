import java.rmi.*; //package
public interface AdderInt extends Remote
{
public int add(int x,int y)throws RemoteException; //abstract method
}
