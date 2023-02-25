/*
 * El programa Duplica: como su nombre indica duplica cualquier numero, que se le envie como argumento
 * mediante la consola.
 *
 * @author: Alvaro Juanez M
 * @version: 1.0 - 25/01/2023
 *
 */
import java.util.Scanner;

public class Duplica{
    public static void main(String[] args){
        //Entrada de datos
        Scanner scanner = new Scanner(args[0]);

        //Guarda el valor de las variables
        int num = scanner.nextInt();
        int numDuplicado;
        
        scanner.close();     //Cierre de la utilidad scanner

        numDuplicado = num * 2;     //Duplica el numero
        System.out.println("El doble de " + num + " es " + numDuplicado);
    }
}

