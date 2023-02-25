/*
 * CalculadoraBasica:  El programa simula el funcionamiento de una calculador sencilla
 * que opera sumas, restas, mutlipicación, division.
 * @author: Alvaro Juanez M
 * @version: 
 *
 */
import java.util.Scanner;

public class CalculadoraBasica{
    public static void main(String[] args){
        //Entrada de datos
        Scanner scanner = new Scanner(System.in);

        //Guarda el valor de las variables
        int num1, num2, total;

        //Inicializa el programa
        System.out.println("Introduce el primer numero");
        num1 = scanner.nextInt();
        System.out.println("Introduce el segundo numero");
        num2 = scanner.nextInt();

        scanner.close();    //cierre de scanner

        //Imprime el resultado de las operaciones matematicas
        System.out.println(num1 + " + " + num2 + " = " + (total = num1 + num2));
        System.out.println(num1 + " - " + num2 + " = " + (total = num1 - num2));
        System.out.println(num1 + " * " + num2 + " = " + (total = num1 * num2));
        System.out.println(num1 + " / " + num2 + " = " + (total = num1 / num2));
    }
}

