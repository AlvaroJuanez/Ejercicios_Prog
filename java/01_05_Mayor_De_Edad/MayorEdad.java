/*
 * MayorEdad: el programa verifica la edad de ususario si es mayo o menor
 * Si es mayor le dira pudes ir a la carcel que tenga cuidado, de los contrario
 * que ande con cuidado.
 * @author: Alvaro Juanez M
 * @version: 1.0 - 26/01/2023
 *
 */
import java.util.Scanner;

public class MayorEdad{
    public static void main(String[] args){

        //Entrada de datos
        Scanner scanner = new Scanner(System.in);

        //Guarda las variables
        int edad;
        String nombre;

        //Interactua con el ususario obten los datos necesarios
        System.out.println("¿Cual es tu nombre?");
        nombre = scanner.nextLine(); 
        System.out.println("¿Cuantos años tienes?");
        edad = scanner.nextInt(); 
        
        scanner.close();    //Cierre Scanner

        //si es mayor de edad carcel
        if(edad >= 18){
            System.out.println("Eres mayor de edad, cuidado con lo que haces \npuedes ir  a la carcel " + nombre);
        }else{
            System.out.println("Eres menor de edad " +  nombre + " anda con cuidado");
        }
    }
}

