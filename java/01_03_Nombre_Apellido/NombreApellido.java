/*
 * NombreApellido: El programa interactua con el usuario, con mensajes interactivos con el objetivo de conoce
 * el nombre, del usuario y saludarlo.
 * @author: Alvaro Juanez M
 * @version: 1.0 - 25/01/2023
 *
 */
import java.util.Scanner;

public class NombreApellido{
    public static void main(String[] args){
        //Entrada de datos
        Scanner scanner = new Scanner(System.in);

        //Variables, valores Guardados
        String nombre, apellido;

        //Inicializa el programa 
        System.out.println("¿como te llamas?");
        nombre = scanner.nextLine();
        System.out.println("¿Cual es tu apellido?");
        apellido = scanner.nextLine();

        scanner.close();    //Cierre Scanner

        //saluda al usuario
        System.out.println("Hola, como estas " + nombre + "\ntienes un apellido interesante " + apellido);    
    }
}

