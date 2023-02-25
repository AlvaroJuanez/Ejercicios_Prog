/*
 * DosEnOrden: El programa te pide 2 numeros, los cuales ordena y los imprime por pantalla 
 * de menor a mayor.
 * @author: Alvaro Juanez M
 * @version: 1.0 26/01/2023
 *
 */
import java.util.Scanner;

public class DosEnOrden{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);   //Entrada de datos

        //Guarda los valores de las variables
        int num1, num2;

        //Incicia el programa, intereactua con el usuario
        System.out.println("Introduce el primer numero");
        num1 = scanner.nextInt();
        System.out.println("Introduce el segundo numero");
        num2 = scanner.nextInt();
        
        scanner.close(); //Cierre scanner

        //Ordena los numero de menor a mayor
        if(num1 > num2){
            System.out.println(num2 + " i " + num1);
        }else if(num2 > num1){
            System.out.println(num1 + " i " + num2);
        }
    }
}

