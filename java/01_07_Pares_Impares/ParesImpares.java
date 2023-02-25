/*
 * ParesImpares: El programa pide al usuario que ingrese un numero como argumento si es par le dice que es par,
 * de lo contrario le dira que es impar
 * @author: Alvaro Juanez M
 * @version: 1.0 26/01/2023
 *
 */
import java.util.Scanner;

public class ParesImpares{
    public static void main(String[] args){

        Scanner scanner = new Scanner(args[0]);   //Entrada de datos
        
        //Guarda el valor de las variables
        int numero;

        //Inicia el Programa, interactua con el usuario
        numero = scanner.nextInt(); 

        scanner.close(); //Cierre scanner

        //Si es par
        if(numero % 2 == 0){
            System.out.println("El numero es Par");
        }else{
            System.out.println("El numero es Impar");
        }
    }
}

